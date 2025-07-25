import json
import pickle
import random
import time
from enum import Enum
from functools import partial
from multiprocessing import Pool
from pathlib import Path
from zipfile import ZipFile

import pandas as pd
import requests
import sglang as sgl
from fire import Fire
from pyrootutils import setup_root
from tqdm import tqdm

from pap2pat.parsers import Section, parse_grobid, parse_patent_xml, parse_pmc
from pap2pat.utils import get_logger, launch_debugger, load_csv, load_pickle_by_id

log = get_logger(__file__)
root = setup_root(__file__)


class ParseStatus(Enum):
    SUCCESS = "success"
    NO_PAPER_PDF = "no_pdf"
    GROBID_FAILED = "grobid_failed"
    PAPER_VALIDATION_FAILED = "paper_validation_failed"
    PATENT_FAILED = "patent_failed"


def get_grobid_xml(paper_dir: Path, grobid_api_base: str, retries_left: int = 5) -> str | Exception:
    pdf_path = paper_dir / "paper.pdf"
    time.sleep(random.random())  # avoid sending multiple requests at exactly the same time
    try:
        with pdf_path.open("rb") as pdf_fp:
            response = requests.post(
                f"{grobid_api_base}/processFulltextDocument", files={"input": pdf_fp}
            )
        response.raise_for_status()
    except Exception as e:
        # log.error(f"{paper_dir.name}: Error during request: {e}")
        if retries_left > 0:
            time.sleep(10)
            # log.error(f"{paper_dir.name}: Retrying ...")
            return get_grobid_xml(paper_dir, grobid_api_base, retries_left - 1)
        return e
    return response.text


def validate_paper(sections: list[Section]) -> bool:
    def iter_paras(secs):
        for sec in secs:
            yield from sec["paragraphs"]
            yield from iter_paras(sec["subsections"])

    n_chars_total = 0
    for para in iter_paras(sections):
        n_chars_total += len(para)

    return n_chars_total > 8000


def parse_sample(
    matches_row_with_xml: dict, grobid_api_base: str, papers_dir: Path
) -> tuple[Path, ParseStatus, str | None, str | None]:
    paper_dir = papers_dir.joinpath(matches_row_with_xml["paper"].split("/")[-1])
    hierarchy_source = None

    # ---------  1. Parse paper  -----------
    paper_json_path = paper_dir.joinpath("paper.json")
    if not paper_json_path.exists():
        paper = dict(
            id=matches_row_with_xml["paper"],
            authors=matches_row_with_xml["author_names"],
            title=matches_row_with_xml["title"],
            date=matches_row_with_xml["date"].strftime("%Y-%m-%d"),
            abstract=matches_row_with_xml["abstract"],
            sections=[],
        )

        # Use pubmed xml if available
        if paper_dir.joinpath("pmc").exists():
            _, sections = parse_pmc(paper_dir)
            paper["sections"] = sections
            paper_source = "pmc"

        # Use grobid from pdf instead
        elif paper_dir.joinpath("paper.pdf").exists():
            paper_source = "grobid"
            # Get grobid xml from endpoint
            if not paper_dir.joinpath("grobid.tei.xml").exists():
                xml = get_grobid_xml(paper_dir, grobid_api_base)
                if isinstance(xml, str):
                    paper_dir.joinpath("grobid.tei.xml").write_text(xml)
                else:
                    return paper_dir, ParseStatus.GROBID_FAILED, None, hierarchy_source

            # Parse grobid xml into json
            _, sections, hierarchy_source = parse_grobid(paper_dir)
            if validate_paper(sections):
                paper["sections"] = sections
            else:
                return (
                    paper_dir,
                    ParseStatus.PAPER_VALIDATION_FAILED,
                    None,
                    hierarchy_source,
                )

        else:
            return paper_dir, ParseStatus.NO_PAPER_PDF, None, hierarchy_source

        paper_dir.joinpath("paper.json").write_text(json.dumps(paper, indent=4))

    else:
        paper_source = "pmc" if paper_dir.joinpath("pmc").exists() else "grobid"

    # ---------  2. Parse patent  -----------
    patent_xml_path = paper_dir.joinpath("patent.xml")
    patent_json_path = paper_dir.joinpath("patent.json")
    if not (patent_xml_path.exists() and patent_json_path.exists()):
        try:
            _, sections = parse_patent_xml(
                matches_row_with_xml["patent_xml"], matches_row_with_xml["patent"]
            )
        except Exception:
            log.exception("Error during patent parsing")
            return paper_dir, ParseStatus.PATENT_FAILED, paper_source, hierarchy_source

        patent = dict(
            id=matches_row_with_xml["patent"],
            authors=matches_row_with_xml["patent_inventors"],
            title=matches_row_with_xml["patent_title"],
            date=matches_row_with_xml["patent_application_date"].strftime("%Y-%m-%d %H:%M:%S"),
            abstract=matches_row_with_xml["patent_abstract"],
            sections=sections,
        )
        patent_xml_path.write_text(matches_row_with_xml["patent_xml"])
        patent_json_path.write_text(json.dumps(patent, indent=4))

    # ---------  3. Save metadata  -----------
    paper_dir.joinpath("match_meta.json").write_text(
        json.dumps(
            dict(
                paper=matches_row_with_xml["paper"],
                patent=matches_row_with_xml["patent"],
                author_overlap=matches_row_with_xml["author_overlap"],
                title_min=matches_row_with_xml["title_min"],
                title_max=matches_row_with_xml["title_max"],
                abstract_min=matches_row_with_xml["abstract_min"],
                abstract_max=matches_row_with_xml["abstract_max"],
            ),
            indent=4,
        )
    )

    return paper_dir, ParseStatus.SUCCESS, paper_source, hierarchy_source


