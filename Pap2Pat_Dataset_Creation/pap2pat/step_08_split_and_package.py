import json
import random
import re
from datetime import datetime
from pathlib import Path

import sglang as sgl
from hydralette import Config
from lxml import etree as ET
from pyrootutils import setup_root
from tqdm import tqdm

from pap2pat.utils import (
    get_logger,
    launch_debugger,
    load_csv,
    load_pickle_by_id,
    is_blacklisted_section,
)
from pap2pat.parsers.reference_numerals import extract_reference_numerals

root = setup_root(__file__)
log = get_logger(__name__)
DATE_FORMAT = "%Y-%m-%d"

cfg = Config(
    papers_dir=root / "data" / "papers",
    matches_path=root / "data" / "outputs" / "matches_with_license.csv",
    patents_path=root / "data" / "outputs" / "patents.pickle",
    patents_index_path=root / "data" / "outputs" / "patents_index.pickle",
    title_blacklist=[
        t.lower().strip()
        for t in root.joinpath("pap2pat/title_blacklist.txt").read_text().split("\n")
    ],
    required_files=[
        "match_meta.json",
        "patent.json",
        "paper.json",
        "patent_summary_empty.md",
        "patent_summary_500.md",
        "patent_summary_1000.md",
        "patent_summary_2000.md",
    ],
    target_dir=root / "data" / "dist" / "ppp-v4",
    cutoff_date=datetime(year=2024, month=1, day=1),
    n_train=1000,
    n_test=500,
    seed=1337,
    sgl_url="http://localhost:59532",
    debug=False,
)


def get_publication_date(xml_path: Path) -> str:
    """We didn't extract the publication date in the beginning, but its relevant for the time-based test set."""
    tree = ET.fromstring(xml_path.read_text(), None)
    date_results = tree.xpath("//publication-reference//date")
    assert len(date_results) == 1, f"Found {len(date_results)} entries for the publication date"
    date = datetime.strptime(date_results[0].text, "%Y%m%d")
    return date.strftime("%Y-%m-%d")


def remove_duplicate(abstract: str, min_n: int = 80):
    start = abstract[:min_n]
    second_start_idx = abstract.find(start, min_n)
    if second_start_idx > 0:
        abstract = abstract[:second_start_idx].strip()
    return abstract


def iter_sections(secs: list[dict], level=1):
    for sec in secs:
        yield level, sec
        yield from iter_sections(sec["subsections"], level=level + 1)


def merge_outline_into_json(description: dict, outline: str, outline_name: str):
    outline_parts = re.findall(r"(#+) ([^\n]+)\n\n((-[^\n]+\n)*)", outline + "\n\n", re.MULTILINE)
    all_sections = list(iter_sections([description]))
    assert len(outline_parts) == len(all_sections)

    for outline_part, (section_level, section) in zip(outline_parts, all_sections):
        hashes, heading, bullets, _ = outline_part
        outline_level = len(hashes)
        bullets = [bullet[1:].strip() for bullet in bullets.split("\n") if bullet.strip()]
        assert section["title"] == heading
        assert outline_level == section_level
        section[f"outline_{outline_name}"] = bullets

    return description


def add_character_lengths(description: dict) -> dict:
    for _, section in iter_sections([description]):
        section["num_characters"] = len("\n\n".join(section["paragraphs"]))
    return description


def remove_metadata_sections(description: dict, title_blacklist: list[str]):
    def _remove_metadata_sections(sections: list[dict]):
        new_sections = []
        for sec in sections:
            if is_blacklisted_section(sec["title"], title_blacklist):
                continue
            sec["subsections"] = _remove_metadata_sections(sec["subsections"])
            if sec["subsections"] or sec["paragraphs"]:
                new_sections.append(sec)
        return new_sections

    return _remove_metadata_sections([description])[0]


def get_markdown_outline(sections: list[dict], outline_name: str) -> str:
    s = ""
    for level, section in iter_sections(sections):
        s += f"{'#'*level} {section['title']}\n\n"
        outline_bullets = section[f"outline_{outline_name}"] if outline_name != "empty" else []
        for bullet in outline_bullets:
            s += f"- {bullet}\n"
        if outline_bullets:
            s += "\n"
    return s


