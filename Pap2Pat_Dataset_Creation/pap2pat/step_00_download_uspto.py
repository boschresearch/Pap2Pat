import multiprocessing
import urllib.request
from pathlib import Path
from typing import Tuple

import requests
from fire import Fire
from lxml import etree as etree_lxml
from utils import get_logger

log = get_logger()

multiprocessing.set_start_method("fork")


class BytesMismatchException(Exception):
    pass


def download_zip_unpacked(args, **kwargs):
    return download_zip(*args, **kwargs)


def download_zip(url: str, file_size: int, out_file: Path, repeat_count=0) -> Tuple[Path, int]:
    try:
        if out_file.exists():
            status = 1
        else:
            status = 0
            r = requests.get(url, stream=True, allow_redirects=True)
            if r.status_code != 200:
                r.raise_for_status()

            urllib.request.urlretrieve(url, out_file)

        result_file_size = out_file.stat().st_size
        if result_file_size != file_size:
            log.warning(
                f"File {out_file} was {result_file_size} Bytes, expected {file_size} Bytes. Retrying ..."
            )
            out_file.unlink()
            raise BytesMismatchException(
                f"File {out_file} was {result_file_size} Bytes, expected {file_size} Bytes."
            )

    except Exception as e:
        status = 2
        if not isinstance(e, BytesMismatchException):
            log.warning(f"Exception for '{out_file.name}': {repr(e)}. Retrying ...")

        if repeat_count < 1:
            download_zip(url, file_size, out_file, repeat_count + 1)

    return out_file, status


def main(years: list[int] = list(range(2005, 2025)), n_processes: int = 10):
    year_links = [
        f"https://bulkdata.uspto.gov/data/patent/application/redbook/fulltext/{year}/"
        for year in years
    ]

    for year_idx, (year, year_link) in enumerate(zip(years, year_links)):
        overview_response = requests.get(year_link)
        overview_response.raise_for_status()
        tree = etree_lxml.fromstring(overview_response.text, etree_lxml.HTMLParser())

        week_filenames = []
        file_sizes = []
        rows = tree.xpath("//table/tr")
        for row in rows:
            entries = row.xpath("td")
            if len(entries) != 3:
                continue
            filename = entries[0].xpath("a[starts-with(text(), 'ipa')]")
            if not filename:
                continue
            filename = filename[0].text
            file_size = entries[1].text
            if filename and file_size and "ipa050113" not in filename:
                week_filenames.append(filename)
                file_sizes.append(int(file_size))

        urls = [f"{year_link}/{week_filename}" for week_filename in week_filenames]
        out_files = [Path(f"data/uspto/{week_filename}") for week_filename in week_filenames]
        log.info(
            f"(Year {year_idx + 1} / {len(year_links)}) Downloading data for year {year} in {len(urls)} files using {n_processes} processes"
        )
        done = 0

        with multiprocessing.Pool(n_processes) as p:
            for f, status in p.imap_unordered(
                download_zip_unpacked, zip(urls, file_sizes, out_files)
            ):
                if status == 0:
                    log.info(f"\t(File {done + 1} / {len(urls)}): Downloaded {f}")
                elif status == 1:
                    log.info(f"\t(File {done + 1} / {len(urls)}): Skipped {f}")
                elif status == 2:
                    log.error(f"\t(File {done + 1} / {len(urls)}): Failed {f}")
                done += 1


if __name__ == "__main__":
    Fire(main)
