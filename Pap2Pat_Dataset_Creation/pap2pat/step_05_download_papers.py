import logging
import re
import shutil
import tarfile
import tempfile
import time
import urllib.request
from dataclasses import dataclass
from functools import partial
from multiprocessing import Pool
from pathlib import Path

import arxiv
import pandas as pd
import requests
from fire import Fire
from pyrootutils import setup_root
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from tqdm import tqdm
from utils import get_logger, launch_debugger, load_csv

arxiv.logger.setLevel(logging.WARNING)

log = get_logger(__file__)
root = setup_root(__file__)


@dataclass
class DownloadStatus:
    pdf: bool = False
    pubmed: bool = False
    arxiv: bool = False


def get_pmcid(match: dict) -> str | None:
    for url in match["urls"] + match["pdf_urls"]:
        r = re.search(r"pmc\d+", url, re.IGNORECASE)
        if r is not None:
            return r.group().upper()


def get_arxiv_id(match: dict) -> str | None:
    for url in match["urls"] + match["pdf_urls"]:
        r = re.search(r"https?://arxiv.org/pdf/(\d+\.\d+)", url)
        if r is None:
            r = re.search(r"https?://arxiv.org/pdf/(.*/\d+)", url)
        if r is not None:
            return r.groups()[0]


def download_pdf(match: dict, out_file: Path, max_wait=60) -> bool:
    if out_file.exists():
        return True

    tmp_dir_ = tempfile.TemporaryDirectory()
    tmp_dir = Path(tmp_dir_.name)
    pdf_found = False

    for url in set(match["pdf_urls"]):
        try:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--ignore-ssl-errors=yes")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--remote-debugging-pipe")
            chrome_options.add_argument("--window-position=-2000,0")
            chrome_options.add_experimental_option(
                "prefs",
                {
                    "download.default_directory": str(tmp_dir),
                    "download.prompt_for_download": False,
                    "download.directory_upgrade": True,
                    "plugins.always_open_pdf_externally": True,
                },
            )
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            waited = 0
            while not list(tmp_dir.glob("*.pdf")) and waited < max_wait:
                time.sleep(0.5)
                waited += 0.5
            driver.quit()

            tmp_dir_contents = list(tmp_dir.glob("*"))
            pdf_files = [
                f for iterator in (tmp_dir.glob("*.pdf"), tmp_dir.glob("*.PDF")) for f in iterator
            ]

            if not pdf_files:
                raise AssertionError(f"No PDF files found! Found {tmp_dir_contents}")

            elif len(pdf_files) > 1:
                log.warning(
                    f"{match['paper']}: Found multiple PDFs: {pdf_files}. Using {pdf_files[0]}"
                )

            out_file.parent.mkdir(exist_ok=True, parents=True)
            tmp_dir_contents[0].rename(str(out_file))
            pdf_found = True

        except Exception as e:
            log.error(f"{match['paper']}: Error while downloading '{url}': {repr(e)}")

        finally:
            if "driver" in locals():
                driver.quit()  # type: ignore

        if pdf_found:
            return True

    return False


def download_pubmed(match: dict, out_dir: Path) -> bool:
    if out_dir.exists():
        return True

    if match["oa_info"] is None:
        return False

    oa_info = match["oa_info"]
    pmcid = oa_info["pmcid"]

    try:
        # Download and extract tarfile to temp directory
        tmp_dir_ = tempfile.TemporaryDirectory()
        tmp_dir = Path(tmp_dir_.name)
        response = requests.get(
            f"https://ftp.ncbi.nlm.nih.gov/pub/pmc/{oa_info['tar']}", stream=True
        )
        tar = tarfile.open(fileobj=response.raw, mode="r|gz")
        tar.extractall(path=tmp_dir)

        # Move files to correct destination
        out_dir.mkdir(exist_ok=True, parents=True)
        for file in tmp_dir.glob("*/*"):
            file.rename(out_dir / file.name)
        return True

    except Exception as e:
        log.error(f"{match['paper']}: Error while downloading {pmcid} from pubmed: {repr(e)}")
        return False


