import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Type

from datasets.arrow_dataset import Dataset as HFDataset
from hydralette import Config, Field
from mpire.pool import WorkerPool
from pyrootutils import setup_root
from torch.utils.data import Dataset
from tqdm import tqdm
from transformers import AutoTokenizer, PreTrainedTokenizerBase

from src.dataset import paper_extractor
from src.dataset.chunk import PatentChunk, chunk_patent
from src.dataset.prompt import Prompt, outline_granularities
from src.utils.general import get_logger

root = setup_root(__file__)
log = get_logger(__file__)


data_cfg = Config(
    papers_dir=root.parent / "Pap2Pat" / "data",
    outline_suffix="long",  # one of ["long", "medium", "short"]
    paper_extractor=Field(
        type=paper_extractor.PaperExtractorBase,
        default=paper_extractor.AbstractOnly,
        convert=lambda s: getattr(paper_extractor, s),
    ),
    max_total_length=8192,  # prompt + response
    max_instruction_length=2048,
    max_paper_length=Field(
        reference=lambda data_cfg: int(
            (data_cfg.max_total_length - data_cfg.max_instruction_length) / 2
        ),
        type=int,
    ),
    # 0.7 to allow model to generate 30% longer texts
    max_patent_length=Field(
        reference=lambda data_cfg: int(
            0.7 * (data_cfg.max_total_length - data_cfg.max_instruction_length) / 2
        ),
        type=int
    ),
    add_claim=False,
)


