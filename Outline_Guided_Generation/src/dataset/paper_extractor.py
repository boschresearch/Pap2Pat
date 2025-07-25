import re
from abc import ABC, abstractmethod
from functools import partial
from typing import TYPE_CHECKING

import bm25s
from mpire.pool import WorkerPool
from tqdm import tqdm
from transformers import AutoTokenizer, PreTrainedTokenizerBase

from src.dataset.prompt import format_outline_md, format_reference_patent
from src.utils.general import get_logger

if TYPE_CHECKING:
    from src.dataset.dataset import PatentDraftingDataset, PatentDraftingSample

log = get_logger(__file__)

TEMPLATE = "Here are the most relevant parts of the research paper describing the invention:\n\n```md\n{paper_context}\n```\n\n"


def get_all_paragraphs(sections):
    for section in sections:
        for paragraph in section["paragraphs"]:
            if len(paragraph) > 50:
                yield paragraph
        yield from get_all_paragraphs(section["subsections"])


def flatten_secs(sections: list[dict], level=1):
    for sec in sections:
        yield sec, level
        yield from flatten_secs(sec["subsections"], level + 1)


def format_paper_blueprint(sections: list[dict]) -> str:
    i = 0
    s = ""
    for section, level in flatten_secs(sections):
        s += f"\n{'#' * level} {section['title']}\n\n"
        for paragraph in section["paragraphs"]:
            s += f"<paragraph-{i}>\n\n"
            i += 1
    return s


class PaperExtractorBase(ABC):
    def __init__(
        self,
        ds: "PatentDraftingDataset",
        tokenizer: PreTrainedTokenizerBase,
        max_tokens: int,
    ):
        self.ds = ds
        self.tokenizer = tokenizer
        self.max_tokens = max_tokens

    @abstractmethod
    def extract_context(self) -> None:
        """Extract context from the paper, then call chunk.prompt.set_paper_context"""

    @staticmethod
    def format_paper_from_ranked_indices(
        tokenizer: PreTrainedTokenizerBase,
        ranked_indices: list[int],
        paper: dict,
        all_paragraphs: list[str],
        max_tokens: int,
    ) -> str:
        def current_length(s: str) -> int:
            s = re.sub(r"(<paragraph-\d+>\n\n)+", "<paragraph-0>\n\n", s)
            s = re.sub(r"<paragraph-0>", "...", s)
            return len(tokenizer.encode(s))

        s = f"# Abstract\n\n{paper['abstract']}\n\n"
        s += format_paper_blueprint(paper["sections"])

        # iteratively add new paragraphs to the context until token limit is reached or whole paper is added
        while len(ranked_indices) > 0:
            next_best_index = ranked_indices.pop(0)
            pattern = rf"<paragraph-{next_best_index}>"
            assert pattern in s
            new_s = re.sub(pattern, all_paragraphs[next_best_index].replace("\\", "\\\\"), s)

            n_tokens = current_length(new_s)
            if n_tokens <= max_tokens:
                s = new_s
            else:
                break

        n_tokens = current_length(s)
        if n_tokens > max_tokens:
            log.error(
                f"Error in retrieving from paper {paper['id']}. Got {n_tokens} tokens with {max_tokens=}"
            )

        # remove placeholders and add "..."
        s = re.sub(r"(<paragraph-\d+>\n\n)+", "<paragraph-0>\n\n", s)
        s = re.sub(r"<paragraph-0>", "...", s)

        return s


class AbstractOnly(PaperExtractorBase):
    def extract_context(self) -> None:
        for sample in tqdm(self.ds.samples, desc="Retrieving context"):
            for chunk in sample.chunks:
                chunk.prompt.paper_context = TEMPLATE.format(
                    paper_context=f"# Abstract:\n\n{sample.paper_content['abstract']}"
                )


class NoPaper(PaperExtractorBase):
    def extract_context(self) -> None:
        for sample in tqdm(self.ds.samples, desc="Retrieving context"):
            for chunk in sample.chunks:
                chunk.prompt.paper_context = ""


class BM25Base(PaperExtractorBase):
    @abstractmethod
    def get_queries(self, sample: "PatentDraftingSample") -> list[str]: ...

    @staticmethod
    def init_worker_process(worker_state, tokenizer_name: str):
        """Need to load tokenizer separately on each worker process to avoid deadlocks"""
        worker_state["tokenizer"] = AutoTokenizer.from_pretrained(tokenizer_name)
        worker_state["n_template_tokens"] = len(worker_state["tokenizer"].encode(TEMPLATE))

    @staticmethod
    def get_ranked_indices(queries: list[str], all_paragraphs: list[str]) -> list[list[int]]:
        corpus_tokens = bm25s.tokenize(all_paragraphs, stopwords="en", show_progress=False)
        retriever = bm25s.BM25()
        retriever.index(corpus_tokens, show_progress=False)
        queries_tokens = bm25s.tokenize(queries, stopwords="en", show_progress=False)  # type: ignore
        results, _ = retriever.retrieve(queries_tokens, k=len(all_paragraphs), show_progress=False)  # type: ignore
        return results.tolist()

    @staticmethod
    def retrieve_and_format(
        worker_state, paper: dict, queries: list[str], max_tokens: int
    ) -> list[str]:
        all_paragraphs = list(get_all_paragraphs(paper["sections"]))
        ranked_indices = (
            BM25Base.get_ranked_indices(queries, all_paragraphs)
            if all_paragraphs
            else [[] for _ in range(len(queries))]
        )
        contexts_formatted = [
            PaperExtractorBase.format_paper_from_ranked_indices(
                worker_state["tokenizer"],
                ranked_indices_,
                paper,
                all_paragraphs,
                max_tokens - worker_state["n_template_tokens"],
            )
            for ranked_indices_ in ranked_indices
        ]
        return contexts_formatted

    def extract_context(self) -> None:
        args = [
            (sample.paper_content, self.get_queries(sample), self.max_tokens)
            for sample in self.ds.samples
        ]

        with WorkerPool(n_jobs=4, use_dill=True, use_worker_state=True) as p:
            for sample, contexts_formatted in tqdm(
                zip(
                    self.ds.samples,
                    p.imap(
                        self.retrieve_and_format,
                        args,
                        worker_init=partial(
                            self.init_worker_process, tokenizer_name=self.tokenizer.name_or_path
                        ),
                    ),
                ),
                desc="Retrieving context with BM25",
                total=len(self.ds.samples),
            ):
                assert len(sample.chunks) == len(contexts_formatted)
                for chunk, context_formatted in zip(sample.chunks, contexts_formatted):
                    chunk.prompt.paper_context = TEMPLATE.format(paper_context=context_formatted)


class BM25(BM25Base):
    def get_queries(self, sample: "PatentDraftingSample"):
        return [format_outline_md([chunk]) for chunk in sample.chunks]


class BM25Oracle(BM25Base):
    def get_queries(self, sample: "PatentDraftingSample"):
        return [format_reference_patent([chunk.content]) for chunk in sample.chunks]
