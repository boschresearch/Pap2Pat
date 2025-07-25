import pickle
import re
from typing import Iterable

import matplotlib.pyplot as plt
import spacy.tokens
import stylo_metrix as sm
from mpire.pool import WorkerPool
from pyrootutils import setup_root
from tqdm import tqdm

from pap2pat.metrics.language import load_dataset_files, load_gen_files, profile_similarity

root = setup_root(__file__)
pkl_path = root / "pap2pat" / "metrics" / "stylometrix_features.pkl"


# disable stylometrix progress bars
def identity_iterator(it, *args, **kwargs):
    for i in it:
        yield i


sm.stylo_metrix.tqdm = identity_iterator


def compute_metrics(worker_state: dict, doc: str) -> tuple[list[dict], list[int]]:
    stylo: sm.StyloMetrix = worker_state["stylo"]
    chunks = [
        chunk.strip()
        for chunk in doc.split("\n\n")
        if (
            len(chunk.strip()) > 50
            and len(chunk.strip())
            < 5_000  # paragraphs longer than that make stylometrix crash and only happen for infinite repetitions
            and len(chunk.split()) > 5
            and not re.match(r"^#+\s+.*$", chunk.strip())
            and not re.match(r"^\*\*.*\*\*", chunk.strip())
        )
    ]
    metrics = []
    chunk_lengths = []
    for chunk in chunks:
        chunk_metrics = stylo.transform(chunk).iloc[0].to_dict()  # type: ignore
        del chunk_metrics["text"]
        metrics.append(chunk_metrics)
        chunk_lengths.append(len(chunk.split()))
    return metrics, chunk_lengths


def init(worker_state: dict):
    nlp = spacy.load("en_core_web_lg")
    nlp.max_length = 3_000_000
    worker_state["stylo"] = sm.StyloMetrix("en", nlp=nlp)


def imap(f, args, worker_init):
    state = {}
    worker_init(state)
    for arg in args:
        yield f(**arg, worker_state=state)


def get_stylometrics_features(docs: Iterable[str], n_processes: int) -> dict[str, float]:
    docs = list(tqdm(docs, desc="loading gen files"))
    args = [{"doc": doc} for doc in docs]
    total_features = {
        metric.code: 0
        for metric in list(sm.get_all_metrics("en"))  # type: ignore
    }
    total_words = 0

    with WorkerPool(12, use_worker_state=True, use_dill=True) as pool:
        for metric_dicts, n_words_list in tqdm(
            pool.imap(
                compute_metrics,
                args,
                worker_init=init,
            ),
            total=len(args),
        ):
            for metrics, n_words in zip(metric_dicts, n_words_list):
                total_words += n_words
                for metric, value in metrics.items():
                    total_features[metric] += value * n_words

    # for metric_dicts, n_words_list in tqdm(
    #     imap(
    #         compute_metrics,
    #         args,
    #         worker_init=init,
    #     ),
    #     total=len(args),
    # ):
    #     for metrics, n_words in zip(metric_dicts, n_words_list):
    #         total_words += n_words
    #         for metric, value in metrics.items():
    #             total_features[metric] += value * n_words

    features = {metric: value / total_words for metric, value in total_features.items()}
    return features


def plot_feature_differences(
    patent_features,
    paper_features,
    save_path=root.parent / "Outline_Guided_Generation" / "outputs" / "plots" / "stylometrix.png",
):
    patent_paper_differences = dict(
        sorted(
            [
                (
                    feat,
                    (pat_val - paper_features[feat]) / max(1e-10, pat_val + paper_features[feat]),
                )
                for feat, pat_val in patent_features.items()
            ],
            key=lambda x: x[1],
        )
    )
    patent_paper_differences_significant = {
        k: v for k, v in patent_paper_differences.items() if abs(v) > 0.1
    }

    fig, ax = plt.subplots()
    fig.set_size_inches(5, 15)
    ax.hlines(
        [feat for feat in patent_paper_differences_significant],
        [value if value < 0 else 0 for value in patent_paper_differences_significant.values()],
        [value if value > 0 else 0 for value in patent_paper_differences_significant.values()],
        color=[
            "blue" if value > 0 else "red"
            for value in patent_paper_differences_significant.values()
        ],
        alpha=0.4,
        linewidth=5,
    )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", which="both", left=False, right=False, labelleft=True, labelsize=6)
    fig.tight_layout()
    if not save_path.parent.exists():
        save_path.parent.mkdir(parents=True)
    fig.savefig("stylometrix.png", dpi=800)


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

    if not pkl_path.exists():
        patent_features = get_stylometrics_features(
            load_dataset_files(data_dir, "train", "patent.md"), 12
        )
        paper_features = get_stylometrics_features(
            load_dataset_files(data_dir, "train", "paper.md"), 12
        )
        with pkl_path.open("wb") as fp:
            pickle.dump({"patent": patent_features, "paper": paper_features}, fp)

    else:
        with pkl_path.open("rb") as fp:
            pkl = pickle.load(fp)
            patent_features = pkl["patent"]
            paper_features = pkl["paper"]

    plot_feature_differences(patent_features, paper_features)

    results = []
    for run_dir in sample_run_dirs:
        model_features = get_stylometrics_features(load_gen_files(run_dir, "test"), 12)

        pat_sim = profile_similarity(
            {"stylometrix": model_features},  # type: ignore
            {"stylometrix": patent_features},  # type: ignore
        )["stylometrix"]
        pap_sim = profile_similarity(
            {"stylometrix": model_features},  # type: ignore
            {"stylometrix": paper_features},  # type: ignore
        )["stylometrix"]
        pat_pap_sim = profile_similarity(
            {"stylometrix": paper_features},  # type: ignore
            {"stylometrix": patent_features},  # type: ignore
        )["stylometrix"]
        results.append(
            {
                "model": run_dir.name[:10],
                "patent": pat_sim,
                "paper": pap_sim,
                "patent_paper": pat_pap_sim,
                "score": (pat_sim - pap_sim + 1) / 2,
            }
        )

    print(results)
