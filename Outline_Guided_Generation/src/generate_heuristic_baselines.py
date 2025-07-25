from typing import Iterable
import bm25s
import json
from pyrootutils import setup_root

from src.utils.general import get_logger

root = setup_root(__file__)
dataset_path = root.parent / "Pap2Pat" / "data"
log = get_logger(__name__)

DATASET = dict[str, list[dict[str, str]]]


def load_dataset() -> DATASET:
    metadata = json.loads(dataset_path.joinpath("metadata.json").read_text())
    return {
        split: [
            {
                "id": sample_id,
                "paper": dataset_path.joinpath(sample_id).joinpath("paper.md").read_text(),
                "patent": dataset_path.joinpath(sample_id).joinpath("patent.md").read_text(),
                **{
                    outline_path.stem: outline_path.read_text()
                    for outline_path in dataset_path.joinpath(sample_id).glob("patent_outline_*.md")
                }
            }
            for sample_id in metadata["splits"][split]
        ]
        for split in metadata["splits"]
    }


def create_retrieval_baseline_dir(
    dataset: DATASET, splits: Iterable[str] = ("test", "val", "non-contaminated-test")
) -> None:
    dir = root / "outputs" / "runs" / "retrieval-baseline"
    if dir.exists():
        log.error(f"Directory '{dir}' exists. Aborting ...")
        return

    all_scores = []
    all_lengths = []
    best_scores = []
    best_lengths = []
    log.info("Creating index from train patents")
    train_patents = [i["patent"] for i in dataset["train"]]
    retriever = bm25s.BM25()
    corpus_tokens = bm25s.tokenize(train_patents, stopwords="en")
    retriever.index(corpus_tokens)
    for split in splits:
        log.info(f"{split}: Retrieving closest matches")
        queries_tokens = bm25s.tokenize([i["paper"] for i in dataset[split]], stopwords="en")  # type: ignore
        results, scores = retriever.retrieve(queries_tokens, k=len(train_patents))  # type: ignore
        for result_list, score_list in zip(results, scores):
            for i, (score, patent_index) in enumerate(zip(score_list, result_list)):
                if i == 0:
                    best_scores.append(score)
                    best_lengths.append(len(train_patents[patent_index]))
                all_scores.append(score)
                all_lengths.append(len(train_patents[patent_index]))

    from matplotlib import pyplot as plt

    plt.clf()
    plt.scatter(all_lengths, all_scores, alpha=0.1)
    plt.scatter(best_lengths, best_scores, color="red", alpha=0.1)
    plt.savefig("BM25_bias.png")

    for split in splits:
        log.info(f"{split}: Retrieving closest matches")
        queries_tokens = bm25s.tokenize([i["paper"] for i in dataset[split]], stopwords="en")  # type: ignore
        results, _ = retriever.retrieve(queries_tokens, k=1)  # type: ignore

        pred_dir = dir / "predictions" / split
        for sample, result in zip(dataset[split], results):
            retrieved = train_patents[result[0]]
            sample_dir = pred_dir / sample["id"]
            sample_dir.mkdir(parents=True)
            sample_dir.joinpath("generated.md").write_text(retrieved)


def create_paper_baseline_dir(
    dataset: DATASET, splits: Iterable[str] = ("test", "val", "non-contaminated-test")
) -> None:
    dir = root / "outputs" / "runs" / "paper-baseline"
    if dir.exists():
        log.error(f"Directory '{dir}' exists. Aborting ...")
        return

    for split in splits:
        pred_dir = dir / "predictions" / split
        for sample in dataset[split]:
            sample_dir = pred_dir / sample["id"]
            sample_dir.mkdir(parents=True)
            sample_dir.joinpath("generated.md").write_text(sample["paper"])


def create_ground_truth_dir(
    dataset: DATASET, splits: Iterable[str] = ("test", "val", "non-contaminated-test")
) -> None:
    dir = root / "outputs" / "runs" / "ground-truth"
    if dir.exists():
        log.error(f"Directory '{dir}' exists. Aborting ...")
        return

    for split in splits:
        pred_dir = dir / "predictions" / split
        for sample in dataset[split]:
            sample_dir = pred_dir / sample["id"]
            sample_dir.mkdir(parents=True)
            sample_dir.joinpath("generated.md").write_text(sample["patent"])


def create_outline_dir(
    dataset: DATASET, splits: Iterable[str] = ("test", "val", "non-contaminated-test"), outline_suffix: str = "long"
) -> None:
    dir = root / "outputs" / "runs" / f"outline-{outline_suffix}"
    if dir.exists():
        log.error(f"Directory '{dir}' exists. Aborting ...")
        return

    for split in splits:
        pred_dir = dir / "predictions" / split
        for sample in dataset[split]:
            sample_dir = pred_dir / sample["id"]
            sample_dir.mkdir(parents=True)
            sample_dir.joinpath("generated.md").write_text(sample[f"patent_outline_{outline_suffix}"])


if __name__ == "__main__":
    log.info("Loading dataset")
    dataset = load_dataset()

    log.info("Creating retrieval baseline")
    create_retrieval_baseline_dir(dataset)

    log.info("Creating paper baseline")
    create_paper_baseline_dir(dataset)

    log.info("Creating outline baseline")
    create_outline_dir(dataset)

    log.info("Creating ground truth")
    create_ground_truth_dir(dataset)
    