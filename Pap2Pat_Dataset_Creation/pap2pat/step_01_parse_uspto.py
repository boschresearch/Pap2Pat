import pickle
from collections import defaultdict
from datetime import datetime
from multiprocessing import Pool
from pathlib import Path
from typing import List, Tuple
from zipfile import BadZipFile, ZipFile

import numpy as np
from fire import Fire
from lxml import etree as etree_lxml
from pyrootutils import setup_root
from tqdm import tqdm
from utils import get_logger, launch_debugger

log = get_logger()
root = setup_root(__file__)


def parse_zip(path: Path) -> Tuple[List[dict], dict]:
    patent_xmls = []
    stats = {
        "parsed": 0,
        "no_title": 0,
        "no_date": 0,
        "no_inventors": 0,
        "no_abstract": 0,
    }

    try:
        with ZipFile(path) as zf:
            for file in zf.namelist():
                with zf.open(file) as fp:
                    contents = fp.read().decode("utf-8")
                xmls = [p for p in contents.split('<?xml version="1.0" encoding="UTF-8"?>') if p]
                patent_xmls.extend(xmls)
    except BadZipFile as e:
        log.error(f"Bad Zip File: {path}. Exception: {e}")
        return [], stats

    patents = []

    for idx_in_zip, patent_xml in enumerate(patent_xmls):
        tree = etree_lxml.fromstring(patent_xml)  # type: ignore

        # Get document ID
        document_id = tree.xpath("//publication-reference/document-id")[0]
        document_id = document_id.xpath("country")[0].text + document_id.xpath("doc-number")[0].text

        # Get Patent Title
        title_results = tree.xpath("//invention-title")
        if not title_results:
            stats["no_title"] += 1
            continue
        title = title_results[0].text

        # Get Application Date
        date_results = tree.xpath("//application-reference//date")
        if not date_results:
            stats["no_date"] += 1
            continue
        try:
            date = datetime.strptime(date_results[0].text, "%Y%m%d")
        except ValueError:
            # log.error(f"Date format incorrect: {date_results[0].text}")
            stats["no_date"] += 1
            continue

        # Get Inventors
        inventors = []
        for xpath in (
            "//us-parties//inventor//addressbook",
            "//parties/applicants/applicant[@app-type='applicant-inventor']/addressbook",
        ):
            inventors_results = tree.xpath(xpath)
            for inventor_result in inventors_results:
                fn_result = inventor_result.xpath("first-name")
                mn_result = inventor_result.xpath("middle-name")
                ln_result = inventor_result.xpath("last-name")
                if fn_result and ln_result:
                    fns = fn_result[0].text.split(" ")
                    mns = mn_result[0].text.split(" ") if mn_result else []
                    lns = ln_result[0].text.split(" ")
                    inventors.append(tuple([*fns, *mns, *lns]))
            if inventors:
                break  # dont include applicants if inventors are explicitly listed
        if not inventors:
            stats["no_inventors"] += 1
            continue

        # Get Assignee
        assignee = None
        for xpath in (
            "//us-parties/us-applicants/us-applicant[@applicant-authority-category='assignee']/addressbook/orgname",
            "//assignees/assignee/addressbook/orgname",
        ):
            result = tree.xpath(xpath)
            if result:
                assignee = result[0].text
                break

        # Get Abstract
        abstract_results = tree.xpath("//abstract/p")
        if not abstract_results:
            stats["no_abstract"] += 1
            continue
        abstract = "".join(abstract_results[0].itertext())

        patents.append(
            dict(
                id=document_id,
                title=title,
                application_date=date,
                abstract=abstract,
                inventors=tuple(inventors),
                assignee=assignee,
                zip_file=path,
                index_in_zip=idx_in_zip,
            )
        )
        stats["parsed"] += 1

    return patents, stats


def main(
    uspto_dir: Path = root / "data" / "uspto",
    patents_file: Path = root / "data" / "outputs" / "patents.pickle",  # list[dict]
    patents_index_file: Path = root
    / "data"
    / "outputs"
    / "patents_index.pickle",  # {patentID: byte position in patents.pickle}
    n_processes: int = 32,
    debug: bool = False,
):
    if debug:
        launch_debugger()

    if patents_file.exists():
        log.warning(f"Output file {patents_file} exists! Overwriting ...")
        patents_file.unlink()
    if patents_index_file.exists():
        log.warning(f"Output file {patents_index_file} exists! Overwriting ...")
        patents_index_file.unlink()

    patent_paths = sorted(list(uspto_dir.glob("*.zip")), key=lambda x: x.name)

    # only keep the newest revision per zip file
    mapping = defaultdict(list)
    for patent_path in patent_paths:
        name = patent_path.name.replace(".zip", "").split("_r")[0]
        mapping[name].append(patent_path)
    for name, files in mapping.items():
        if len(files) < 2:
            continue
        nums = [file.name.split("_r")[1][0] if "_r" in file.name else 0 for file in files]
        to_keep = np.argmax(nums)
        for i in range(len(files)):
            if i != to_keep:
                patent_paths.remove(files[i])

    stats = {
        "parsed": 0,
        "no_title": 0,
        "no_date": 0,
        "no_inventors": 0,
        "no_abstract": 0,
    }
    patents_index = {}

    try:
        with open(patents_file, "wb") as fp, Pool(n_processes) as p:
            for patents, stats_ in (
                pbar := tqdm(
                    p.imap_unordered(parse_zip, patent_paths),
                    total=len(patent_paths),
                    desc="Parsing Zip Files",
                )
            ):
                for k in stats:
                    stats[k] += stats_[k]

                pbar.set_postfix(stats)

                for patent in patents:
                    if patent["id"] in patents_index:
                        log.warning(
                            f"Patent ID is not unique: {patent['id']}. Overwriting index {patents_index[patent['id']]}"
                        )
                    patents_index[patent["id"]] = fp.tell()
                    pickle.dump(patent, fp, protocol=pickle.HIGHEST_PROTOCOL)

    except KeyboardInterrupt:
        log.info("Detected Keyboard interrupt. Saving index before terminating ...")

    except Exception as e:
        log.exception(f"'{repr(e)}' raised. Saving index before terminating ...")

    finally:
        with open(patents_index_file, "wb") as fp:
            pickle.dump(patents_index, fp, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    Fire(main)
