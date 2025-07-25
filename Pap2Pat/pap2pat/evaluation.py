import json
from pathlib import Path
import pickle
import re
from typing import Literal

from logging import getLogger
from mpire.pool import WorkerPool as Pool
import pandas as pd
from pyrootutils import setup_root
import torch
from tqdm import tqdm
from typing import Generator

from pap2pat.clustering import split_doc_and_cluster_sections, ClusteredPatent
from pap2pat.metrics import (
    BLEU,
    Rouge,
    RR,
    Tokens,
    BERTScore,
    RepetitionScore,
    language as language_eval,
    stylometrix as sm_eval,
    scale,
    CoherenceMetrics
)

root = setup_root(__file__)
logger = getLogger("pap2pat_evaluator")


# used as cache to avoid redundant loading and parsing
pap2pat_metadata = {}
ground_truth_patents = {}
papers = {}


class Predictions:
    def __init__(
        self,
        preds: dict[str, str],
        split: Literal["train", "val", "test", "non-contaminated-test"],
        data_path: Path = root / "data",
    ):
        self.preds = preds
        self.split = split
        self.data_path = data_path
        self.clustered_docs: dict[str, ClusteredPatent] = {}
        self.metrics_per_sample: dict[str, dict] = {}
        self.metrics: dict = {}

        # load pap2pat metadata
        global pap2pat_metadata
        if not pap2pat_metadata:
            pap2pat_metadata = json.loads(data_path.joinpath("metadata.json").read_text())

        # check if predictions have correct ids
        pred_ids = set(preds.keys())
        true_ids = set(pap2pat_metadata["splits"][split])
        if pred_ids != true_ids:
            raise ValueError(
                f"Incorrect IDs in predictions for split {split}!\n"
                f"Additional IDs in predictions: {pred_ids-true_ids}\n"
                f"Missing IDs in predictions: {true_ids-pred_ids}"
            )

        # load ground truth patents
        global ground_truth_patents
        for sample_id in pap2pat_metadata["splits"][split]:
            if sample_id not in ground_truth_patents:
                ground_truth_patents[sample_id] = (
                    data_path.joinpath(sample_id).joinpath("patent.md").read_text()
                )

        # load papers
        global papers
        for sample_id in pap2pat_metadata["splits"][split]:
            if sample_id not in papers:
                papers[sample_id] = data_path.joinpath(sample_id).joinpath("paper.md").read_text()

        # split documents and cluster sections into ("Background", "Summary", "Detailed Description")
        self.clustered_docs = {
            sample_id: split_doc_and_cluster_sections(
                preds[sample_id], ground_truth_patents[sample_id]
            )
            for sample_id in pap2pat_metadata["splits"][split]
        }

    def compute_bleu(self) -> None:
        bleu = BLEU()
        for sample_id, doc in tqdm(self.clustered_docs.items(), desc="Computing BLEU"):
            metrics = bleu.compute(doc)
            self.metrics_per_sample[sample_id] = {
                **self.metrics_per_sample.get(sample_id, {}),
                **metrics,
            }

    def compute_rouge(self, n_processes=12) -> None:
        rouge = Rouge()
        with Pool(n_processes) as pool:

            def rouge_wrapper(sample_id, doc):
                return sample_id, rouge.compute(doc)

            for sample_id, metrics in tqdm(
                pool.imap(rouge_wrapper, self.clustered_docs.items()),
                desc="Computing ROUGE",
                total=len(self.clustered_docs),
            ):
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

    def compute_repetitions(self, n_processes=12) -> None:
        with Pool(n_processes, use_worker_state=True, use_dill=True) as pool:
            # load tokenizer and spacy model in each process at initialization
            def init_worker(worker_state: dict):
                worker_state["score"] = RepetitionScore()

            def compute_repetitions_wrapper(worker_state: dict, sample_id: str):
                gen_patent = self.preds[sample_id]
                orig_patent = ground_truth_patents[sample_id]
                paper = papers[sample_id]
                metrics = {
                    "repetitions": {
                        "generated": worker_state["score"].compute(gen_patent)[1],
                        "reference": worker_state["score"].compute(orig_patent)[1],
                        "paper": worker_state["score"].compute(paper)[1],
                    }
                }
                return sample_id, metrics

            for sample_id, metrics in tqdm(
                pool.imap(
                    compute_repetitions_wrapper,
                    list(self.clustered_docs),
                    worker_init=init_worker,
                ),
                desc="Computing repetitions",
                total=len(self.clustered_docs),
            ):
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

    def compute_rr(self, n_processes=12, **kwargs) -> None:
        with Pool(n_processes, use_worker_state=True, use_dill=True) as pool:
            # load tokenizer in each process at initialization
            def init_worker(worker_state: dict):
                worker_state["rr"] = RR(**kwargs)

            def compute_rr_wrapper(worker_state: dict, sample_id: str):
                gen_patent = self.preds[sample_id]
                orig_patent = ground_truth_patents[sample_id]
                paper = papers[sample_id]
                metrics = worker_state["rr"].compute(gen_patent, orig_patent, paper)
                return sample_id, metrics

            for sample_id, metrics in tqdm(
                pool.imap(
                    compute_rr_wrapper,
                    list(self.clustered_docs),
                    worker_init=init_worker,
                ),
                desc="Computing RR",
                total=len(self.clustered_docs),
            ):
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

    def compute_coherence(self, devices: list[str] | None = None) -> None:
        if devices is None:
            n_gpus = torch.cuda.device_count()
            devices = [f"cuda:{i}" for i in range(n_gpus)]

        if len(devices) < 1:
            logger.error("No devices selected. Cannot compute discoscore without GPU")
            return

        logger.info(f"Computing discoscore on devices: {devices}")


        with Pool(len(devices), use_worker_state=True, use_dill=True, pass_worker_id=True, start_method="spawn") as pool:

            def init_worker(worker_id: int, worker_state: dict):
                device = f"cuda:{worker_id}"
                logger.info(f"Initializing DiscoScore on GPU '{device}'")
                worker_state["CoherenceMetrics"] = CoherenceMetrics(device=device)

            def compute_coherence_wrapper(worker_id: int, worker_state: dict, sample_id: str, gen_patent: str, ref_patent: str):
                scores = worker_state["CoherenceMetrics"].score(gen_patent, ref_patent)
                return sample_id, {"coherence": scores}
            
            def get_inputs(
                sample_ids: list[str],
            ) -> Generator[tuple[str, str, str], None, None]:
                for sample_id in sample_ids:
                    yield (
                        sample_id,
                        self.preds[sample_id],
                        ground_truth_patents[sample_id],
                    )

            for sample_id, metrics in tqdm(
                pool.imap(
                    compute_coherence_wrapper,
                    list(get_inputs(list(self.clustered_docs.keys()))),
                    worker_init=init_worker,
                ),
                desc="Computing Coherence",
                total=len(self.clustered_docs),
            ):
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

    def compute_tokens(self, n_processes=12) -> None:
        with Pool(n_processes, use_worker_state=True, use_dill=True) as pool:
            # load tokenizer in each process at initialization
            def init_worker(worker_state: dict):
                worker_state["tokens"] = Tokens()

            def compute_tokens_wrapper(worker_state: dict, sample_id: str, doc: ClusteredPatent):
                metrics = worker_state["tokens"].compute(doc)
                return sample_id, metrics

            for sample_id, metrics in tqdm(
                pool.imap(
                    compute_tokens_wrapper,
                    list(self.clustered_docs.items()),
                    worker_init=init_worker,
                ),
                desc="Computing Tokens",
                total=len(self.clustered_docs),
            ):
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

    def compute_bertscore(self, devices: list[str] | None = None) -> None:
        if devices is None:
            n_gpus = torch.cuda.device_count()
            devices = [f"cuda:{i}" for i in range(n_gpus)]

        if len(devices) < 1:
            logger.error("No devices selected. Cannot compute bertscore without GPU")
            return

        logger.info(f"Computing BERTScore on devices: {devices}")

        with Pool(
            len(devices),
            use_worker_state=True,
            use_dill=True,
            pass_worker_id=True,
            start_method="spawn",
        ) as pool:
            # load model in each process at initialization
            def init_worker(worker_id: int, worker_state: dict):
                device = f"cuda:{worker_id}"
                logger.info(f"Initializing BERTScore on GPU '{device}'")
                bertscore = BERTScore(device)
                worker_state["bertscore"] = bertscore

            def compute_bertscore_wrapper(
                worker_id: int,
                worker_state: dict,
                sample_id: str,
                clustered_doc: ClusteredPatent,
                gen_patent: str,
                orig_patent: str,
            ):
                # logger.info(sample_id)
                metrics = worker_state["bertscore"].compute(
                    doc=clustered_doc, orig_patent=orig_patent, gen_patent=gen_patent
                )
                return sample_id, metrics

            def get_inputs(
                sample_ids: list[str],
            ) -> Generator[tuple[str, ClusteredPatent, str, str], None, None]:
                for sample_id in sample_ids:
                    yield (
                        sample_id,
                        self.clustered_docs[sample_id],
                        self.preds[sample_id],
                        ground_truth_patents[sample_id],
                    )

            for sample_id, metrics in tqdm(
                pool.imap(
                    compute_bertscore_wrapper,
                    list(get_inputs(list(self.clustered_docs))),
                    worker_init=init_worker,
                ),
                desc="Computing BERTScore",
                total=len(self.clustered_docs),
            ):
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

    def compute_language(self, n_processes=12, n=list(range(1, 5)), k=1000, cache=True) -> None:
        
        def get_n_gram_profiles():
            if cache and language_eval.pkl_path.exists():
                with language_eval.pkl_path.open("rb") as fp:
                    profiles = pickle.load(fp)
            else:
                profiles = {}
            
            if self.split not in profiles:
                patent_counts = language_eval.get_n_gram_counts(
                    language_eval.load_dataset_files(self.data_path, self.split, "patent.md", metadata=pap2pat_metadata or None),
                    n=n,
                    n_processes=n_processes,
                )
                paper_counts = language_eval.get_n_gram_counts(
                    language_eval.load_dataset_files(self.data_path, self.split, "paper.md", metadata=pap2pat_metadata or None),
                    n=n,
                    n_processes=n_processes,
                )
                patent_profile = language_eval.get_top_k_per_n_and_normalize(
                    patent_counts, k=k
                )
                paper_profile = language_eval.get_top_k_per_n_and_normalize(paper_counts, k=k)
                profiles[self.split] = {"patent": patent_profile, "paper": paper_profile}

                if cache:
                    with language_eval.pkl_path.open("wb") as fp:
                        pickle.dump(profiles, fp)

            return profiles[self.split]["patent"], profiles[self.split]["paper"]

        def get_stylometrix_profiles():
            if cache and sm_eval.pkl_path.exists():
                with sm_eval.pkl_path.open("rb") as fp:
                    profiles = pickle.load(fp)
            else:
                profiles = {}

            if self.split not in profiles:
                patent_features = sm_eval.get_stylometrics_features(
                    sm_eval.load_dataset_files(self.data_path, self.split, "patent.md", metadata=pap2pat_metadata or None),
                    n_processes=n_processes,
                )
                paper_features = sm_eval.get_stylometrics_features(
                    sm_eval.load_dataset_files(self.data_path, self.split, "paper.md", metadata=pap2pat_metadata or None),
                    n_processes=n_processes,
                )
                profiles[self.split] = {"patent": patent_features, "paper": paper_features}
                
                if cache:
                    with sm_eval.pkl_path.open("wb") as fp:
                        pickle.dump(profiles, fp)

            return profiles[self.split]["patent"], profiles[self.split]["paper"]

        logger.info("Loading reference n-gram profiles")
        patent_n_gram_profile, paper_n_gram_profile = get_n_gram_profiles()
        logger.info("Loading reference stylometrix profiles")
        patent_stylometrix_profile, paper_stylometrix_profile = get_stylometrix_profiles()
        logger.info("Computing model n-gram profile")
        model_n_gram_profile = language_eval.get_top_k_per_n_and_normalize(
            language_eval.get_n_gram_counts(
                self.preds.values(), n=list(range(1, 5)), n_processes=12
            ),
            k=1000,
        )
        logger.info("Computing model stylometrix profile")
        model_stylometrix_profile = sm_eval.get_stylometrics_features(
            self.preds.values(), n_processes
        )

        scores = {
            "patent": language_eval.add_avg(
                {
                    **language_eval.profile_similarity(model_n_gram_profile, patent_n_gram_profile),
                    **language_eval.profile_similarity(
                        {"stylometrix": model_stylometrix_profile},  # type: ignore
                        {"stylometrix": patent_stylometrix_profile},  # type: ignore
                    ),
                }
            ),
            "paper": language_eval.add_avg(
                {
                    **language_eval.profile_similarity(model_n_gram_profile, paper_n_gram_profile),
                    **language_eval.profile_similarity(
                        {"stylometrix": model_stylometrix_profile},  # type: ignore
                        {"stylometrix": paper_stylometrix_profile},  # type: ignore
                    ),
                }
            ),
        }
        self.metrics["language"] = scores

    def compute_factuality(self, k: int = 5) -> None:
        args = [
            {
                "sample": sample_id,
                "generated": gen,
                "reference": ground_truth_patents[sample_id],
                "paper": papers[sample_id],
                "k": k,
            }
            for sample_id, gen in self.preds.items()
        ]

        with Pool(
            torch.cuda.device_count(),
            use_worker_state=True,
            use_dill=True,
            pass_worker_id=True,
            start_method="spawn",
        ) as pool:
            for arg, metrics in tqdm(
                zip(args, pool.imap(scale.score_patent, args, worker_init=scale.init)),
                total=len(args),
                desc="Computing Factuality",
            ):
                sample_id = arg["sample"]
                self.metrics_per_sample[sample_id] = {
                    **self.metrics_per_sample.get(sample_id, {}),
                    **metrics,
                }

        # ws = {}
        # scale.init(0, ws)
        # args = [
        #     {
        #         "worker_id": 0,
        #         "worker_state": ws,
        #         "sample": sample_id,
        #         "generated": gen,
        #         "reference": ground_truth_patents[sample_id],
        #         "paper": papers[sample_id],
        #         "k": k
        #     }
        #     for sample_id, gen in self.preds.items()
        # ]
        # for arg, metrics in tqdm(
        #     zip(args, scale.imap(scale.score_patent, args)),
        #     total=len(args),
        #     desc="Computing Factuality",
        # ):
        #     sample_id = arg["sample"]
        #     self.metrics_per_sample[sample_id] = {
        #         **self.metrics_per_sample.get(sample_id, {}),
        #         **metrics,
        #     }

    def compute_chunk_stats(self, run_dir: Path) -> None:
        logger.info("Computing chunk stats")
        for sample_id in tqdm(list(self.preds.keys()), desc="Computing chunk stats"):

            n_chunks = 0
            for f in run_dir.glob(f"predictions/{self.split}/{sample_id}/conversations/chunk-*-assistant.md"):
                response = re.findall(r"```md(.*)```", f.read_text(), re.DOTALL)[0]
                response = "\n".join([line for line in response.split("\n") if not line.startswith("#")]).strip()
                if response:
                    n_chunks += 1

            n_bullets = 0
            for f in run_dir.glob(f"predictions/{self.split}/{sample_id}/conversations/chunk-*-user.md"):
                outline = re.findall(r"```md(.*)```", f.read_text(), re.DOTALL)[-1]
                n_bullets_ = len(re.findall(r"(\n-.*)", outline))
                if n_bullets_:
                    n_bullets += n_bullets_

            self.metrics_per_sample[sample_id] = {
                **self.metrics_per_sample.get(sample_id, {}),
                **{
                    "chunk_stats": {
                        "n_chunks": n_chunks,
                        "bullets_per_chunk": n_bullets / n_chunks
                    }
                }
            }

    def average_metrics(self) -> dict:
        return {
            **self.metrics,
            **MetricAverager(list(self.metrics_per_sample.values())).get_average(),
        }


