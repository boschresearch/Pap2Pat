import re
from typing import TYPE_CHECKING

from transformers import PreTrainedTokenizerBase

from src.utils.general import get_logger

if TYPE_CHECKING:
    from src.dataset.chunk import PatentChunk
    from src.dataset.dataset import PatentDraftingSample

log = get_logger(__file__)


outline_granularities = {
    "long": 500,
    "medium": 1000,
    "short": 2000,
}


class Prompt:
    INSTRUCTION = (
        "Limit your response to the sections mentioned in the outline: {headings}. "
        "Remember what you have already written and do not repeat yourself."
    )
    SYSTEM_PROMPT = """### ROLE

You are a highly skilled patent attorney with decades of experience in drafting high-quality patent applications.
You assist scientists in transforming their scientific discoveries into lucrative patents.

### TASK DESCRIPTION

Your task is to draft a patent application.

### INPUTS

As input, you will be provided a research paper and a patent outline, each serving a distinct purpose.

1. Research Paper:

The research paper describes a novel invention to be patented.
The scientist has selected the most relevant excerpts from the paper.
Your task is to extract the invention from the paper and write a patent application for it.

2. Patent Outline:

The patent outline summarizes the desired discourse structure of the patent document.
It is in markdown format and contains a number of bullet points per section.
Use this outline as a rough guidance during drafting.
Note that the number of bullet points is also a strong indicator of the desired length! If bullet points are provided, each one corresponds to about {n_words} words or {n_paragraphs} paragraphs on average.
You should cover all content mentioned in the outline but you are not restricted to it! Feel free to add any further information that you feel would improve the patent application.

3. Prior Patent Outline:

Unless you are asked to generate the beginning of a patent, the user will also provide you with the outline of all prior content.
Use it as global context where you currently stand in the process and do not repeat yourself.

### GUIDELINES

There are a couple of guidelines you need to follow strictly:

- You might be asked to draft only parts of a patent document. Do not draft the whole patent but only those sections requested by the user.
- Copy the headings from the outline exactly. You must include only the headings provided in the outline!
- You must always write complete sentences and avoid keywords, bullet lists and enumerations!
- You must use proper language and maintain a very high level of detail, as you would expect to find in a good patent!
- The patent must act as a standalone document, therefore do not refer to the research paper in the patent!
"""

    OUTLINE_INTRO = "Here is the outline of the desired patent application."
    LENGTH_INFO = " Per bullet point, write roughly {n_paragraphs} paragraphs or {n_words} words.\n"
    PRIOR_OUTLINE_PREFIX = "\n\nFirst, here is the outline of what you have already written:"
    CURRENT_OUTLINE_PREFIX = "Now, continue drafting and add the following points:"
    CLAIM_PROMPT = "We have already finalized the claims for this patent. Here is the first one:\n\n```md\n{claim}\n```\n\n"

    def __init__(self):
        self.n_system_tokens = None
        self.n_user_pc_tokens = None  # paper context
        self.n_user_po_tokens = None  # prior outline
        self.n_user_co_tokens = None  # current outline
        self.n_user_tokens = None  # pc + po + co + instructions
        self.n_assistant_tokens = None

        self._system = None
        self._user = None
        self._assistant = None

        self.paper_context: str | None = None

    @property
    def system(self) -> str:
        if self._system is None:
            raise RuntimeError("System prompt not initialized. Call prepare_system_prompt first")
        return self._system

    @property
    def user(self) -> str:
        if self._user is None:
            raise RuntimeError("User prompt not initialized. Call prepare_user_prompt first")
        return self._user

    @property
    def assistant(self) -> str:
        if self._assistant is None:
            raise RuntimeError(
                "Assistant response not initialized. Call prepare_assistant_response first"
            )
        return self._assistant

    def messages(self, exclude_roles: list[str] = []) -> list[dict[str, str]]:
        return [
            {"role": role, "content": getattr(self, role)}
            for role in ("system", "user", "assistant")
            if role not in exclude_roles
        ]

    def prepare_system_prompt(
        self, tokenizer: PreTrainedTokenizerBase, n_paragraphs: int, n_words: int
    ) -> None:
        self._system = self.SYSTEM_PROMPT.format(n_paragraphs=n_paragraphs, n_words=n_words)
        self.n_system_tokens = len(tokenizer.encode(self._system))

    def prepare_user_prompt(
        self,
        tokenizer: PreTrainedTokenizerBase,
        sample: "PatentDraftingSample",
        chunk: "PatentChunk",
        max_tokens: int,
        add_claim: bool,
    ) -> None:
        if self.paper_context is None:
            log.warning(f"{sample.id}: paper_context not set!")
            paper_context = ""
        else:
            paper_context = self.paper_context.strip()

        prior_outline, current_outline = self._get_outlines(chunk, sample)
        add_prior_outline = bool(prior_outline)
        prior_outline_with_prefix = (
            f"{self.PRIOR_OUTLINE_PREFIX}\n\n```md\n{prior_outline}\n```\n\n"
            if add_prior_outline
            else ""
        )
        current_outline_with_prefix = (
            f"{self.CURRENT_OUTLINE_PREFIX}\n\n```md\n{current_outline}\n```\n"
            if add_prior_outline
            else f"\n\n```md\n{current_outline}\n```\n"
        )

        if sample.patent_outline_suffix != "empty" and re.findall(r"-[^\n]+", current_outline):
            n_chars = outline_granularities[sample.patent_outline_suffix]
            n_paragraphs = max(
                1, n_chars // 590
            )  # 590 = average number of characters per paragraph in the dataset
            n_words = max(
                1, n_chars // 7
            )  # 7 = average number of words per paragraph in the dataset
            length_info = self.LENGTH_INFO.format(n_words=n_words, n_paragraphs=n_paragraphs)
        else:
            length_info = ""

        headings = ", ".join([f'"{heading}"' for heading in get_all_headings(chunk.content)])
        instruction = self.INSTRUCTION.format(headings=headings)

        # select first non-canceled claim
        if add_claim:
            claim = next(cl for cl in sample.patent_content["claims"] if len(cl) > 50)
            claim_prompt = self.CLAIM_PROMPT.format(claim=claim)
        else:
            claim_prompt = ""

        # iteratively reduce outline until instruction fits token limit
        n_iterations = 0
        while True:
            n_iterations += 1
            user_prompt = (
                f"{paper_context}\n\n{claim_prompt}{self.OUTLINE_INTRO}{length_info}"
                f"{prior_outline_with_prefix}{current_outline_with_prefix}{instruction}"
            )
            n_tokens = len(tokenizer.encode(user_prompt))

            if n_iterations > 50:
                log.error(f"Prompt length out of bounds: {sample.id}: {n_tokens} / {max_tokens}")
                break
                # raise Exception("Prompt could not be created!")

            if n_tokens <= max_tokens:
                break
            else:
                reduced_prior_outline = self._reduce_prior_outline(prior_outline)
                if len(reduced_prior_outline) == len(prior_outline):
                    reduced_prior_outline = "\n".join(prior_outline.split("\n")[10:])

                prior_outline = reduced_prior_outline
                prior_outline_with_prefix = (
                    f"{self.PRIOR_OUTLINE_PREFIX}\n\n```md\n{prior_outline}\n```\n\n"
                    if add_prior_outline
                    else ""
                )

        self._user = user_prompt
        self.n_user_tokens = n_tokens
        self.n_user_pc_tokens = len(tokenizer.encode(paper_context))
        self.n_user_po_tokens = len(tokenizer.encode(prior_outline_with_prefix))
        self.n_user_co_tokens = len(tokenizer.encode(current_outline_with_prefix))

    def prepare_assistant_response(
        self, tokenizer: PreTrainedTokenizerBase, chunk: "PatentChunk"
    ) -> None:
        s = ""
        for level, section in iter_sections(chunk.content, level=chunk.level):
            s += f'\n\n{"#" * (level + 1)} {section["title"]}'
            if section["paragraphs"]:
                s += "\n\n"
                s += "\n\n".join(section["paragraphs"])
        self._assistant = f"```md\n{s}\n```"
        self.n_assistant_tokens = len(tokenizer.encode(self._assistant))

    def _get_outlines(
        self, chunk: "PatentChunk", sample: "PatentDraftingSample"
    ) -> tuple[str, str]:
        prior_chunks = []
        for prior_chunk in sample.chunks:
            if chunk is prior_chunk:
                break
            prior_chunks.append(prior_chunk)
        prior_outline = format_outline_md(prior_chunks)
        current_outline = format_outline_md([chunk])
        return prior_outline, current_outline

    def _reduce_prior_outline(self, prior_outline: str, n_sections_per_call: int = 3) -> str:
        def replace_ranges(s: str, ranges: list[tuple[int, int, str]]):
            offset = 0
            for start, end, sub in sorted(ranges, key=lambda x: x[0]):
                s = s[: start + offset] + sub + s[end + offset :]
                offset += len(sub) - (end - start)
            return s

        outline_section_pattern = re.compile(r"(#+ .*)\n\n((- .*\n)+)")
        replacement_ranges = []
        outline_sections = list(outline_section_pattern.finditer(prior_outline + "\n"))[
            :-1
        ]  # never remove bullets from the last section
        n_removed = 0
        for match in outline_sections:
            start_idx, end_idx = match.span()
            heading = match.group(1)
            bullets = [b for b in match.group(2).split("\n") if b.strip()]
            if len(bullets) > 1:
                replacement_ranges.append(
                    (start_idx, end_idx, f"{heading}\n\n<{len(bullets)} bullet points>\n")
                )
                n_removed += 1
                if n_removed >= n_sections_per_call:
                    break

        new_prior_outline = replace_ranges(prior_outline, replacement_ranges)
        return new_prior_outline


