from copy import deepcopy
import math
from dataclasses import dataclass, field

from src.dataset.prompt import Prompt
from src.utils.general import get_logger

log = get_logger(__file__)


@dataclass
class PatentChunk:
    content: dict
    level: int
    trace: list[str] = field(default_factory=list)
    prompt: Prompt = field(default_factory=Prompt)

    @property
    def num_characters(self) -> int:
        return self.content["num_characters"]

    def num_characters_recursive(self, sections: list[dict]) -> int:
        n = 0
        for section in sections:
            n += section["num_characters"]
            n += self.num_characters_recursive(section["subsections"])
        return n


def merge_sections_to_chunk(sections: list[tuple[int, list[str], dict]]) -> PatentChunk:
    def merge_recursive(sections: list[tuple[int, list[str], dict]]) -> list[dict]:
        if not sections:
            return []

        hierarchical_sections = []
        root_level = min(level for level, _, _ in sections)

        region = []
        for i in range(len(sections)):
            if sections[i][0] == root_level and region:
                region_root, rest = region[0], region[1:]
                rest = merge_recursive(rest)
                if rest:
                    subsections = [s[2] for s in rest]
                else:
                    subsections = []
                region_root[2]["subsections"] = subsections
                hierarchical_sections.append(region_root)
                region = []
            region.append(sections[i])

        if region:
            region_root, rest = region[0], region[1:]
            rest = merge_recursive(rest)
            if rest:
                subsections = [s[2] for s in rest]
            else:
                subsections = []
            region_root[2]["subsections"] = subsections
            hierarchical_sections.append(region_root)

        return hierarchical_sections

    hierarchical_sections = merge_recursive(sections)
    if len(hierarchical_sections) == 1:
        level, trace, section = hierarchical_sections[0]

    else:
        assert len(set(level for level, _, _ in hierarchical_sections)) == 1
        assert len(set(tuple(trace) for _, trace, _ in hierarchical_sections)) == 1
        level = hierarchical_sections[0][0] - 1
        trace = hierarchical_sections[0][1][:-1]
        section = {
            "title": hierarchical_sections[0][1][-1],
            "subsections": [section for _, _, section in hierarchical_sections],
            "paragraphs": [],
            "num_characters": 0,
            "outline": [],
        }

    chunk = PatentChunk(content=section, level=level, trace=trace)
    return chunk


def iter_sections(sections: list[dict], level=0, trace=None):
    if not trace:
        trace = []
    for sec in sections:
        yield level, trace, sec
        yield from iter_sections(sec["subsections"], level=level + 1, trace=trace + [sec["title"]])


def chunk_patent(description: dict, max_chunk_length: int) -> list[PatentChunk]:
    def total_chars(chunk):
        return sum(section["num_characters"] for _, _, section in chunk)

    chunks = []
    current_chunk = []

    for level, trace, section in iter_sections([deepcopy(description)]):
        # enforce that first section in chunk is always highest in tree
        if current_chunk and current_chunk[0][0] > level:
            chunks.append(current_chunk)
            current_chunk = []

        # new section fits in this chunk
        if total_chars(current_chunk) + section["num_characters"] <= max_chunk_length:
            current_chunk.append((level, trace, section))

        else:
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []

            # new section alone exceeds chunk size --> split up section
            if section["num_characters"] > max_chunk_length:
                n_chunks = math.ceil(section["num_characters"] / max_chunk_length)
                new_chunks = [[(level, trace, deepcopy(section))] for _ in range(n_chunks)]

                chars_per_chunk = math.ceil(section["num_characters"] / n_chunks)
                bullets_per_chunk = math.ceil(len(section["outline"]) / n_chunks)
                paras_per_chunk = math.ceil(len(section["paragraphs"]) / n_chunks)

                for i, chunk in enumerate(new_chunks):
                    chunk[0][2]["num_characters"] = chars_per_chunk
                    chunk[0][2]["outline"] = section["outline"][
                        i * bullets_per_chunk : (i + 1) * bullets_per_chunk
                    ]
                    chunk[0][2]["paragraphs"] = section["paragraphs"][
                        i * paras_per_chunk : (i + 1) * paras_per_chunk
                    ]

                chunks.extend(new_chunks)

            else:
                current_chunk.append((level, trace, section))

    if current_chunk:
        chunks.append(current_chunk)

    chunks = [merge_sections_to_chunk(chunk) for chunk in chunks]

    return chunks