class MetricAverager:
    def __init__(self, all_metrics: list[dict]):
        self.all_metrics = all_metrics
        self.paths = set(path for metrics in all_metrics for path in self.get_paths(metrics))

    @staticmethod
    def get_paths(metrics, _path=tuple()):
        if isinstance(metrics, dict):
            for k, v in metrics.items():
                yield from MetricAverager.get_paths(v, (*_path, k))
        elif isinstance(metrics, list):
            for k, v in enumerate(metrics):
                yield from MetricAverager.get_paths(v, (*_path, k))
        elif isinstance(metrics, int) or isinstance(metrics, float):
            yield _path

    def get_average(self):
        averaged_metrics = {}
        for path in self.paths:
            all_values = [self.get_value(metrics, path) for metrics in self.all_metrics]
            all_values = pd.Series([value for value in all_values if value is not None])
            self.set_value(
                averaged_metrics,
                path,
                {
                    "mean": all_values.mean(),
                    "n": len(all_values),
                    "std": all_values.std(),
                },
            )
        return averaged_metrics

    @staticmethod
    def get_value(metrics, path):
        if metrics is None:
            return None
        if len(path) == 0:
            return metrics
        key, path = path[0], path[1:]
        try:
            metrics = metrics[key]
        except (KeyError, IndexError):
            return None
        return MetricAverager.get_value(metrics, path)

    @staticmethod
    def set_value(metrics: dict | list, path: tuple[str | int, ...], value):
        if len(path) == 1:
            metrics[path[0]] = value  # type: ignore
            return
        key, path = path[0], path[1:]
        if isinstance(metrics, dict):
            assert isinstance(key, str), "key is not str"
            if key not in metrics:
                if isinstance(key, str):
                    metrics[key] = {}
                elif isinstance(key, int):
                    metrics[key] = []
        elif isinstance(metrics, list):
            assert isinstance(key, int), "key is not int"
            if len(metrics) < key + 1:
                metrics = metrics + [None] * (len(metrics) - key + 1)
        return MetricAverager.set_value(metrics[key], path, value)  # type: ignore
