import json
import re
import time
from pathlib import Path
from typing import Any

import pandas as pd
import rich.live
import rich.syntax
import rich.table
import sglang as sgl
from hydralette import Config, Field
from pyrootutils import setup_root
from sglang.lang.interpreter import ProgramState
from transformers import AutoTokenizer, PreTrainedTokenizerBase

from pap2pat.parsers.type import Section
from pap2pat.utils import get_logger, get_model_info, launch_debugger

root = setup_root(__file__)
log = get_logger(__file__)


cfg = Config(
    remote_url="http://localhost:59532",
    debug=False,
    max_length=2**13,
    papers_dir=root / "data" / "papers",
    system_prompt=(
        "You are a highly skilled patent attorney with decades of experience in drafting high-quality patent applications. "
        "You answer every question in the most concise way possible, without adding unnecessary explanations."
    ),
    prompt_template="""### INSTRUCTION

For the sections of a patent application shown below, write a bullet list that summarizes the discourse structure of the document.

### OUTPUT FORMAT

The output needs to be in markdown syntax. Keep the headings as they are and add bullet lists summarizing the structure of each section. Do NOT write nested lists.

### GUIDELINES

Here are important guidelines you need to follow:

- **{n_words} words per bullet**: Every bullet point should summarize roughly {n_words} words in just a couple of words on a very high level.
- **Structure, not content**: The bullet points should not contain all the content. You should not write a summary of the content, but a summary of the structure! For instance, you should write 'motivate neural networks' rather than writing what the motivation for a neural network is.
- **Start with verbal phrases**: If applicable, start the bullet points with phrases like 'define', 'motivate', 'summarize', 'limitations of', 'application of' or 'embodiment'. You are not restricted to this set of phrases, just use them as inspiration. Avoid overusing the phrase 'describe'.
- **Specificity**: Avoid overly generic bullet points like 'define method' at all cost!
- **Conciseness**: Keep every bullet point as concise as possible! Do NOT write more than 5 words per bullet!
- **{n_bullets} bullet points in total**: You have a fixed budget of bullet points for the whole text. Make sure to write exactly {n_bullets} bullet points in total. This is with respect to all the text you are shown.
- **Coverage**: Since you cannot write more than {n_bullets} bullet points in total, make sure you don't make the list too fine-grained in the beginning. All text must be covered! Use numbers '(i/n)' after the dash as progress indicators with respect to the current section.

### EXAMPLE

Here is an example of the output format:

```md
# HEADING 1 (0 bullet points)

## HEADING 1.1 (2 bullet points)

- (1/2) introduce neural networks
- (2/2) advantage over svm

## HEADING 1.2 (3 bullet points)

- (1/3) derivation of backpropagation
- (2/3) software design of automatic differentiation
- (3/3) example applications
```


### Inputs

Here is the patent application you need to summarize:


```md
{context}
```""",
    n_chars_per_bullet=Field(
        default=[-1, 500, 1000, 2000],
        convert=lambda s: [int(x.strip()) for x in s.split(",")],
    ),
    state_path=root / "data" / "summarization_state.json",
    model=Field(reference=lambda cfg: get_model_info(cfg.remote_url, 120)),
)


