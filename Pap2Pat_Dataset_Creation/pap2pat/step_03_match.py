import csv
import json
import pickle
from collections import defaultdict
from functools import partial
from multiprocessing import Pool
from pathlib import Path

import pandas as pd
import spacy.tokens
from cdifflib import CSequenceMatcher
from fire import Fire
from nltk.stem import PorterStemmer
from pyrootutils import setup_root
from rich.console import Console
from rich.table import Table
from sklearn.feature_extraction.text import TfidfVectorizer
from tqdm import tqdm
from utils import (
    get_logger,
    is_compute_node,
    launch_debugger,
    load_csv,
    load_csv_generator,
    load_pickle_by_id,
    print_pair,
)

spacy_pipeline = spacy.load("en_core_web_sm", enable=["tagger"])
stemmer = PorterStemmer()

log = get_logger(__file__)
root = setup_root(__file__)
idf: dict[str, float] = None  # type: ignore | global variable to hold idf values to avoid serialization in multiprocessing


def get_terms(doc: spacy.tokens.Doc):
    """From a spacy document, extract the token set after stopword removal and stemming"""

    def get_term(token):
        if token.is_stop or token.is_punct or not token.text.strip():
            return None
        return stemmer.stem(token.text.strip())

    terms = set()
    for token in doc:
        term = get_term(token)
        if term is not None:
            terms.add(term)

    return terms


def run_spacy_pipeline(
    patent_ids: list[str],
    patent_strs: list[str],
    paper_ids: list[str],
    paper_strs: list[str],
):
    """Run spacy pipeline without redundantly running it for the same text"""
    documents = list(zip(patent_ids + paper_ids, patent_strs + paper_strs))
    docs_set = set(documents)

    ids_unique = [id for id, _ in docs_set]
    strs_unique = [str for _, str in docs_set]

    encs = {id: enc for id, enc in zip(ids_unique, spacy_pipeline.pipe(strs_unique, batch_size=32))}

    for patent_id, paper_id in zip(patent_ids, paper_ids):
        yield encs[patent_id], encs[paper_id]


def term_overlaps(
    patent_ids: list[str],
    patent_strs: list[str],
    paper_ids: list[str],
    paper_strs: list[str],
    idf: dict,
) -> tuple[list[float], list[float]]:
    """Compute term overlaps for pairs"""
    min_overlaps, max_overlaps = [], []

    for patent_enc, paper_enc in run_spacy_pipeline(patent_ids, patent_strs, paper_ids, paper_strs):
        # Get term sets
        patent_terms = get_terms(patent_enc)
        paper_terms = get_terms(paper_enc)

        # Add idf weights
        patent_terms = {(term, idf.get(term, 1)) for term in patent_terms}
        paper_terms = {(term, idf.get(term, 1)) for term in paper_terms}

        # Compute metrics
        overlap_sum = sum(weight for term, weight in patent_terms.intersection(paper_terms))
        total_sums = [
            sum(weight for term, weight in terms) for terms in (patent_terms, paper_terms)
        ]
        min_sum = min(total_sums)
        max_sum = max(total_sums)
        min_overlap = overlap_sum / min_sum if min_sum > 0 else 0
        max_overlap = overlap_sum / max_sum if max_sum > 0 else 0

        min_overlaps.append(min_overlap)
        max_overlaps.append(max_overlap)

    return min_overlaps, max_overlaps


