import json
import logging
from pathlib import Path
from typing import Literal

import pap2pat
import rich.syntax
from hydralette import Config, Field
from pyrootutils import setup_root
from tqdm import tqdm

from src.utils.general import get_logger, launch_debugger

root = setup_root(__file__)
log = get_logger(__file__)
logging.basicConfig(level=logging.INFO)
rich_console = rich.console.Console()

ALL_METRICS_KEYS = (
    "bertscore",
    "bleu",
    "rouge",
    "rr",
    "tokens",
    "repetitions",
    "language",
    "factuality",
    "coherence",
    "chunk_stats"
)

ALL_METRICS = (
    "BERTScore",
    "bleu",
    "rouge",
    "rr",
    "tokens",
    "repetitions",
    "clustered_BERTScore",
    "clustered_bleu",
    "clustered_rouge",
    "clustered_tokens",
    "language",
    "factuality",
    "coherence",
    "chunk_stats"
)

cfg = Config(
    run_dir=Field(type=Path),
    debug=False,
    scores=Field(
        default=ALL_METRICS_KEYS,
        convert=lambda s: s.split(","),
    ),
    splits=Field(default=["val", "test", "non-contaminated-test"], convert=lambda s: s.split(",")),
    metrics_filename="metrics.json"
)


def main(cfg: Config) -> None:
    if cfg.debug:
        launch_debugger()

    rich_console.print(rich.syntax.Syntax(cfg.to_yaml(), "yaml"))

    aggregate_metrics = {}

    run_dir: Path = cfg.run_dir
    splits: Literal["train", "val", "test", "non-contaminated-test"] = cfg.splits
    for split in splits:
        log.info(f"Evaluating {split} split")
        generated = {
            pred_dir.name: pred_dir.joinpath("generated.md").read_text()
            for pred_dir in tqdm(
                list(run_dir.glob(f"predictions/{split}/*")), desc="Loading pred files"
            )
        }
        predictions = pap2pat.Predictions(generated, split)  # type: ignore

        if "tokens" in cfg.scores:
            predictions.compute_tokens()

        if "bleu" in cfg.scores:
            predictions.compute_bleu()

        if "rouge" in cfg.scores:
            predictions.compute_rouge()

        if "bertscore" in cfg.scores:
            predictions.compute_bertscore()

        if "rr" in cfg.scores:
            predictions.compute_rr()

        if "repetitions" in cfg.scores:
            predictions.compute_repetitions()

        if "language" in cfg.scores:
            predictions.compute_language()

        if "factuality" in cfg.scores:
            predictions.compute_factuality()
        
        if "coherence" in cfg.scores:
            predictions.compute_coherence()

        if "chunk_stats" in cfg.scores:
            predictions.compute_chunk_stats(run_dir)

        for sample_id in predictions.preds.keys():
            metrics = predictions.metrics_per_sample.get(sample_id, {})

            metrics_path = run_dir / "predictions" / split / sample_id / cfg.metrics_filename
            if metrics_path.exists():
                metrics_disk = json.loads(metrics_path.read_text())
            else:
                metrics_disk = {}

            metrics = {**metrics_disk, **metrics}
            metrics = {str(k): v for k, v in metrics.items() if k in ALL_METRICS}
            metrics_path.write_text(json.dumps(metrics, indent=4, sort_keys=True))
            # save combined metrics into predictions object for averaging
            predictions.metrics_per_sample[sample_id] = metrics

        aggregate_metrics[split] = predictions.average_metrics()

    metrics_path = run_dir / cfg.metrics_filename
    if metrics_path.exists():
        metrics_disk = json.loads(metrics_path.read_text())
    else:
        metrics_disk = {}
    metrics = {
        split: {**metrics_disk.get(split, {}), **aggregate_metrics.get(split, {})}
        for split in set((*metrics_disk.keys(), *aggregate_metrics.keys()))
    }
    metrics = {
        split: {str(k): v for k, v in metrics_.items() if k in ALL_METRICS}
        for split, metrics_ in metrics.items()
    }
    metrics_path.write_text(json.dumps(metrics, indent=4, sort_keys=True))


if __name__ == "__main__":
    cfg.apply()
    main(cfg)
