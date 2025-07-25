import json
from pathlib import Path
from typing import Generator

import pandas as pd
from nltk import sent_tokenize
from tqdm import tqdm

from .pubmed_nxml import parse_pmc
from .type import Document, Section


def parse_papers(paper_dirs: list[Path], matches: pd.DataFrame) -> dict[str, Document]:
    papers = {}

    status = {
        "source/pmc": 0,
        "source/grobid": 0,
        "source/none": 0,
        "content/abstract": 0,
        "content/sections": 0,
    }

    for paper_dir in (pbar := tqdm(paper_dirs, desc="Loading Papers")):
        abstract = matches[matches.paper == f"https://semopenalex.org/work/{paper_dir.name}"].iloc[
            0
        ]["abstract"]

        if paper_dir.joinpath("pmc").exists():
            paper = parse_pmc(paper_dir, abstract)
            status["source/pmc"] += 1

        elif paper_dir.joinpath("grobid.tei.xml").exists():
            # paper = parse_grobid(paper_dir)
            paper = None
            status["source/grobid"] += 1

        else:
            paper = None
            status["source/none"] += 1

        status["content/abstract"] += int(paper is not None and paper["abstract"] is not None)
        status["content/sections"] += int(paper is not None and paper["sections"] is not None)
        pbar.set_postfix(status)

        if not paper:
            continue

        paper_dir.joinpath("paper_content.json").write_text(json.dumps(paper))
        papers[paper_dir.name] = paper

    return papers


def iter_documents(matches, patents, papers):
    for patent_id, paper_id in matches[["patent", "paper"]].itertuples(index=False, name=None):
        paper_id = paper_id.split("/")[-1]
        yield patents[patent_id], papers[paper_id]


def iter_paragraphs(
    sections: list[Section], path: tuple = tuple()
) -> Generator[tuple[tuple, str], None, None]:
    for sec in sections:
        for i, para in enumerate(sec["paragraphs"]):
            yield tuple([*path, sec["title"], i]), para

        for path_, para in iter_paragraphs(sec["subsections"], path=tuple([*path, sec["title"]])):
            yield path_, para


def iter_sentences(
    sections: list[Section], path: tuple = tuple()
) -> Generator[tuple[tuple, str], None, None]:
    for sec in sections:
        for i, para in enumerate(sec["paragraphs"]):
            for j, sentence in enumerate(sent_tokenize(para)):
                yield tuple([*path, sec["title"], i, j]), sentence

        for path_, sentence in iter_sentences(
            sec["subsections"], path=tuple([*path, sec["title"]])
        ):
            yield path_, sentence


def iter_headings(sections: list[Section]) -> Generator[str, None, None]:
    for sec in sections:
        yield sec["title"]
        for subsec_title in iter_headings(sec["subsections"]):
            yield subsec_title