def match(
    candidates: list[dict],
    patents_path: Path,
    patents_index_path: Path,
    thresholds: dict[str, float],
    min_margins: dict[str, float],
    duplicate_copy_thresholds: dict[str, float],
) -> tuple[list[dict], list[dict], list[dict], list[bool], list[int], list[int]]:
    """Main matching function. Load patent --> compute overlap metrics --> deduplicate & disambiguate"""
    # Load patents from disk
    patent_ids = set(cand["patent"] for cand in candidates)
    patents = {
        patent_ids: load_pickle_by_id(patent_ids, patents_path, patents_index_path)
        for patent_ids in patent_ids
    }
    patents = [patents[candidate["patent"]] for candidate in candidates]

    # Compute metrics
    title_min, title_max = term_overlaps(
        [patent["id"] for patent in patents],
        [patent["title"] for patent in patents],
        [candidate["paper"] for candidate in candidates],
        [candidate["title"] for candidate in candidates],
        idf,
    )
    abstract_min, abstract_max = term_overlaps(
        [patent["id"] for patent in patents],
        [patent["abstract"] for patent in patents],
        [candidate["paper"] for candidate in candidates],
        [candidate["abstract"] for candidate in candidates],
        idf,
    )
    metrics = [
        dict(
            title_min=title_min_,
            title_max=title_max_,
            abstract_min=abstract_min_,
            abstract_max=abstract_max_,
            author_overlap=candidate["author_overlap"],
        )
        for title_min_, title_max_, abstract_min_, abstract_max_, candidate in zip(
            title_min, title_max, abstract_min, abstract_max, candidates
        )
    ]

    # Deduplicate and disambiguate
    matched_list = [all(v >= thresholds[k] for k, v in metrics_.items()) for metrics_ in metrics]
    duplicate_idxs, ambiguous_idxs, concat_mapping = find_duplicates_and_ambiguous_matches(
        candidates, metrics, min_margins, duplicate_copy_thresholds
    )

    # Concatenate paper info from duplicates into main entry
    for i, jl in concat_mapping.items():
        for field in ["locations", "urls", "pdf_urls", "licenses"]:
            for j in jl:
                for v in candidates[j][field]:
                    candidates[i][field].append(v)

    return candidates, patents, metrics, matched_list, duplicate_idxs, ambiguous_idxs


def copy_similarity(s1: str, s2: str) -> float:
    """Similarity metric based on exact matched (copy pasted) substrings. Used for deduplication"""
    sm = CSequenceMatcher(None, s1.lower(), s2.lower(), autojunk=False)
    copied = sum(block.size for block in sm.get_matching_blocks())
    return 2 * copied / (len(s1) + len(s2))


def check_duplicate(cand1: dict, cand2: dict, thresholds: dict[str, float]) -> bool:
    """Deduplication heuristics"""
    if copy_similarity(cand1["title"], cand2["title"]) < thresholds["title"]:
        return False

    if (
        copy_similarity(cand1["abstract"], cand2["abstract"]) < thresholds["abstract"]
        # if one abstract is missing in SOA, detect as duplicate even if copy similarity is low
        # --> keep longer one
        and len(cand1["abstract"]) > 80
        and len(cand2["abstract"]) > 80
    ):
        return False

    return True


def find_duplicates_and_ambiguous_matches(
    candidates: list[dict],
    metrics_list: list[dict],
    min_margins: dict[str, float],
    duplicate_copy_thresholds: dict[str, float],
) -> tuple[list[int], list[int], dict]:
    """Deduplicate and disambiguate matches/candidates"""

    duplicate_idxs = []
    ambiguous_idxs = []
    concat_mapping = defaultdict(list)

    patent_ids = {c["patent"] for c in candidates}

    for patent_id in patent_ids:
        # get all indices of candidates with that patent id
        idxs = [i for i, c in enumerate(candidates) if c["patent"] == patent_id]

        if len(idxs) < 2:
            continue

        for i in idxs:
            for j in idxs:
                if i < j or i == j:
                    continue
                if check_duplicate(candidates[i], candidates[j], duplicate_copy_thresholds):
                    # if two papers are (near-)duplicates, keep the longer one to avoid information loss
                    longer_index = (
                        i if len(candidates[i]["abstract"]) > len(candidates[j]["abstract"]) else j
                    )
                    shorter_index = i if longer_index == j else j

                    duplicate_idxs.append(shorter_index)
                    concat_mapping[longer_index].append(shorter_index)
                    if shorter_index in concat_mapping:
                        concat_mapping[longer_index].extend(concat_mapping.pop(shorter_index))

        # if this candidates outperforms all other candidates for that patent
        # in at least 3 metrics by at least min_margin, keep only this one, otherwise discard all
        for i in idxs:
            if i in duplicate_idxs:
                continue

            other_i = [idx for idx in idxs if idx != i and idx not in duplicate_idxs]
            if all(
                [
                    sum(
                        [
                            (value >= (metrics_list[j][metric] + min_margins[metric]))
                            for metric, value in metrics_list[i].items()
                            if metric in min_margins
                        ]
                    )
                    >= 3
                    for j in other_i
                ]
            ):
                ambiguous_idxs.extend(other_i)
                break
        else:
            ambiguous_idxs.extend(idxs)

    return (
        duplicate_idxs,
        ambiguous_idxs,
        {i: lj for i, lj in concat_mapping.items() if lj},
    )