def format_reference_patent(sections: list[dict]) -> str:
    """Get the reference patent formatted in markdown"""

    def inner(sections, level=0):
        s = ""
        for section in sections:
            s += f'\n\n{"#" * (level + 1)} {section["title"]}'
            if section["paragraphs"]:
                s += "\n\n" + "\n\n".join(p for p in section["paragraphs"] if p)
            s += inner(section["subsections"], level + 1)
        return s

    return re.sub("\n{2,}", "\n\n", inner(sections))


def iter_secs_with_outline(sec: dict, level: int):
    """Flatten section hierarchy and yield outline along with title and level"""
    yield sec["title"], sec["outline"], level
    for subsec in sec["subsections"]:
        yield from iter_secs_with_outline(subsec, level + 1)


def format_outline_md(chunks: list["PatentChunk"]):
    """Format outline for chunks considering difference edge cases regarding chunk boundaries"""

    def iter_secs_with_outline_and_trace(sec: dict, level: int, trace: list[str]):
        trace = [*trace, sec["title"]]
        yield sec["outline"], trace
        for subsec in sec["subsections"]:
            yield from iter_secs_with_outline_and_trace(subsec, level + 1, trace)

    last_trace = []
    last_print_was_heading = True
    s = ""
    for chunk in chunks:
        for outline, trace in iter_secs_with_outline_and_trace(
            chunk.content, chunk.level, chunk.trace
        ):
            for trace_level, trace_title in enumerate(trace):
                if len(last_trace) <= trace_level or (
                    len(last_trace) > trace_level and last_trace[trace_level] != trace_title
                ):
                    s += f"\n\n{'#' * (trace_level + 1)} {trace_title}"
                    last_print_was_heading = True

            if outline:
                if last_print_was_heading:
                    s += "\n"
                for bullet in outline:
                    s += f"\n- {bullet}"
                    last_print_was_heading = False

            last_trace = trace
    return s.strip()