def get_markdown_fulltext(sections: list[dict]) -> str:
    s = ""
    for level, section in iter_sections(sections):
        s += f"{'#'*level} {section['title']}\n\n"
        s += "\n\n".join(section["paragraphs"])
        if section["paragraphs"]:
            s += "\n\n"
    return s


def main(cfg):
    if cfg.debug:
        launch_debugger()

    papers_dir: Path = cfg.papers_dir
    target_dir: Path = cfg.target_dir
    if target_dir.exists():
        log.error(f"Target dir '{target_dir}' exists. Aborting ...")
        raise SystemExit

    ###########################################
    #             Load metadata
    ###########################################
    # region
    log.info("Loading sample metadata")
    matches = load_csv(cfg.matches_path)
    stats = {"not_all_files": 0, "success": 0}
    samples = {}
    pbar = tqdm(total=len(matches), desc="Loading files")
    for _, row in matches.iterrows():
        paper_id = row.paper.split("/")[-1]
        paper_dir = papers_dir / paper_id

        if not all(paper_dir.joinpath(file).exists() for file in cfg.required_files):
            stats["not_all_files"] += 1

        else:
            patent = load_pickle_by_id(row.patent, cfg.patents_path, cfg.patents_index_path)
            sample_id = f"{paper_id}-{row.patent}"
            sample = {
                "id": sample_id,
                "paper": {
                    "id": paper_id,
                    "author_ids": row.authors,
                    "authors": row.author_names,
                    "doi": row.doi,
                    "title": row.title,
                    "date": row.date.strftime(DATE_FORMAT),
                    "abstract": remove_duplicate(row.abstract),
                    "locations": row.locations,
                    "urls": row.urls,
                    "pdf_urls": [
                        {"url": url, "license": license}
                        for url, license in zip(row.pdf_urls, row.licenses)
                    ],
                },
                "patent": {
                    "id": patent["id"],
                    "title": patent["title"],
                    "application_date": patent["application_date"].strftime(DATE_FORMAT),
                    "publication_date": get_publication_date(paper_dir / "patent.xml"),
                    "inventors": patent["inventors"],
                    "abstract": patent["abstract"],
                    "assignee": patent["assignee"],
                },
                "match_metrics": {
                    "author_overlap": row.author_overlap,
                    "title_min": row.title_min,
                    "title_max": row.title_max,
                    "abstract_min": row.abstract_min,
                    "abstract_max": row.abstract_max,
                },
            }
            samples[sample_id] = sample
            stats["success"] += 1

        pbar.update(1)
        pbar.set_postfix(stats)
    log.info(f"Found {len(samples)} complete samples")

    # endregion

    ###########################################
    #          Create Dataset Splits
    ###########################################
    # region
    log.info(f"Creating dataset splits with {cfg.n_train=} and {cfg.n_test=}")
    random.seed(cfg.seed)
    # Splits
    # non-contaminated-test split
    time_samples_ids = [
        id
        for id, sample in samples.items()
        if datetime.strptime(sample["patent"]["publication_date"], DATE_FORMAT) >= cfg.cutoff_date
    ]
    log.info(
        f"Found {len(time_samples_ids)} ({len(time_samples_ids) / len(samples) * 100:.2f}%) samples published after {cfg.cutoff_date.strftime(DATE_FORMAT)}"
    )

    # train split
    assigned_ids = [i for ids in (time_samples_ids,) for i in ids]
    train_samples_ids = random.sample(
        [id for id in samples.keys() if id not in assigned_ids], cfg.n_train
    )

    # test split
    assigned_ids = [i for ids in (time_samples_ids, train_samples_ids) for i in ids]
    test_samples_ids = random.sample(
        [id for id in samples.keys() if id not in assigned_ids], cfg.n_test
    )

    # val split
    assigned_ids = [
        i for ids in (time_samples_ids, train_samples_ids, test_samples_ids) for i in ids
    ]
    val_samples_ids = [id for id in samples.keys() if id not in assigned_ids]

    n_samples = len(samples)
    log.info(
        f"Split distribution:"
        f"\n\ttrain: {len(train_samples_ids)} ({len(train_samples_ids) / n_samples * 100:.2f}%)"
        f"\n\tval: {len(val_samples_ids)} ({len(val_samples_ids) / n_samples * 100:.2f}%)"
        f"\n\ttest: {len(test_samples_ids)} ({len(test_samples_ids) / n_samples * 100:.2f}%)"
        f"\n\tnon-contaminated-test: {len(time_samples_ids)} ({len(time_samples_ids) / n_samples * 100:.2f}%)"
    )

    # endregion

    ###########################################
    #          Copy files to dist dir
    ###########################################
    # region
    log.info(f"Creating dist dir at '{target_dir}")
    target_dir.mkdir(parents=True)
    metadata = {
        "splits": {
            "train": train_samples_ids,
            "val": val_samples_ids,
            "test": test_samples_ids,
            "non-contaminated-test": time_samples_ids,
        },
        "samples": samples,
    }
    target_dir.joinpath("metadata.json").write_text(json.dumps(metadata, indent=4))
    for sample_id, sample in tqdm(
        samples.items(), desc="Postprocessing and copying files", total=len(samples)
    ):
        old_paper_dir: Path = papers_dir / sample["paper"]["id"]
        new_paper_dir: Path = target_dir / sample_id
        new_paper_dir.mkdir()

        # remove duplicated abstracts in paper.json
        paper = json.loads(old_paper_dir.joinpath("paper.json").read_text())
        paper["abstract"] = remove_duplicate(paper["abstract"])

        # load patent and outlines
        patent = json.loads(old_paper_dir.joinpath("patent.json").read_text())
        long_outline = old_paper_dir.joinpath("patent_summary_500.md").read_text()
        medium_outline = old_paper_dir.joinpath("patent_summary_1000.md").read_text()
        short_outline = old_paper_dir.joinpath("patent_summary_2000.md").read_text()

        # merge outlines into patent json
        for outline_name, outline in (
            ("long", long_outline),
            ("medium", medium_outline),
            ("short", short_outline),
        ):
            patent["sections"][0] = merge_outline_into_json(
                patent["sections"][0], outline, outline_name
            )

        # remove metadata sections
        description = remove_metadata_sections(patent["sections"][0], cfg.title_blacklist)

        # set description as only section and claims as separate field
        claims = patent["sections"][1]["paragraphs"]
        patent["sections"] = [description]
        patent["claims"] = claims

        # save modified patent.json and outlines without metadata sections
        new_paper_dir.joinpath("patent.json").write_text(json.dumps(patent, indent=4))
        new_paper_dir.joinpath("patent.md").write_text(get_markdown_fulltext(patent["sections"]))
        new_paper_dir.joinpath("paper.json").write_text(json.dumps(paper, indent=4))
        new_paper_dir.joinpath("paper.md").write_text(get_markdown_fulltext(paper["sections"]))
        new_paper_dir.joinpath("patent_outline_long.md").write_text(
            get_markdown_outline(patent["sections"], "long")
        )
        new_paper_dir.joinpath("patent_outline_medium.md").write_text(
            get_markdown_outline(patent["sections"], "medium")
        )
        new_paper_dir.joinpath("patent_outline_short.md").write_text(
            get_markdown_outline(patent["sections"], "short")
        )
        new_paper_dir.joinpath("patent_outline_empty.md").write_text(
            get_markdown_outline(patent["sections"], "empty")
        )
    # endregion


    ####################################################
    # Extract reference numerals and figure captions
    ####################################################
    # region
    log.info("Extracting figure numbers and reference numerals")
    sgl.set_default_backend(sgl.RuntimeEndpoint(cfg.sgl_url))

    files = list(target_dir.glob("**/patent.md"))
    args = [
        {"patent": patent.read_text()}
        for patent in files
    ]
    all_reference_numerals = extract_reference_numerals.run_batch(args, progress_bar=True, num_threads=32)

    for patent_md_path, reference_numerals in zip(files, all_reference_numerals):
        patent_json_path = patent_md_path.parent / "patent.json"
        patent_json = json.loads(patent_json_path.read_text())
        patent_json["reference_numerals"] = reference_numerals
        patent_json_path.write_text(json.dumps(patent_json))
    # endregion

if __name__ == "__main__":
    cfg.apply()
    main(cfg)
