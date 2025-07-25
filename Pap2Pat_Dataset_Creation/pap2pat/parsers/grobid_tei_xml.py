import re
import unicodedata
from dataclasses import dataclass

# from collections import Counter
from pathlib import Path

import pdfplumber
from bs4 import BeautifulSoup, Tag

# from src.parsers.pubmed_nxml import normalize_title
from pap2pat.utils import get_logger

from .type import Section
from .uspto_xml import make_sections_hierarchical

log = get_logger()


@dataclass
class Font:
    font: str
    size: float
    is_bold: bool
    is_caps: bool

    @classmethod
    def match(cls, char: dict, title: str):
        is_bold = "bold" in char["fontname"].lower() or char["fontname"].lower()[-2:] == "-b"
        is_caps = title.isupper()
        return Font(char["fontname"], round(char["size"], 3), is_bold, is_caps)

    def __hash__(self):
        return hash((self.font, self.size, self.is_bold, self.is_caps))

    def __gt__(self, other: "Font"):
        return (
            self.size > other.size
            or self.is_caps
            and not other.is_caps
            or self.is_bold
            and not other.is_bold
        )


def most_common(l):
    counts = {f: 0 for f in set(l)}
    for f in l:
        counts[f] += 1
    return next(iter(sorted(counts.items(), key=lambda x: x[1], reverse=True)))[0]


def infer_levels_from_fonts(sections: list[tuple], pdf_path: Path) -> list[tuple]:
    with pdfplumber.open(pdf_path) as pdf:
        font_per_heading = {}
        for title, _, _ in sections:
            # ignore spaces in matching because pdfplumber doesnt do spaces well
            title_words = [re.escape(word) for word in title.split(" ")]
            matches = [match for page in pdf.pages for match in page.search(" ?".join(title_words))]

            # if we dont find matches (happens in dual column format when heading is more than one line)
            # incrementally make more words optional until we find a match (leave at least 2 words)
            while not matches and len(title_words) >= 2:
                title_words = title_words[:-1]
                matches = [
                    match for page in pdf.pages for match in page.search(" ?".join(title_words))
                ]

            # For every match, get the font that is most common among its characters
            font_per_match = [
                most_common([Font.match(char, title) for char in match["chars"]])
                for match in matches
            ]
            # Then use the "largest" font since headings are likely to appear somewhere in the text
            fonts = max(font_per_match) if font_per_match else None
            font_per_heading[title] = fonts

    all_fonts_sorted = list(sorted(set([f for f in font_per_heading.values() if f]), reverse=True))
    return [
        (
            title,
            all_fonts_sorted.index(font_per_heading[title]) + 1
            if font_per_heading[title] is not None
            else 999,
            text,
        )
        for title, _, text in sections
    ]


def get_section_text(soup: Tag, pdf_path: Path) -> tuple[list[Section], str]:
    has_numbering = False
    sections = []
    for div in soup.find_all("div"):
        head = div.head
        ps = div.find_all("p", recursive=False)
        if head is None:
            continue

        if "n" in head.attrs:
            level = len([s for s in head.attrs["n"].split(".") if s])
            sections.append((head.text, level, [p.text for p in ps if p.text]))
            has_numbering = True
        else:
            sections.append((head.text, 1, [p.text for p in ps if p.text]))

    if not has_numbering:
        sections = infer_levels_from_fonts(sections, pdf_path)
        hierarchy_source = "font"
    else:
        hierarchy_source = "numbering"

    return make_sections_hierarchical(sections), hierarchy_source


def normalize_string(s):
    s = s.replace("–", "-").replace("—", "-")
    s = unicodedata.normalize("NFKD", s)
    return s


def postprocess(sections: list[Section]) -> list[Section]:
    def remove_empty_sections(sections: list[Section]) -> list[Section]:
        return [
            {
                "title": sec["title"],
                "paragraphs": sec["paragraphs"],
                "subsections": remove_empty_sections(sec["subsections"]),
            }
            for sec in sections
            if sec["paragraphs"] or remove_empty_sections(sec["subsections"])
        ]

    sections = remove_empty_sections(sections)
    return sections


def parse_grobid(paper_dir: Path) -> tuple[str, list[Section], str]:
    soup = BeautifulSoup(paper_dir.joinpath("grobid.tei.xml").read_text(), "xml")
    abstract = soup.abstract.text.strip()  # type: ignore
    sections, hierarchy_source = get_section_text(soup, paper_dir.joinpath("paper.pdf"))
    sections = postprocess(sections)
    return abstract, sections, hierarchy_source
