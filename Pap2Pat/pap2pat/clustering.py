import re
from dataclasses import dataclass

from editdistance import eval as edit_distance


cluster_prototypes = {
    "Background": [
        "BACKGROUND",
        "BACKGROUND OF THE INVENTION",
        "BACKGROUND ART",
        "Description of Related Art",
        "RELATED ART",
        "Related Technology",
        "PRIOR ART",
        "Discussion of Related Art",
        "Description of the Related Art",
        "BACKGROUND OF THE INVENTION AND PRIOR ART",
        "FIELD AND BACKGROUND OF THE INVENTION",
        "BACKGROUND OF THE DISCLOSURE",
        "BACKGROUND OF RELATED ART",
        "BACKGROUND PRIOR ART OF THE INVENTION",
        "BACKGROUND INFORMATION",
        "BACKGROUND AND OVERVIEW OF THE INVENTION",
        "Description of the Prior Art",
    ],
    "Summary": ["SUMMARY", "BRIEF SUMMARY"],
    "Detailed Description": [
        "Detailed Description",
        "DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS",
        "DETAILED DESCRIPTION OF PREFERRED EMBODIMENTS",
        "DETAILED DESCRIPTION OF ILLUSTRATED EMBODIMENTS",
        "DETAILED DESCRIPTION OF ILLUSTRATIVE EMBODIMENTS",
        "DETAILED DESCRIPTION OF THIS DISCLOSURE",
        "DETAILED DESCRIPTION OF CERTAIN EMBODIMENTS",
        "DETAILED DESCRIPTION OF CERTAIN PREFERRED EMBODIMENTS",
        "DETAILED DESCRIPTION AND FURTHER OPTIONAL FEATURES OF THE INVENTION",
        "DETAILED DESCRIPTION OF THE EXAMPLE EMBODIMENTS",
        "DETAILED DESCRIPTION OF THE PRESENT INVENTION",
        "DETAILED DESCRIPTION OF SOME EMBODIMENTS",
        "DETAILED DESCRIPTION OF SEVERAL EMBODIMENTS",
        "DETAILED DESCRIPTION OF THE INVENTION",
        "DETAILED DESCRIPTION OF SPECIFIC EMBODIMENTS",
        "DETAILED DESCRIPTION OF THE ILLUSTRATED EMBODIMENTS",
        "DETAILED DESCRIPTION OF EXEMPLARY EMBODIMENTS",
        "DETAILED DESCRIPTION OF THE MOST PREFERRED EMBODIMENT",
        "DETAILED DESCRIPTION OF CERTAIN EMBODIMENTS OF THE INVENTION",
        "DESCRIPTION OF THE INVENTION",
    ],
}


@dataclass
class ClusteredPatent:
    complete_gen: str
    complete_ref: str
    headings: list[str]
    gen_sections: dict[str, str]
    ref_sections: dict[str, str]
    clusters: dict[str, list[str]]


def matches_cluster(heading: str, prototypes: list[str]) -> bool:
    def remove(s, r):
        s = s.lower()
        for w in r:
            s = s.replace(w.lower(), "")
        return s.strip()

    for prototype in prototypes:
        for heading_variant in (
            heading.lower().strip(),
            remove(
                heading,
                ("of", "the", "invention", "disclosure", "embodiments", "embodiment"),
            ),
        ):
            if edit_distance(heading_variant, prototype.lower()) <= 3:
                return True

    return False


def split_doc_and_cluster_sections(generated: str, reference: str) -> ClusteredPatent:
    all_headings = re.findall(r"\n\n(#{1,2} [^\n]*)", "\n\n" + reference)

    # Split generated document
    heading_locations = [generated.find(heading) for heading in all_headings]
    heading_slices = [
        (
            slice(heading_locations[i] + len(all_headings[i]), heading_locations[i + 1])
            if i + 1 < len(heading_locations)
            else slice(heading_locations[i] + len(all_headings[i]), None)
        )
        for i in range(len(heading_locations))
    ]
    gen_sections = {
        heading: generated[slice].strip() for heading, slice in zip(all_headings, heading_slices)
    }

    # Split reference document
    heading_locations = [reference.find(heading) for heading in all_headings]
    heading_slices = [
        (
            slice(heading_locations[i] + len(all_headings[i]), heading_locations[i + 1])
            if i + 1 < len(heading_locations)
            else slice(heading_locations[i] + len(all_headings[i]), None)
        )
        for i in range(len(heading_locations))
    ]
    ref_sections = {
        heading: reference[slice].strip() for heading, slice in zip(all_headings, heading_slices)
    }

    # Cluster headings
    clusters = {
        cluster: [heading for heading in all_headings if matches_cluster(heading, prototypes)]
        for cluster, prototypes in cluster_prototypes.items()
    }

    return ClusteredPatent(generated, reference, all_headings, gen_sections, ref_sections, clusters)
