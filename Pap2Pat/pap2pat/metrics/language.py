import json
from typing import Iterable
import nltk
from pathlib import Path
from tqdm import tqdm
import string
from pyrootutils import setup_root
from collections import defaultdict
from mpire.pool import WorkerPool

root = setup_root(__file__)
pkl_path = root / "pap2pat" / "metrics" / "ngram_features.pkl"

N_GRAM_COUNTS = dict[tuple[str, ...], int]
N_GRAM_COUNTS_PER_N = dict[int, N_GRAM_COUNTS]
N_GRAM_PROFILE = dict[tuple[str, ...], float]
N_GRAM_PROFILE_PER_N = dict[int, N_GRAM_PROFILE]


def load_gen_files(run_dir: Path, split: str):
    for f in run_dir.glob(f"predictions/{split}/*/generated.md"):
        yield f.read_text()


def load_dataset_files(data_dir: Path, split: str, filename: str, metadata: dict = None):
    if metadata is None:
        metadata = json.loads(data_dir.joinpath("metadata.json").read_text())
    for sample_id in metadata["splits"][split]:
        sample_id: str
        file = data_dir / sample_id / filename
        yield file.read_text()


def get_n_grams(doc: str, n: list[int]) -> N_GRAM_COUNTS:
    counts = defaultdict(int)
    tokens = [
        t.lower()
        for t in nltk.tokenize.word_tokenize(doc)
        if any(c not in string.punctuation for c in t.strip())
    ]
    for n_ in n:
        for n_gram in nltk.ngrams(tokens, n_):
            counts[n_gram] += 1
    return dict(counts)


def get_n_gram_counts(docs: Iterable[str], n: list[int], n_processes: int) -> N_GRAM_COUNTS_PER_N:
    counts = {n_: defaultdict(int) for n_ in n}
    docs = list(tqdm(docs, desc="Loading files"))
    args = [{"doc": doc, "n": list(n)} for doc in docs]
    with WorkerPool(n_processes) as pool:
        for counts_ in tqdm(
            pool.imap(get_n_grams, args, chunk_size=16), desc="Extracting n-grams", total=len(args)
        ):
            for ngram, c in counts_.items():
                counts[len(ngram)][ngram] += c
    counts = {n_: dict(counts_) for n_, counts_ in counts.items()}
    return counts


def get_top_k_per_n_and_normalize(counts: N_GRAM_COUNTS_PER_N, k: int) -> N_GRAM_PROFILE_PER_N:
    top_k = {
        n_: dict(list(sorted(counts_.items(), key=lambda x: x[1], reverse=True))[:k])
        for n_, counts_ in counts.items()
    }
    total_ngrams = {n_: total_num_ngrams(counts_) for n_, counts_ in top_k.items()}
    top_k_normalized = {
        n_: {ngram: count / total_ngrams[n_] for ngram, count in counts_.items()}
        for n_, counts_ in top_k.items()
    }
    return top_k_normalized


def total_num_ngrams(counts: N_GRAM_COUNTS) -> int:
    return sum(counts.values())


def profile_similarity(
    model_profile: N_GRAM_PROFILE_PER_N, reference_profile: N_GRAM_PROFILE_PER_N
) -> dict[str, float]:
    n_gram_scores = {
        str(n): [
            1
            - (
                (p_ref - model_profile[n].get(ngram, 0))
                / max(1e-10, p_ref + model_profile[n].get(ngram, 0))
            )
            ** 2
            for ngram, p_ref in profile.items()
        ]
        for n, profile in reference_profile.items()
    }
    return {n: sum(scores) / len(scores) for n, scores in n_gram_scores.items()}


def add_avg(d):
    return {"avg": sum(d.values()) / len(d), **d}
