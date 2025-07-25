import re
from dataclasses import dataclass

import pypandoc
import sglang as sgl
from lxml import etree as ET
from pyrootutils import setup_root

from pap2pat.utils import get_logger

from .type import Section

log = get_logger(__file__)
root = setup_root(__file__)


RELEVANT_TAGS = (
    "p",
    "b",
    "claim",
    "claim-text",
    "claim-ref",
    "abstract",
    "i",
    "heading",
    "sub",
    "sup",
    "figref",
    "latex",
    "ol",
    "ul",
    "li",
    "in-line-formulae",
    "md",
    "span",
)


def get_text(node):
    if node.tag in RELEVANT_TAGS:
        text = node.text or ""
        for child in node:
            text += get_text(child)
            if child.tail:
                text += child.tail
        return text
    return ""


@dataclass
class Numbering:
    path: list[int]

    @staticmethod
    def from_str(s):
        return Numbering([int(x) for x in s.strip().split(".") if x])

    def next_choices(self, title: str):
        choices = []
        # same depth or up
        for i in list(range(len(self.path)))[::-1]:
            choices.append(Numbering([*self.path[:i], self.path[i] + 1]))
        # deeper
        choices.append(Numbering([*self.path, 1]))
        # filter out invalid numberings
        choices = [
            c.str
            for c in choices
            if (
                all(x > 0 for x in c.path)  # no zeros or negative numbers
                # and not (title.isupper() and len(c.path) > 2)  # no caps titles deeper than level 2
                and not (
                    len(c.path) == 1 and title != "DESCRIPTION"
                )  # description is the only level 1 heading
            )
        ]
        return choices

    @property
    def str(self):
        return ".".join([str(x) for x in self.path]) + "."


@sgl.function
def fix_section_levels(s, sections: list[tuple[str, int, list[str]]]):
    task_desc = (
        "Due to a mistake in our IT system, the heading hierarchies in our patent documents were corrupted. "  # type: ignore
        "Your task is to fix the levels. The main clues are the titles. "
        "On the top level, there is ALWAYS just one heading that contains all other sections: 'DESCRIPTION'. "
        "I will provide you the headings as a flat list. "
        "You will infer the correct levels and format the corrected hierarchy using numbered headings (1., 1.1., 1.1.1., ...). "
        "You will put the final hierarchy in a markdown block (started by '```md'). "
        "If you have any more questions, feel free to ask before we begin. "
    )

    # User prompt
    s += sgl.user_begin()
    s += f"{task_desc}\n\n```md\n"
    for i, (title, _, _) in enumerate(sections):
        nl = "\n\n" if i < len(sections) - 1 else ""
        s += f"- {title}{nl}"
    s += "\n```"
    s += sgl.user_end()

    # Assistant response
    s += sgl.assistant_begin()
    # s += sgl.gen("reasoning", max_tokens=500, stop="```")
    s += "```md\n"
    for i, (title, _, _) in enumerate(sections):
        last_numbering = Numbering.from_str(s["numbering"]) if i > 0 else Numbering.from_str("0.")
        choices = last_numbering.next_choices(title)
        s += sgl.select("numbering", choices=choices)
        nl = "\n\n" if i < len(sections) - 1 else ""
        s += f" {title}{nl}"
    s += "\n```"
    s += sgl.user_end()


def convert_lists_to_md(root):
    lists = root.xpath("//ol | //ul")
    for lst in lists:
        html_list = ET.tostring(lst, encoding="unicode", method="html")  # type: ignore
        md = pypandoc.convert_text(html_list, to="gfm-raw_html", format="html").strip()
        md_node = ET.Element("md", None, None)
        md_node.text = f"\n\n{md}\n\n"
        lst.getparent().replace(lst, md_node)
    return root


def make_sections_hierarchical(
    sections: list[tuple[str, int, list[str]]], fix_patent_hierarchy: bool = False
) -> list[Section]:
    if not sections:
        return []

    if fix_patent_hierarchy:
        # run llm to infer hierarchy
        sections_fixed = []
        state = fix_section_levels.run(sections)
        msg = state.messages()[-1]["content"].strip()
        md_block = re.findall(r"```md(.*)```", msg, re.DOTALL)[-1].strip()
        headings = re.findall(r"((\d+\.)+) (.*)", md_block)
        assert len(sections) == len(headings)
        for i in range(len(sections)):
            numbering, _, title_sgl = headings[i]
            assert sections[i][0] == title_sgl
            sections_fixed.append((title_sgl, len(numbering.replace(".", "")), sections[i][2]))
        sections = sections_fixed

    hierarchical_sections = []
    root_level = min(level for _, level, _ in sections)

    region = []
    for i in range(len(sections)):
        if sections[i][1] == root_level and region:
            region_root, rest = region[0], region[1:]
            hierarchical_sections.append(
                {
                    "title": region_root[0],
                    "paragraphs": region_root[2],
                    "subsections": make_sections_hierarchical(rest),
                }
            )
            region = []
        region.append(sections[i])

    if region:
        region_root, rest = region[0], region[1:]
        hierarchical_sections.append(
            {
                "title": region_root[0],
                "paragraphs": region_root[2],
                "subsections": make_sections_hierarchical(rest),
            }
        )

    return hierarchical_sections


