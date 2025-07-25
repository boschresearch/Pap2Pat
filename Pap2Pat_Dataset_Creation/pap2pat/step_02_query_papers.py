import datetime
import json
import time
from dataclasses import dataclass
from functools import partial
from multiprocessing import Pool
from pathlib import Path

import pandas as pd
from fire import Fire
from pyrootutils import setup_root
from SPARQLWrapper import get_sparql_dataframe
from tqdm import tqdm

from pap2pat.utils import (
    LIST_FIELDS,
    get_logger,
    get_num_pickles,
    launch_debugger,
    load_pickle_generator,
)

log = get_logger(__file__)
root = setup_root(__file__)

SPARQL_ENDPOINT = "https://semopenalex.org/sparql"
SPARQL_QUERY = root.joinpath("ppp/step_02_query.sparql").read_text()
EMPTY_PLACEHOLDER = "<EMPTY>"


@dataclass
class QueryReturnStatus:
    status: str


TOO_FEW_INVENTORS = QueryReturnStatus("too_few_inventors")
ERROR_IN_REQUEST = QueryReturnStatus("error_in_request")


def query(
    patent: dict,
    author_overlap_threshold: float,
    days_before: int,
    days_after: int,
    min_inventors: int,
    retry_count=0,
) -> pd.DataFrame | QueryReturnStatus:
    if len(patent["inventors"]) < min_inventors:
        return TOO_FEW_INVENTORS

    inventors = [f"\"{' '.join(inventor)}\"" for inventor in patent["inventors"]]
    inventors_list = ", ".join(inventors)
    earliest_date = patent["application_date"] - datetime.timedelta(days=days_before)
    latest_date = patent["application_date"] + datetime.timedelta(days=days_after)

    query_str = (
        SPARQL_QUERY.replace("<AUTHOR_LIST>", inventors_list)
        .replace("<NUM_AUTHORS>", str(len(patent["inventors"])))
        .replace("<AUTHOR_OVERLAP_THRESHOLD>", str(author_overlap_threshold))
        .replace("<DATE_EARLIEST>", earliest_date.isoformat())
        .replace("<DATE_LATEST>", latest_date.isoformat())
        .replace("<EMPTY_PLACEHOLDER>", EMPTY_PLACEHOLDER)
    )

    try:
        results = get_sparql_dataframe(SPARQL_ENDPOINT, query_str)
        if len(results) > 0:
            results.insert(0, column="patent", value=[patent["id"]] * len(results))
            # Split concatenated lists along \n and replace empty placeholder string with None
            for k in LIST_FIELDS:
                results[k] = results[k].apply(
                    lambda x: [s if s != EMPTY_PLACEHOLDER else None for s in x.split("\n")]
                )
        return results

    except Exception as e:  # noqa
        # log.warning(f"Error during SparQL request: {repr(e)}")
        if retry_count < 1:
            time.sleep(5)
            return query(
                patent=patent,
                author_overlap_threshold=author_overlap_threshold,
                days_after=days_after,
                days_before=days_before,
                min_inventors=min_inventors,
                retry_count=retry_count + 1,
            )
        else:
            # log.error(f"Repeated Error during SparQL request: {repr(e)}")
            return ERROR_IN_REQUEST


def main(
    patents_path: Path = root / "data" / "outputs" / "patents.pickle",
    patents_index_path: Path = root / "data" / "outputs" / "patents_index.pickle",
    candidates_path: Path = root / "data" / "outputs" / "candidates.csv",
    querying_state_path: Path = root / "data" / "outputs" / "_querying_state.json",
    n_threads: int = 16,
    author_overlap_threshold: float = 0.8,
    min_inventors: int = 2,
    days_before: int = 365 * 1,
    days_after: int = 365 * 2,
    debug: bool = False,
):
    if debug:
        launch_debugger()

    query_ = partial(
        query,
        author_overlap_threshold=author_overlap_threshold,
        days_after=days_after,
        days_before=days_before,
        min_inventors=min_inventors,
    )
    num_patents = get_num_pickles(patents_index_path)

    # Restore last state from disk if possible
    if querying_state_path.exists():
        state = json.loads(querying_state_path.read_text())
        log.info(f"Restored old state: {json.dumps(state)}")
    else:
        state = {
            "num_checked_patents": 0,
            "num_papers": 0,
            "runtime": 0.0,
            TOO_FEW_INVENTORS.status: 0,
            ERROR_IN_REQUEST.status: 0,
        }

    saved_results_to_disk = False
    results = pd.DataFrame()

    try:
        with (
            tqdm(
                total=num_patents,
                desc="Querying SemOpenAlex",
                initial=state["num_checked_patents"],
            ) as pbar,
            Pool(n_threads) as p,
        ):
            pbar.start_t -= state["runtime"]
            start = time.time()
            for results in p.imap(
                query_,
                load_pickle_generator(
                    patents_path,
                    skip=state["num_checked_patents"],
                    index_path=patents_index_path,
                ),
                chunksize=128,
            ):
                saved_results_to_disk = False

                state["num_checked_patents"] += 1
                new_start = time.time()
                state["runtime"] += new_start - start
                start = new_start

                if isinstance(results, QueryReturnStatus):
                    state[results.status] += 1

                elif len(results) > 0:
                    state["num_papers"] += len(results)
                    querying_state_path.write_text(json.dumps(state))
                    results.to_csv(
                        candidates_path,
                        sep=";",
                        mode="a",
                        index=False,
                        header=(not candidates_path.exists()),
                    )
                    saved_results_to_disk = True

                pbar.update(1)
                pbar.set_postfix({k: v for k, v in state.items() if k != "num_checked_patents"})

    except KeyboardInterrupt:
        log.info("Detected Keyboard interrupt. Terminating ...")

    finally:
        querying_state_path.write_text(json.dumps(state))
        if not saved_results_to_disk and isinstance(results, pd.DataFrame) and len(results) > 0:
            results.to_csv(
                candidates_path,
                sep=";",
                mode="a",
                index=False,
                header=(not candidates_path.exists()),
            )


if __name__ == "__main__":
    Fire(main)