def format_outline_ref(sections: list[dict], level: int = 0, recursive=True):
    """Format complete outline for verification of `format_outline_md`"""
    s = ""
    for section in sections:
        s += f"\n\n{'#' * (level + 1)} {section['title']}"
        if section["outline"]:
            s += "\n"
            for bullet in section["outline"]:
                s += f"\n- {bullet}"
        if recursive:
            s += format_outline_ref(section["subsections"], level + 1)
    return s


def iter_sections(section: dict, level=1):
    """Flatten section hierarchy yielding level and section"""
    yield level, section
    for subsec in section["subsections"]:
        yield from iter_sections(subsec, level=level + 1)


def iter_sections_with_next(section: dict, level=1):
    """Flatten section hierarchy but also yield the following section"""
    it = iter_sections(section, level)
    try:
        current_sec = next(it)
    except StopIteration:
        return

    for next_sec in it:
        yield current_sec, next_sec
        current_sec = next_sec
    yield current_sec, (None, None)


def get_all_headings(section: dict, level: int = 1, return_hashes: bool = False):
    """Extract all headings from the hierarchy regardless of the level. Used for postprocessing"""
    if return_hashes:
        yield f'{"#" * level} {section["title"]}'
    else:
        yield section["title"]
    for subsec in section["subsections"]:
        yield from get_all_headings(subsec, level=level + 1, return_hashes=return_hashes)