def get_num_bullets(section: Section, n_chars_per_bullet: int) -> int:
    if not section["paragraphs"] or n_chars_per_bullet == -1:
        return 0
    n_char = sum(len(p) for p in section["paragraphs"])
    n_bullets = max(1, n_char // n_chars_per_bullet)
    return n_bullets


def get_total_num_bullets(section: Section, n_chars_per_bullet: int) -> int:
    n = get_num_bullets(section, n_chars_per_bullet)
    for subsec in section["subsections"]:
        n += get_total_num_bullets(subsec, n_chars_per_bullet)
    return n


def get_empty_summary(sections: list[Section], level=0):
    s = ""
    for section in sections:
        s += f"{'#' * (level + 1)} {section['title']}\n\n"
        s += get_empty_summary(section["subsections"], level=level + 1)
    return s


def iter_subsecs(
    section: Section, include_heading: bool, n_chars_per_bullet: int, level: int
) -> list[dict[str, Any]]:
    """Flatten the hierarchical representation"""
    main_sec = {
        "title": section["title"],
        "num_bullets": get_num_bullets(section, n_chars_per_bullet),
        "include_heading": include_heading,
        "level": level,
    }
    subsecs = [
        subsec_obj
        for subsec in section["subsections"]
        for subsec_obj in iter_subsecs(subsec, True, n_chars_per_bullet, level + 1)
    ]
    return [main_sec, *subsecs]


def format_section(section: Section, level=0) -> str:
    section_str = f"\n{'#'*(level+1)} {section['title']}\n\n"
    for paragraph in section["paragraphs"]:
        section_str += f"{paragraph}\n\n"
    for subsection in section["subsections"]:
        section_str += format_section(subsection, level + 1)
    return section_str


@sgl.function
def generate_summary(
    s: ProgramState,
    section: Section,
    section_formatted: str,
    include_heading: bool,
    n_chars_per_bullet: int,
    level: int = 0,
):
    n_total_bullets = get_total_num_bullets(section, n_chars_per_bullet)
    n_words_per_bullet = max(1, n_chars_per_bullet // 5)
    s += sgl.system(cfg.system_prompt)
    s += sgl.user(
        cfg.prompt_template.format(
            context=section_formatted.strip(),
            n_bullets=n_total_bullets,
            n_words=n_words_per_bullet,
        )
    )

    s += sgl.assistant_begin()
    for sec in iter_subsecs(section, include_heading, n_chars_per_bullet, level):
        if sec["include_heading"]:
            s += f"\n{'#' * (sec['level'] + 1)} {sec['title']} ({sec['num_bullets']} bullet points)\n\n"
        for current_bullet in range(sec["num_bullets"]):
            s += f"- ({current_bullet+1}/{sec['num_bullets']})"
            s += sgl.gen(max_tokens=30, stop="\n")
            s += "\n"
    s += sgl.assistant_end()


def format_prompt(chunk: Section, level, tokenizer):
    """Only used for chunking to compute number of tokens of the prompt. n_bullets and n_words are not correctly set"""
    context = format_section(chunk, level)
    prompt = cfg.prompt_template.format(
        context=context, n_bullets=get_total_num_bullets(chunk, 1000), n_words=1000
    )
    prompt = tokenizer.apply_chat_template(
        [{"role": "user", "content": cfg.system_prompt + "\n\n" + prompt}],
        add_generation_prompt=True,
        tokenize=True,
    )
    return prompt


def chunk_patent(
    description: Section,
    tokenizer: PreTrainedTokenizerBase,
    max_length: int,
    gen_length: int = 2048,
):
    def insert_if_not_empty(old_chunks, insert_chunks, i):
        insert_chunks = [
            c for c in insert_chunks if c[0]["paragraphs"] or c[0]["subsections"] or c[3]
        ]
        chunks = [*old_chunks[:i], *insert_chunks, *old_chunks[i + 1 :]]
        return chunks

    chunks = [(description, 0, True, False)]

    while True:
        for i in range(len(chunks)):
            chunk: Section = chunks[i][0]  # type: ignore
            level: int = chunks[i][1]  # type: ignore
            include_heading: int = chunks[i][2]  # type: ignore

            prompt = format_prompt(chunk, level, tokenizer)
            if len(prompt) > max_length - gen_length:
                paras_only_chunk: Section = {
                    "title": chunk["title"],
                    "paragraphs": chunk["paragraphs"],
                    "subsections": [],
                }

                # If prompt length is exceeded with paragraphs alone:
                # Split into first_half_paragraphs, second_half_paragraphs, subsections
                if len(format_prompt(paras_only_chunk, level, tokenizer)) > max_length - gen_length:
                    # If a single paragraph exceeds the token limit
                    # split paragraph in the middle
                    if len(chunk["paragraphs"]) == 1:
                        para = chunk["paragraphs"][0]
                        sep = len(para) // 2
                        first_half = (
                            {
                                "title": chunk["title"],
                                "paragraphs": [para[:sep]],
                                "subsections": [],
                            },
                            level,
                            include_heading,
                            False,
                        )
                        second_half = (
                            {
                                "title": chunk["title"],
                                "paragraphs": [para[sep:]],
                                "subsections": [],
                            },
                            level,
                            False,
                            False,
                        )
                        chunks = insert_if_not_empty(chunks, [first_half, second_half], i)

                    # Otherwise, created separate chunks with half of the paragraphs each
                    else:
                        sep = len(chunk["paragraphs"]) // 2
                        first_half = (
                            {
                                "title": chunk["title"],
                                "paragraphs": chunk["paragraphs"][:sep],
                                "subsections": [],
                            },
                            level,
                            include_heading,
                            False,
                        )
                        second_half = (
                            {
                                "title": chunk["title"],
                                "paragraphs": chunk["paragraphs"][sep:],
                                "subsections": [],
                            },
                            level,
                            False,
                            False,
                        )
                        subsecs = (
                            {
                                "title": chunk["title"],
                                "paragraphs": [],
                                "subsections": chunk["subsections"],
                            },
                            level,
                            False,
                            False,
                        )
                        chunks = insert_if_not_empty(chunks, [first_half, second_half, subsecs], i)

                    break

                # If paragraphs alone do not exceed prompt length:
                # Keep adding subsections until we reach the limit
                else:
                    main_chunk = paras_only_chunk
                    remaining_subsecs = []

                    for j, subsec in enumerate(chunk["subsections"]):
                        main_chunk["subsections"].append(subsec)
                        if (
                            len(format_prompt(main_chunk, level, tokenizer))
                            > max_length - gen_length
                        ):
                            main_chunk["subsections"].pop(-1)
                            remaining_subsecs = chunk["subsections"][j:]
                            break

                    # If one subsection is too long alone, we need to make it a standalone chunk
                    # so that its paragraphs can be split above
                    subchunks = []
                    if not main_chunk["subsections"]:
                        # Super section (flagged to be added regardless if its empty by last True)
                        subchunks.append(
                            (
                                {
                                    "title": chunk["title"],
                                    "paragraphs": chunk["paragraphs"],
                                    "subsections": [],
                                },
                                level,
                                include_heading,
                                True,
                            )
                        )
                        # Separate subsection
                        subchunks.append((remaining_subsecs.pop(0), level + 1, True, False))
                    else:
                        # Super section + some subsections
                        subchunks.append((main_chunk, level, include_heading, False))

                    if len(remaining_subsecs) == 1:
                        subchunks.append((remaining_subsecs[0], level + 1, True, False))
                    else:
                        subchunks.append(
                            (
                                {
                                    "title": chunk["title"],
                                    "paragraphs": [],
                                    "subsections": remaining_subsecs,
                                },
                                level,
                                False,
                                False,
                            )
                        )

                    chunks = insert_if_not_empty(chunks, subchunks, i)

                    break

        # If we looped through all chunks without breaking, it means
        # all chunks fit the context length
        else:
            break

    # Drop last field as its not needed after chunking
    return [(c[0], c[1], c[2]) for c in chunks]


def words_per_bullet(summary):
    bullets = re.findall(r"\n-[^\n]+", summary)
    n_words = [len(bullet[2:].split(" ")) for bullet in bullets]
    return n_words


def init_metrics(n_patents: int, state_path: Path):
    if state_path.exists():
        return json.loads(state_path.read_text())

    metrics = {
        "total_time": 0,
        "total_patents": n_patents,
        "finished_patents": 0,
        "summaries_cached": 0,
        "summaries_failed": 0,
        "summaries_generated": 0,
        "llm_calls": 0,
        "words_per_bullet": [],
    }
    for n_chars_per_bullet in cfg.n_chars_per_bullet:
        if n_chars_per_bullet > 0:
            metrics[f"n_bullets_{n_chars_per_bullet}"] = []
    return metrics


def status_table(metrics) -> rich.table.Table:
    table = rich.table.Table(title="Patent Summarization Stats")
    for k in metrics:
        table.add_column(k)
    table.add_row(
        *[
            f"{v}"
            if isinstance(v, int)
            else f"{v:.2f}"
            if isinstance(v, float)
            else f"{(s := pd.Series(v, dtype=pd.Int64Dtype)).mean():.2f} ± {s.std():.2f}"
            for v in metrics.values()
        ]
    )
    return table


def verify_summary_structure(description: Section, summary: str):
    special_characters = [
        "\\",
        "*",
        "{",
        "}",
        ")",
        "]",
        "[",
        "|",
        "+",
        "(",
        "?",
        "^",
        "$",
        ".",
    ]
    empty_summary = get_empty_summary([description]).strip() + "\n\n"
    for c in special_characters:
        empty_summary = empty_summary.replace(c, f"\{c}")  # noqa
    regex = empty_summary.replace("\n\n", "\n\n(-[^\n]+\n)*\n*")
    assert bool(re.match(regex, summary.strip() + "\n\n")), "Summary structure verification failed!"


def main(cfg: Config) -> None:
    if cfg.debug:
        launch_debugger()

    rich.console.Console().print(rich.syntax.Syntax(cfg.to_yaml(), "yaml"))

    sample_dirs = [
        dir
        for dir in cfg.papers_dir.glob("*")
        if (
            dir.joinpath("paper.json").exists()
            and dir.joinpath("patent.json").exists()
            and dir.joinpath("match_meta.json").exists()
        )
    ]
    metrics = init_metrics(len(sample_dirs), cfg.state_path)
    sample_dirs = sample_dirs[metrics["finished_patents"] :]

    if sample_dirs:
        sgl.set_default_backend(sgl.RuntimeEndpoint(cfg.remote_url))
        # HF tokenizer is only used to chunk the patent
        tokenizer = AutoTokenizer.from_pretrained(cfg.model["model_path"])

    with rich.live.Live(status_table(metrics)) as table:
        for sample_dir in sample_dirs:
            patent_content_path: Path = sample_dir.joinpath("patent.json")

            # Load and chunk patent text
            patent_content = json.loads(patent_content_path.read_text())
            description = patent_content["sections"][0]
            chunks = chunk_patent(description, tokenizer, cfg.max_length)

            # Perform summarization multiple times with a varying level of detail
            for n_chars_per_bullet in cfg.n_chars_per_bullet:
                start_time = time.time()

                suffix = n_chars_per_bullet if n_chars_per_bullet > 0 else "empty"
                out_path = patent_content_path.parent.joinpath(f"patent_summary_{suffix}.md")

                if out_path.exists():
                    summary = out_path.read_text()
                    if n_chars_per_bullet > 0:
                        metrics["summaries_cached"] += 1
                    continue

                else:
                    # Generate summaries for all chunks in parallel
                    summaries = generate_summary.run_batch(
                        [
                            dict(
                                section=chunk,
                                section_formatted=format_section(chunk, level=level),
                                include_heading=include_heading,
                                n_chars_per_bullet=n_chars_per_bullet,
                                level=level,
                            )
                            for chunk, level, include_heading in chunks
                        ],
                        temperature=0,
                    )

                    try:
                        # Merge and postprocess summaries
                        summary = ""
                        for summary_state in summaries:
                            last_msg = summary_state.messages()[-1]
                            assert last_msg["role"] == "assistant"
                            summary += "\n" + last_msg["content"]
                        summary = summary.strip()
                        summary = re.sub(r"\n{2,}", "\n\n", summary)  # unify line spacing
                        summary = re.sub(
                            r"\n- \(\d+/\d+\)", "\n-", summary
                        )  # remove bullet numbering
                        summary = re.sub(
                            r"(#+ .*) \(\d+ bullet points\)", r"\1", summary
                        )  # remove number of bullets from section headings
                        for _ in range(
                            10
                        ):  # remove empty lines inside lists. Need to repeat if patterns overlap
                            summary = re.sub(r"\n(-.*)\n\n(-.*)\n", r"\n\1\n\2\n", summary)
                        out_path.write_text(summary)
                        if n_chars_per_bullet > 0:
                            metrics["summaries_generated"] += 1
                            metrics["llm_calls"] += len(chunks)
                    except:  # noqa
                        log.exception(f"Exception while postprocessing '{patent_content_path}'")
                        print("\n" * 10)

                try:
                    # Use empty summary to construct a regex that verifies the summary
                    verify_summary_structure(description, summary)

                    # Check number of bullets correct
                    total_bullets_target = sum(
                        get_total_num_bullets(chunk[0], n_chars_per_bullet) for chunk in chunks
                    )
                    total_bullets_gen = len(re.findall(r"\n-[^\n]+", summary))
                    assert (
                        total_bullets_target == total_bullets_gen
                    ), f"Model generated {total_bullets_gen}, expected {total_bullets_target}"

                    if n_chars_per_bullet > 0:
                        metrics[f"n_bullets_{n_chars_per_bullet}"].append(total_bullets_gen)
                        metrics["words_per_bullet"].extend(words_per_bullet(summary))

                except:  # noqa
                    log.exception(f"Exception while summarizing '{patent_content_path}'")
                    print("\n" * 10)

                metrics["total_time"] += time.time() - start_time
                table.update(status_table(metrics))

            metrics["finished_patents"] += 1
            table.update(status_table(metrics))
            cfg.state_path.write_text(json.dumps(metrics))


if __name__ == "__main__":
    cfg.apply()
    main(cfg)