def load_patents_from_zip(args) -> dict:
    zipfile, row = args
    with ZipFile(zipfile) as zf:
        assert len(zf.namelist()) == 1
        filename = zf.namelist()[0]
        with zf.open(filename) as fp:
            contents = fp.read().decode("utf-8")

    xmls = [p for p in contents.split('<?xml version="1.0" encoding="UTF-8"?>') if p]
    return {
        patent_id: xmls[index] for patent_id, index in zip(row["patent"], row["patent_zipfile_idx"])
    }


def load_patent_xmls(
    matches: pd.DataFrame, patents_path: Path, patents_index_path: Path
) -> pd.DataFrame:
    patent_metas = [
        load_pickle_by_id(row.patent, patents_path, patents_index_path)
        for _, row in matches.iterrows()
    ]
    matches["patent_title"] = [m["title"] for m in patent_metas]
    matches["patent_application_date"] = [m["application_date"] for m in patent_metas]
    matches["patent_abstract"] = [m["abstract"] for m in patent_metas]
    matches["patent_inventors"] = [[" ".join(inv) for inv in m["inventors"]] for m in patent_metas]
    matches["patent_zipfile"] = [root / "data" / "uspto" / m["zip_file"].name for m in patent_metas]
    matches["patent_zipfile_idx"] = [m["index_in_zip"] for m in patent_metas]

    xml_strings = {}
    matches_per_zip = matches.groupby("patent_zipfile").agg(list)
    with Pool(12) as p, tqdm(total=len(matches_per_zip), desc="Loading zips") as pbar:
        for xmls in p.imap(load_patents_from_zip, matches_per_zip.iterrows()):
            for pid, xml in xmls.items():
                xml_strings[pid] = xml
            pbar.update(1)

    matches["patent_xml"] = matches.apply(lambda row: xml_strings[row["patent"]], axis=1)
    return matches


def main(
    papers_dir: Path = root / "data" / "papers",
    matches_with_license_path: Path = root / "data" / "outputs" / "matches_with_license.csv",
    patents_path: Path = root / "data" / "outputs" / "patents.pickle",
    patents_index_path: Path = root / "data" / "outputs" / "patents_index.pickle",
    matches_with_patents_cache_path: Path = root
    / "data"
    / "outputs"
    / "matches_with_patents_cache.pickle",
    grobid_api_base: str = "https://kermitt2-grobid.hf.space/api",
    sglang_port: int = 59532,
    n_processes: int = 10,
    debug: bool = False,
):
    if debug:
        launch_debugger()

    sgl.set_default_backend(sgl.RuntimeEndpoint(f"http://localhost:{sglang_port}"))

    log.info("Loading Matches")
    if not matches_with_patents_cache_path.exists():
        matches = load_csv(matches_with_license_path)
        log.info("Extracting Patent XMLs from Zipfiles")
        matches_with_patent = load_patent_xmls(matches, patents_path, patents_index_path)
        with matches_with_patents_cache_path.open("wb") as fp:
            pickle.dump(matches_with_patent, fp)
    else:
        log.info("CACHED: Extracting Patent XMLs from Zipfiles")
        with matches_with_patents_cache_path.open("rb") as fp:
            matches_with_patent = pickle.load(fp)

    stats = {
        **{status.value: 0 for status in ParseStatus},
        "source/pmc": 0,
        "source/grobid": 0,
        "hierarchy/font": 0,
        "hierarchy/numbering": 0,
    }
    parse_sample_fn = partial(parse_sample, grobid_api_base=grobid_api_base, papers_dir=papers_dir)

    args = [
        match
        for match in matches_with_patent.to_dict("records")
        if papers_dir.joinpath(match["paper"].split("/")[-1]).exists()
    ]

    with (
        Pool(n_processes) as p,
        tqdm(
            p.imap_unordered(parse_sample_fn, args),
            desc="Parsing Papers",
            total=len(args),
            postfix=stats,
            dynamic_ncols=True,
        ) as pbar,
    ):
        for paper_dir, status, source, hierarchy_source in pbar:
            stats[status.value] += 1  # type: ignore

            if status is ParseStatus.SUCCESS:
                stats[f"source/{source}"] += 1

                if hierarchy_source is not None:
                    stats[f"hierarchy/{hierarchy_source}"] += 1

            pbar.set_postfix(stats)


if __name__ == "__main__":
    Fire(main)
