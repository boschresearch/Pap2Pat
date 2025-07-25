import re
import time
from functools import lru_cache, partial
from pathlib import Path

import pandas as pd
import requests
from fire import Fire
from pyrootutils import setup_root
from tqdm import tqdm
from utils import get_logger, launch_debugger, load_csv

log = get_logger(__file__)
root = setup_root(__file__)


license_mapping = {
    "http://arxiv.org/licenses/nonexclusive-distrib/1.0/": "arxiv-license",
    "http://creativecommons.org/licenses/by/3.0/": "cc-by",
    "http://creativecommons.org/licenses/by/4.0/": "cc-by",
    "http://creativecommons.org/licenses/by-sa/3.0/": "cc-by-sa",
    "http://creativecommons.org/licenses/by-sa/4.0/": "cc-by-sa",
    "http://creativecommons.org/licenses/by-nc-sa/3.0/": "cc-by-nc-sa",
    "http://creativecommons.org/licenses/by-nc-sa/4.0/": "cc-by-nc-sa",
    "http://creativecommons.org/licenses/by-nc-nd/3.0/": "cc-by-nc-nd",
    "http://creativecommons.org/licenses/by-nc-nd/4.0/": "cc-by-nc-nd",
    "http://creativecommons.org/publicdomain/zero/1.0/": "cc0",
}


@lru_cache(maxsize=1000)
def get_arxiv_license(arxiv_id: str) -> str | None:
    try:
        url = f"https://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:{arxiv_id}&metadataPrefix=arXivRaw"
        r = requests.get(url)

        if r.status_code != 200:
            log.warning(f"Error {r.status_code} in request: {r.text}")
            return None

        match = re.search(r"<license>(.*)</license>", r.text)

        if not match:
            # log.warning(f"License not found in response for {arxiv_id}")
            return None

        license = match.groups()[0]
        if license not in license_mapping:
            log.warning(f"License {license} is not mapped!")
        else:
            license = license_mapping[license]

    except Exception as e:
        log.error(f"Error during request: {repr(e)}")
        log.info("Waiting 20 seconds before retry")
        time.sleep(20)
        return get_arxiv_license(arxiv_id)
    return license


def main(
    matches_path: Path = root / "data" / "outputs" / "matches.csv",
    allowed_licenses: list[str] = ["cc-by", "cc0", "public-domain"],
    url_remove_patterns: list[str] = [r".*oaktrust\.library\.tamu\.edu.*"],
    debug: bool = False,
):
    if debug:
        launch_debugger()

    matches = load_csv(matches_path)

    pbar = tqdm(matches.iterrows(), total=len(matches))
    stats = {"requested": 0, "found": 0, "found_good": 0}
    for _, m in pbar:
        requested = False
        found = False
        found_good = False

        for j, url in enumerate(m["pdf_urls"]):
            if url is None or m["licenses"][j] is not None or "arxiv" not in url.lower():
                continue

            match = re.search(r"https?://arxiv.org/pdf/(\d+\.\d+)", url)
            if match is None:
                match = re.search(r"https?://arxiv.org/pdf/(.*/\d+)", url)
                if match is None:
                    log.warning(f"Malformed arxiv url: '{url}'")
                    continue

            arxiv_id = match.groups()[0]
            license = get_arxiv_license(arxiv_id)
            requested = True

            if license is not None:
                m["licenses"][j] = license
                found = True

                if license in allowed_licenses:
                    found_good = True

                break

        stats["requested"] += int(requested)
        stats["found"] += int(found)
        stats["found_good"] += int(found_good)

        pbar.set_postfix(stats)

    matches_with_license = matches.apply(
        partial(
            filter_licenses,
            allowed_licenses=allowed_licenses,
            url_remove_patterns=url_remove_patterns,
        ),
        axis=1,
    )
    matches_with_license = matches_with_license[~matches_with_license.licenses.isna()]
    log.info(f"{len(matches_with_license)} matches with permissive license and pdf url left!")
    out_path = matches_path.parent / "matches_with_license.csv"
    log.info(f"Saving to {out_path}")
    matches_with_license.to_csv(out_path, sep=";", index=False)


def filter_licenses(
    row: pd.Series, allowed_licenses: list[str], url_remove_patterns: list[str]
) -> pd.Series:
    l, p = [], []  # noqa: E741
    for license, pdf_url in zip(row["licenses"], row["pdf_urls"]):
        if license in allowed_licenses and pdf_url is not None:
            if any(re.match(pattern, pdf_url) for pattern in url_remove_patterns):
                continue

            l.append(license)
            p.append(pdf_url)

    if l and p:
        row["licenses"], row["pdf_urls"] = l, p
    else:
        row["licenses"], row["pdf_urls"] = None, None

    return row


if __name__ == "__main__":
    Fire(main)