def _get_terms_for_candidates(
    candidates: list[dict], patents_path: Path, patents_index_path: Path
) -> tuple[list[tuple[str, list[str]]], int]:
    """Compute term sets for candidates in IDF computation"""
    seen = set()
    docs = []

    for candidate in candidates:
        if candidate["paper"] not in seen:
            docs.append((candidate["paper"], f"{candidate['title']}\n\n{candidate['abstract']}"))
            seen.add(candidate["paper"])

        if candidate["patent"] not in seen:
            patent = load_pickle_by_id(candidate["patent"], patents_path, patents_index_path)
            docs.append((candidate["patent"], f"{patent['title']}\n\n{patent['abstract']}"))
            seen.add(candidate["patent"])

    terms_list = []
    for (id, _), doc in zip(docs, spacy_pipeline.pipe((doc[1] for doc in docs), batch_size=16)):
        terms = get_terms(doc)
        terms_list.append((id, terms))

    return terms_list, len(candidates)


def _load_token_lists_for_idf(
    candidates_path: Path,
    patents_path: Path,
    patents_index_path: Path,
    num_candidates: int,
):
    """Wrapper around _get_terms_for_candidates to load tokens in multiple processes"""
    seen = set()
    __load_candidate = partial(
        _get_terms_for_candidates,
        patents_path=patents_path,
        patents_index_path=patents_index_path,
    )
    with Pool(32) as p, tqdm(total=num_candidates, desc="Loading titles and abstracts") as pbar:
        for term_list, n_candidates in p.imap(
            __load_candidate,
            load_csv_generator(candidates_path, 32, dont_split_along="patent"),
        ):
            for id, tokens in term_list:
                if id not in seen:
                    yield tokens
                    seen.add(id)
            pbar.update(n_candidates)


def compute_idf(
    idf_path: Path,
    candidates_path: Path,
    patents_path: Path,
    patents_index_path: Path,
    num_candidates: int,
):
    """Compute or load IDF weights"""
    if idf_path.exists():
        log.info(f"Caching IDF weights from {idf_path}")
        with idf_path.open("rb") as fp:
            idf = pickle.load(fp)

    else:
        vectorizer = TfidfVectorizer(analyzer=lambda x: x)
        vectorizer.fit(
            _load_token_lists_for_idf(
                candidates_path, patents_path, patents_index_path, num_candidates
            )
        )
        # Create dict {term --> idf} without looping through vectorizer.idf_
        vocab_sorted = dict(sorted(vectorizer.vocabulary_.items(), key=lambda x: x[1]))
        idf = dict(zip(vocab_sorted, vectorizer.idf_))
        with idf_path.open("wb") as fp:
            pickle.dump(idf, fp)

    return idf