def remove_empty_sections_and_paragraphs(
    sections_hierarchical: list[Section],
) -> list[Section]:
    cleaned_sections = []
    for section in sections_hierarchical:
        cleaned_section = {
            "title": section["title"],
            "paragraphs": [p.strip() for p in section["paragraphs"] if p.strip()],
            "subsections": remove_empty_sections_and_paragraphs(section["subsections"]),
        }

        if cleaned_section["paragraphs"] or cleaned_section["subsections"]:
            cleaned_sections.append(cleaned_section)

    return cleaned_sections


def convert_mathml_to_latex(tree: ET._Element):
    maths = tree.findall(".//maths", [])
    for math in maths:
        mathml_str = ET.tostring(math, encoding="unicode", method="xml")  # type: ignore
        mathml_html = f"<html><body>{mathml_str}</body></html>"
        latex = pypandoc.convert_text(
            mathml_html, to="latex", format="html", extra_args=["--mathml"]
        )
        latex_elem = ET.Element("latex")  # type: ignore
        latex_elem.text = latex
        math.getparent().replace(math, latex_elem)
    return tree


def limit_section_depth(section: Section, level=1, max_level=3) -> Section:
    """Limit the section depth to a specified level.
    Move all content from deeper sections into the paragraphs of the parent with max_level depth.
    Also include the subsection heading as **title** as paragraph."""
    if level == max_level:
        additional_paragraphs = [
            para
            for subsec in section["subsections"]
            for para in limit_section_depth(subsec, level + 1, max_level)
        ]
        section["subsections"] = []
        section["paragraphs"] = [*section["paragraphs"], *additional_paragraphs]
        return section

    elif level < max_level:
        section["subsections"] = [
            limit_section_depth(subsec, level + 1, max_level) for subsec in section["subsections"]
        ]
        return section

    elif level > max_level:
        paras = [f"**{section['title']}**", *section["paragraphs"]]
        for subsec in section["subsections"]:
            paras.extend(limit_section_depth(subsec, level + 1, max_level))
        return paras  # type: ignore

    raise Exception  # only for type checker, cannot be reached


def parse_patent_xml(xml: str, patent_id: str) -> tuple[str, list[Section]]:
    xml = xml.replace(
        '<?in-line-formulae description="In-line Formulae" end="lead"?>',
        "<in-line-formulae>",
    )
    xml = xml.replace(
        '<?in-line-formulae description="In-line Formulae" end="tail"?>',
        "</in-line-formulae>",
    )

    tree = ET.fromstring(xml)  # type: ignore
    tree = convert_mathml_to_latex(tree)
    tree = convert_lists_to_md(tree)

    # Check that patent_id is correct
    document_id = tree.xpath("//publication-reference/document-id")[0]
    patent_id_xml = document_id.xpath("country")[0].text + document_id.xpath("doc-number")[0].text
    assert patent_id == patent_id_xml

    abstract = get_text(tree.find("abstract")).strip()  # type: ignore
    all_sections = []

    # Read all description sections into flat format
    description = tree.find("description")  # type: ignore
    heading = None
    level = None
    paras = []
    last_section_had_level = True
    sections: list[tuple[str, int, list[str]]] = [("DESCRIPTION", 0, [])]
    for child in description:
        if (
            child.tag == "heading"
            or (child.tag == "p" and child.attrib["id"].lower().startswith("h"))
            or (child.tag == "p" and child.attrib.get("num", "").startswith("heading"))
        ):
            if heading is not None and level is not None:
                sections.append((heading, level, paras))

            heading = get_text(child).strip()

            if "level" in child.attrib:
                level = int(child.attrib["level"])
                last_section_had_level = True

            # for headings that dont have a level attribute we assign one level deeper than the previous
            elif last_section_had_level:
                level = sections[-1][1] + 1
                last_section_had_level = False

            # unless the previous heading was also without a level, then we assign the same level as the previous
            else:
                level = sections[-1][1]
                last_section_had_level = False

            paras = []

        elif child.tag == "p":
            para_text = get_text(child).strip()
            if heading is None:  # if no heading, put paragraph to top level description section
                sections[0][2].append(para_text)
            else:
                paras.append(para_text)

    if paras and heading and level:
        sections.append((heading, level, paras))

    # Transform flat section format into hierarchical format with limited depth
    sections_hierarchical = make_sections_hierarchical(sections, fix_patent_hierarchy=True)
    sections_hierarchical = remove_empty_sections_and_paragraphs(sections_hierarchical)
    sections_hierarchical = [limit_section_depth(sec) for sec in sections_hierarchical]

    all_sections.extend(sections_hierarchical)

    # Read all claims
    claims = []
    for claim in tree.xpath("//claim"):
        claim_text = get_text(claim).strip()
        claims.append(claim_text)
    all_sections.append({"title": "CLAIMS", "paragraphs": claims, "subsections": []})

    return abstract, all_sections