@dataclass
class PatentDraftingSample:
    id: str
    paper_id: str
    patent_id: str
    paper_content: dict
    patent_content: dict
    patent_outline_suffix: str
    chunks: list[PatentChunk] = field(default_factory=list)

    @classmethod
    def from_path(
        cls: Type["PatentDraftingSample"], path: Path, patent_outline_suffix: str
    ) -> "PatentDraftingSample":
        paper_id, patent_id = path.name.split("-")
        patent_content = json.loads(path.joinpath("patent.json").read_text())
        paper_content = json.loads(path.joinpath("paper.json").read_text())

        sample = cls(
            id=path.name,
            paper_id=paper_id,
            patent_id=patent_id,
            paper_content=paper_content,
            patent_content=patent_content,
            patent_outline_suffix=patent_outline_suffix,
        )
        sample.select_outline(sample.patent_content["sections"])
        return sample

    def select_outline(self, sections: list[dict]) -> list[dict]:
        for section in sections:
            if self.patent_outline_suffix == "empty":
                section["outline"] = []
            else:
                section["outline"] = section[f"outline_{self.patent_outline_suffix}"]
            section["subsections"] = self.select_outline(section["subsections"])
        return sections

    @staticmethod
    def prompts_to_messages(prompts: dict, exclude_roles: list[str] = []) -> list[dict]:
        return [
            {"role": role, "content": prompts[role]}
            for role in ("system", "user", "assistant")
            if role not in exclude_roles
        ]

    def prepare_prompt(
        self, tokenizer: PreTrainedTokenizerBase, max_prompt_length: int, add_claim: bool
    ) -> list[Prompt]:
        assert self.chunks, "Need to chunk before creating the prompts"
        n_chars = outline_granularities.get(self.patent_outline_suffix) or outline_granularities.get("long")
        assert n_chars is not None
        n_paragraphs = max(
            1, n_chars // 590
        )  # 590 = average number of characters per paragraph in the dataset
        n_words = max(1, n_chars // 7)  # 7 = average number of characters per word in the dataset

        for chunk in self.chunks:
            chunk.prompt.prepare_system_prompt(tokenizer, n_paragraphs, n_words)
            assert chunk.prompt.n_system_tokens is not None
            chunk.prompt.prepare_user_prompt(
                tokenizer=tokenizer,
                sample=self,
                chunk=chunk,
                max_tokens=max_prompt_length - chunk.prompt.n_system_tokens,
                add_claim=add_claim,
            )
            chunk.prompt.prepare_assistant_response(tokenizer, chunk)

        return [chunk.prompt for chunk in self.chunks]


class PatentDraftingDataset(Dataset):
    def __init__(
        self,
        data_dir: Path,
        outline_suffix: str,
        paper_extractor: Type[paper_extractor.PaperExtractorBase],
        do_chunk: bool = False,
        tokenizer: PreTrainedTokenizerBase | None = None,
        max_total_length: int | None = None,
        max_instruction_length: int | None = None,
        max_paper_length: int | None = None,
        max_patent_length: int | None = None,
        n_threads: int = 4,
        exclude_splits: list[str] | None = None,
        add_claim: bool = False,
    ):
        self.data_dir = data_dir
        self.outline_suffix = outline_suffix
        self.paper_extractor = paper_extractor
        self.tokenizer = tokenizer

        self.do_chunk = do_chunk
        self.add_claim = add_claim
        self.max_total_length = max_total_length
        self.max_instruction_length = max_instruction_length
        self.max_paper_length = max_paper_length
        self.max_patent_length = max_patent_length

        self.exclude_splits = exclude_splits if exclude_splits is not None else []
        self.metadata = json.loads(data_dir.joinpath("metadata.json").read_text())
        self.samples: list[PatentDraftingSample] = []
        self.splits: dict[str, list[PatentDraftingSample]] = {}

        for split, sample_ids in self.metadata["splits"].items():
            if split in self.exclude_splits:
                continue

            self.splits[split] = []
            for sample_id in tqdm(sample_ids, desc=f"Loading {split} samples"):
                sample_dir = data_dir.joinpath(sample_id)
                sample = PatentDraftingSample.from_path(sample_dir, outline_suffix)
                self.samples.append(sample)
                self.splits[split].append(sample)

        if do_chunk:
            assert tokenizer is not None, "tokenizer is required for chunking"
            assert max_total_length is not None, "max_total_length is required for chunking"
            assert (
                max_instruction_length is not None
            ), "max_instruction_length is required for chunking"
            assert max_paper_length is not None, "max_paper_length is required for chunking"
            assert max_patent_length is not None, "max_patent_length is required for chunking"

            # CHUNK PATENTS
            chars_per_token = get_characters_per_token(tokenizer, data_dir)
            max_chunk_length = int(max_patent_length * chars_per_token)
            for sample in tqdm(self.samples, desc="Chunking Patents"):
                description = sample.patent_content["sections"][0]
                sample.chunks = chunk_patent(description, max_chunk_length=max_chunk_length)

            # EXTRACT PAPER CONTEXT FOR EACH CHUNK
            # parallelization is handled inside to allow different approaches for different retrievers
            pe = paper_extractor(self, tokenizer, max_paper_length)  # type: ignore
            pe.extract_context()

            # ASSEMBLE PROMPTS
            with WorkerPool(n_jobs=n_threads, use_dill=True, use_worker_state=True) as pool:

                def init_tokenizer(worker_state):
                    worker_state["tokenizer"] = AutoTokenizer.from_pretrained(
                        tokenizer.name_or_path
                    )

                def prepare_prompt_fn(worker_state: dict, sample: PatentDraftingSample):
                    return sample.prepare_prompt(
                        tokenizer=worker_state["tokenizer"],
                        max_prompt_length=max_instruction_length + max_paper_length,
                        add_claim=self.add_claim,
                    )

                for sample, prompts in tqdm(
                    zip(
                        self.samples,
                        pool.imap(prepare_prompt_fn, self.samples, worker_init=init_tokenizer),
                    ),
                    desc="Assembling Prompts",
                    total=len(self.samples),
                ):
                    for current_chunk, prompt in zip(sample.chunks, prompts):
                        current_chunk.prompt = prompt

    def to_huggingface_dataset(self) -> dict[str, HFDataset]:
        return {
            split: HFDataset.from_dict(
                dict(
                    messages=[
                        chunk.prompt.messages()
                        for sample in samples
                        for chunk in sample.chunks
                        if chunk.prompt.n_assistant_tokens > 1000  # type: ignore
                    ]
                )
            )
            for split, samples in self.splits.items()
        }


def get_characters_per_token(tokenizer: PreTrainedTokenizerBase, pap2pat_dir: Path) -> float:
    def get_sample_documents(n):
        n_ = 0
        for sample_dir in pap2pat_dir.glob("*"):
            paper = sample_dir.joinpath("paper.md").read_text()
            patent = sample_dir.joinpath("patent.md").read_text()
            yield paper
            yield patent
            n_ += 2
            if n_ >= n:
                break

    documents = list(get_sample_documents(n=50))
    text = "\n\n".join(documents)

    n_tokens = len(tokenizer.encode(text))
    n_chars = len(text)
    return n_chars / n_tokens
