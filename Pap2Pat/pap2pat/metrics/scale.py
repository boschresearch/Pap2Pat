import logging
import random
import re
from pathlib import Path

import bm25s
import pysbd
import scale_score.utils
import torch
from mpire.pool import WorkerPool
from pyrootutils import setup_root
from transformers import T5ForConditionalGeneration, T5Tokenizer
from tqdm import tqdm

from pap2pat.metrics.stylometrix import identity_iterator

root = setup_root(__file__)
seg = pysbd.Segmenter(language="en", clean=False)
logging.getLogger("bm25s").setLevel(logging.INFO)


def filter_chunks_decorator(orig_get_chunks, k=5):
    def clean_chunk(chunk: str) -> str:
        return (
            next(re.finditer(r'(.*)Question: Does this imply that ".*"\? Yes or No\?', chunk))
            .group(1)
            .strip()
        )

    def clean_query(query: str) -> str:
        return (
            next(
                re.finditer(
                    r'\{\{premise\}\} Question: Does this imply that "(.*)"\? Yes or No\?', query
                )
            )
            .group(1)
            .strip()
        )

    def get_chunks(
        tokenizer: T5Tokenizer,
        joined_convo: str,
        prompt: str,
        chunk_size: int | None = None,
        window_size: float = 0.25,
    ) -> list[torch.Tensor]:
        chunks = orig_get_chunks(tokenizer, joined_convo, prompt, chunk_size, window_size)
        chunks_str = [clean_chunk(tokenizer.decode(c[0])) for c in chunks]
        query_sentence = clean_query(prompt)

        bm25 = bm25s.BM25()
        chunks_tokens = bm25s.tokenize(chunks_str, stopwords="en", show_progress=False)
        assert chunks_str and chunks_tokens
        bm25.index(chunks_tokens, show_progress=False)
        queries_tokens = bm25s.tokenize(query_sentence, stopwords="en", show_progress=False)  # type: ignore
        ranked_indices, _ = bm25.retrieve(
            queries_tokens, k=min(len(chunks_str), k), show_progress=False
        )  # type: ignore
        chunks_filtered = [chunks[i] for i in ranked_indices[0]]
        return chunks_filtered

    return get_chunks


def get_flan_T5_model_without_device_map(
    size: str, model_path: str | None = None
) -> tuple[T5ForConditionalGeneration, T5Tokenizer]:
    tokenizer = T5Tokenizer.from_pretrained(f"google/flan-t5-{size}")
    model: T5ForConditionalGeneration = T5ForConditionalGeneration.from_pretrained(
        f"google/flan-t5-{size}"
    )  # type: ignore
    if model_path is not None:
        model.load_state_dict(torch.load(model_path))
    return model, tokenizer


scale_score.utils.tqdm = identity_iterator
scale_score.utils.get_chunks = filter_chunks_decorator(scale_score.utils.get_chunks, k=5)
scale_score.utils.get_flan_T5_model = get_flan_T5_model_without_device_map

from scale_score.scorer import SCALEScorer  # noqa


def init(worker_id: int, worker_state: dict):
    device = f"cuda:{worker_id}"
    scorer = SCALEScorer(size="large", device=device)
    scorer.model.to(device)  # type: ignore
    worker_state["scorer"] = scorer


def score_patent(
    worker_id: int,
    worker_state: dict,
    generated: str,
    reference: str,
    paper: str,
    k: int = 10,
    **kwargs,
) -> dict[str, dict[str, float]]:
    def get_sents(text):
        return [
            sent.strip()
            for sent in seg.segment(text)
            if (
                len(sent.strip()) > 50
                and len(sent.strip()) < 500
                and len(sent.split()) > 5
                and not re.match(r"^#+\s+.*$", sent.strip())
                and not re.match(r"^\*\*.*\*\*", sent.strip())
            )
        ]

    scorer: SCALEScorer = worker_state["scorer"]
    gen_sents = get_sents(generated)
    gen_sents_sample = random.sample(gen_sents, k=k) if len(gen_sents) > k else gen_sents

    ref_sents = get_sents(reference)
    ref_sents_sample = random.sample(ref_sents, k=k) if len(ref_sents) > k else ref_sents

    all_scores = {}
    for score_name, premise, hypothesis in (
        ("faithfulness", paper, gen_sents_sample),
        ("factuality", reference, gen_sents_sample),
        ("factuality_both", reference + "\n\n" + paper, gen_sents_sample),
        ("coverage", generated, ref_sents_sample),
    ):
        scores = scorer.score([premise], [hypothesis], chunk_size=512)
        all_scores[score_name] = sum(scores) / len(scores) if scores else 0
    return {"factuality": all_scores}


def imap(f, kwargs):
    for kwarg in kwargs:
        yield f(**kwarg)


def load_samples(run_dir: Path, split: str):
    for sample_dir in run_dir.glob(f"predictions/{split}/*"):
        gen = sample_dir.joinpath("generated.md").read_text()
        ref = sample_dir.joinpath("reference.md").read_text()
        yield (sample_dir.name, gen, ref)


if __name__ == "__main__":
    data_dir = root / "data"
    sample_run_dirs = [
        root.parent.parent
        / "ppp-modelling/outputs/runs/FT-Meta-Llama-3-8B-Instruct-BM25-outline-1000-filter+hyp/",
        root.parent
        / "Outline_Guided_Generation/outputs/runs/Meta-Llama-3-8B-Instruct-BM25-outline-medium",
        root.parent
        / "Outline_Guided_Generation/outputs/runs/Qwen2-72B-Instruct-BM25-outline-medium",
    ]
    data_dir = root / "data"

    for run_dir in sample_run_dirs:
        scores = {}

        args = [
            {"sample": i, "generated": gen, "reference": ref}
            for i, gen, ref in load_samples(run_dir, "test")
        ]
        with WorkerPool(
            torch.cuda.device_count(),
            use_worker_state=True,
            use_dill=True,
            pass_worker_id=True,
            start_method="spawn",
        ) as pool:
            for arg, score in tqdm(
                zip(args, pool.imap(score_patent, args, worker_init=init)), total=len(args)
            ):
                scores[arg["sample"]] = score

        avg_score = sum(scores.values()) / len(scores)
        print(run_dir.name, avg_score)
