import re
from pathlib import Path

import pypandoc
from bs4 import BeautifulSoup, Tag

from pap2pat.utils import get_logger

from .grobid_tei_xml import postprocess
from .type import Section

log = get_logger()


def format_abstract(abstract: Tag) -> str | None:
    if abstract is None:
        return None
    abstract_str = ""
    for child in abstract.children:
        if child.name == "p":  # type: ignore
            abstract_str += f"\n{child.text}"
        elif child.name == "sec":  # type: ignore
            title = child.find("title")  # type: ignore
            abstract_str += f"\n{title.text}: "
            for p in child.find_all("p", recursive=False):  # type: ignore
                abstract_str += f"\n{p.text}"
    return abstract_str.strip()


def normalize_title(title: str) -> str:
    roman_numeral = r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
    r = re.search(rf"\s*(({roman_numeral}|\d+)(\s+|\s*\.\s*))?(.*)\s*", title)
    if r is None:
        log.warning(f"Title '{title}' could not be normalized")
        return title
    title_norm = r.groups()[-1].title()
    return title_norm


def get_section_text(root: Tag) -> list[Section]:
    r = []
    if root is None:
        return r
    sections = root.find_all("sec", recursive=False)
    for section in sections:
        title = section.title.text if section.title else ""
        section_result = {
            "title": normalize_title(title),
            "subsections": [],
            "paragraphs": [],
        }
        for para in section.find_all("p", recursive=False):
            section_result["paragraphs"].append(para.text.strip().replace("\n", " "))
        section_result["subsections"] = get_section_text(section)
        r.append(section_result)
    return r


def convert_formulas(soup: BeautifulSoup) -> BeautifulSoup:
    for formula in soup.find_all(["inline-formula", "disp-formula"]):
        latex = None
        mathml = formula.find("math")
        texmath = formula.find("tex-math")

        # MML --> Latex
        if mathml is not None:
            try:
                mathml_html = f"<html><body>{mathml.decode()}</body></html>"
                latex = pypandoc.convert_text(
                    mathml_html, to="latex", format="html", extra_args=["--mathml"]
                )
            except:  # noqa
                log.exception(f"Failed to convert MML formula:\n\n{formula.decode()}")

        if texmath is not None and latex is None:
            latexs = re.findall(
                r"\\begin\{document\}(.*)\\end\{document\}", texmath.text, re.DOTALL
            )
            if not latex:
                # malformed latex pattern in pmc
                latexs = re.findall(
                    r"\\begin\{document\}\s*\}\{\}(.*)\\end\{document\}",
                    texmath.text,
                    re.DOTALL,
                )

            try:
                latex = pypandoc.convert_text(
                    latexs[0].strip(), to="latex", format="tex"
                )  # normalize, e.g. $$...$$ to \[...\]
            except:  # noqa
                log.exception(f"Failed to convert latex formula:\n\n{formula.decode()}")
                latex = latexs[0].strip()

        if latex is None:
            latex = formula.text

        new_node = soup.new_tag("formula")
        new_node.string = latex
        formula.replace_with(new_node)

    return soup


def remove_tags(soup: BeautifulSoup, tags: list[str]) -> BeautifulSoup:
    for tag in soup.find_all(tags):
        tag.decompose()
    return soup


def parse_pmc(dir: Path) -> tuple[str, list[Section]]:
    nxml = list(dir.glob("pmc/*.nxml"))[0]
    soup = BeautifulSoup(nxml.read_text(), "xml")
    soup = remove_tags(soup, ["supplementary-material", "media"])
    soup = convert_formulas(soup)
    xml_abstract = format_abstract(soup.find("abstract"))  # type: ignore
    return xml_abstract, postprocess(get_section_text(soup.find("body")))  # type: ignore