def main(
    candidates_path: Path = root / "data/outputs/candidates.csv",
    matches_path: Path = root / "data/outputs/matches.csv",
    matches_print_path: Path = root / "data/outputs/matches.log",
    match_metrics_path: Path = root / "data/outputs/match_metrics.pickle",
    query_state_path: Path = root / "data/outputs/_querying_state.json",
    patents_path: Path = root / "data/outputs/patents.pickle",
    patents_index_path: Path = root / "data/outputs/patents_index.pickle",
    idf_path: Path = root / "data/outputs/idf.pickle",
    n_processes: int = 16 if is_compute_node() else 4,
    batch_size: int = 128,
    thresholds: dict = dict(
        author_overlap=0.8,
        title_min=0.15,
        abstract_min=0.15,
        title_max=0.1,
        abstract_max=0.1,
    ),
    duplicate_copy_thresholds: dict[str, float] = dict(title=0.8, abstract=0.6),
    min_margins: dict = dict(title_min=0.15, abstract_min=0.15, title_max=0.1, abstract_max=0.1),
    use_idf: bool = True,
    debug: bool = False,
):
    global idf

    if debug:
        launch_debugger()

    if matches_path.exists() or matches_print_path.exists():
        log.warning("Overwriting previous matches!")
        if matches_path.exists():
            matches_path.unlink()
        if matches_print_path.exists():
            matches_print_path.unlink()

    # Initialize stats
    query_state = json.loads(query_state_path.read_text())
    stats = {"matched": 0, "removed_duplicate": 0, "removed_ambiguous": 0}
    metric_columns = (*thresholds, "author_overlap")
    metrics = {
        k: []
        for k in (
            "paper",
            "patent",
            "ambiguous_paper",
            "duplicate",
            "matched",
            *metric_columns,
        )
    }

    # Initialize IDF weights
    if use_idf:
        log.info("Loading IDF weights")
        idf = compute_idf(
            idf_path,
            candidates_path,
            patents_path,
            patents_index_path,
            query_state["num_papers"],
        )
    else:
        log.info("Setting IDF weights to 1")
        idf = {}

    with (
        Pool(n_processes) as p,
        tqdm(desc="Checking PPPs", total=query_state["num_papers"], postfix=stats) as pbar,
        matches_path.open("w", newline="", encoding="utf-8") as matches_fp,
        matches_print_path.open("w", encoding="utf-8") as matches_print_fp,
    ):
        match_ = partial(
            match,
            patents_path=patents_path,
            patents_index_path=patents_index_path,
            thresholds=thresholds,
            min_margins=min_margins,
            duplicate_copy_thresholds=duplicate_copy_thresholds,
        )

        # Prepare output csv file
        all_fields = next(load_csv_generator(candidates_path, batch_size=1))[0].keys()
        candidate_columns = [c for c in all_fields if c not in metric_columns]
        out_columns = [*candidate_columns, *metric_columns]
        matches_csv_writer = csv.DictWriter(matches_fp, out_columns, delimiter=";")
        matches_csv_writer.writeheader()

        for (
            candidates,
            patents,
            metrics_list,
            matched_list,
            duplicate_idxs,
            ambiguous_idxs,
        ) in p.imap(
            match_,
            load_csv_generator(candidates_path, batch_size=batch_size, dont_split_along="patent"),
        ):
            assert len(candidates) == len(patents) == len(metrics_list)

            for i, (candidate, patent, metrics_, matched) in enumerate(
                zip(candidates, patents, metrics_list, matched_list)
            ):
                if matched:
                    if i in duplicate_idxs:
                        stats["removed_duplicate"] += 1
                    elif i in ambiguous_idxs:
                        stats["removed_ambiguous"] += 1
                    else:
                        stats["matched"] += 1
                        candidate_with_metrics = {**candidate, **metrics_}
                        print_pair(candidate_with_metrics, patent, file=matches_print_fp)
                        matches_csv_writer.writerow(candidate_with_metrics)
                    pbar.set_postfix(stats)

                metrics["paper"].append(candidate["paper"])
                metrics["patent"].append(candidate["patent"])
                metrics["duplicate"].append(bool(i in duplicate_idxs))
                metrics["ambiguous_paper"].append(bool(i in ambiguous_idxs))
                metrics["matched"].append(bool(matched))

                for k, v in metrics_.items():
                    metrics[k].append(v)

            pbar.update(len(candidates))

    matches = load_csv(matches_path)
    if "author_overlap.1" in matches.columns:
        matches.drop(columns=["author_overlap.1"], inplace=True)

    # Filter out cases where we matched multiple patents to the same paper
    paper_counts = matches.paper.value_counts()
    papers_with_multiple_patents = paper_counts[paper_counts > 1].index
    amb_mask = matches.paper.isin(papers_with_multiple_patents)
    matches = matches[~amb_mask]
    metrics["ambiguous_patent"] = [
        paper in papers_with_multiple_patents for paper in metrics["paper"]
    ]
    log.info(
        f"Filtered out {amb_mask.sum()} matches where the same paper was matched with multiple patents!"
    )
    log.info(f"Total matches: {len(matches)}")

    matches.to_csv(matches_path, sep=";", index=False)
    with match_metrics_path.open("wb") as fp:
        pickle.dump(metrics, fp)

    console = Console()
    table = Table(title="Similarity Metric Stats")
    stats = {metric: pd.Series(values).describe().to_dict() for metric, values in metrics.items()}
    stats = {
        metric: {
            "count": len(values),
            "mean": (s := pd.Series(values)).mean(),
            "median": s.median(),
            "std": s.std(),
            "max": s.max(),
            "threshold": thresholds[metric],
            "above_threshold": (s >= thresholds[metric]).sum(),
        }
        for metric, values in metrics.items()
        if metric
        not in (
            "paper",
            "patent",
            "duplicate",
            "ambiguous_paper",
            "ambiguous_patent",
            "matched",
        )
    }
    table.add_column("Stat")
    for k in stats:
        table.add_column(k, justify="right")
    for stat in list(stats.values())[0].keys():
        table.add_row(stat, *[f"{stats[k][stat]:.3f}" for k in stats])
    console.print(table)


if __name__ == "__main__":
    Fire(main)