def download_arxiv(match: dict, out_dir: Path) -> bool:
    if out_dir.joinpath("arxiv.tar.gz").exists():
        return True

    arxiv_id = get_arxiv_id(match)
    if arxiv_id is None:
        return False

    try:
        paper = next(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
        out_dir.mkdir(parents=True, exist_ok=True)
        paper.download_source(str(out_dir), "arxiv.tar.gz")
    except Exception as e:
        log.error(f"{match['paper']}: Error while downloading {arxiv_id} from arxiv: {repr(e)}")
        return False

    return True


def download(match: dict, out_dir: Path) -> DownloadStatus:
    status = DownloadStatus()
    paper_id = match["paper"].split("/")[-1]  # soa paper id

    out_dir = out_dir / paper_id
    out_file_pdf = out_dir / "paper.pdf"
    out_dir_pubmed = out_dir / "pmc"

    status.pdf = download_pdf(match, out_file_pdf)
    status.arxiv = download_arxiv(match, out_dir)
    status.pubmed = download_pubmed(match, out_dir_pubmed)

    if not status.pdf:
        log.warning(f"No PDF for {paper_id}")

    return status


def get_pubmed_oa_info(match: dict, pmc_oa_list: pd.DataFrame) -> dict:
    pmcid = get_pmcid(match)
    if pmcid is None:
        match["oa_info"] = None
        return match

    try:
        oa_info = pmc_oa_list.loc[pmcid]
        match["oa_info"] = {"pmcid": oa_info.name, **oa_info}
        return match

    except KeyError:
        # log.warning(f"{match['paper']}: PMCID not found in oa subset list")
        match["oa_info"] = None
        return match


def main(
    matches_path: Path = root / "data" / "outputs" / "matches_with_license.csv",
    pmc_oa_list_path: Path = root / "data" / "pmc_oa_list.txt",
    out_dir: Path = root / "data" / "papers",
    debug: bool = False,
    n_processes: int = 10,
):
    if debug:
        launch_debugger()

    if not out_dir.exists():
        out_dir.mkdir(exist_ok=True, parents=True)

    log.info("Loading pubmed oa list")
    if not pmc_oa_list_path.exists():
        urllib.request.urlretrieve("https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_comm_use_file_list.txt")
    pmc_oa_list = pd.read_csv(
        pmc_oa_list_path,
        skiprows=1,
        sep="\t",
        names=["tar", "journal", "pmcid", "pmid", "license"],
    )
    pmc_oa_list.set_index("pmcid", inplace=True)

    log.info("Loading matches")
    matches_with_license = load_csv(matches_path)

    # Check if there are paper directories which do not correspond to any valid paper from a previous iteration
    all_matched_papers = set(matches_with_license.paper.str.split("/").str.get(-1))
    legacy_dirs = [p for p in out_dir.glob("*") if p.name not in all_matched_papers]
    if legacy_dirs:
        log.warning(
            f"Found {len(legacy_dirs)} directories that are not present in {matches_path}:\n{legacy_dirs}"
        )
        while (a := input("Remove? [y/n]")) not in "yYnN":
            pass
        if a in "yY":
            for legacy_dir in legacy_dirs:
                shutil.rmtree(legacy_dir)
            log.info("Legacy directories deleted")

    matches_with_license = list(
        map(
            partial(get_pubmed_oa_info, pmc_oa_list=pmc_oa_list),
            matches_with_license.to_dict(orient="records"),
        )
    )
    stats = {"pdf": 0, "pubmed": 0, "arxiv": 0}
    pbar = tqdm(desc="Downloading Papers", total=len(matches_with_license), postfix=stats)

    with Pool(n_processes) as p:
        for status in p.imap_unordered(
            partial(download, out_dir=out_dir),
            matches_with_license,
        ):
            pbar.update(1)
            stats["pdf"] += int(status.pdf)
            stats["pubmed"] += int(status.pubmed)
            stats["arxiv"] += int(status.arxiv)
            pbar.set_postfix(stats)


if __name__ == "__main__":
    Fire(main)
