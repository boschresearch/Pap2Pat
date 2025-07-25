import logging
import subprocess
import time
from pathlib import Path

import requests
from editdistance import eval as edit_distance
from rich.console import Console
from rich.logging import RichHandler
from rich.style import Style
from rich.table import Table


def get_logger(name=__name__) -> logging.Logger:
    logging.basicConfig(handlers=[RichHandler()], format="%(message)s")
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger


log = get_logger()


def launch_debugger(port=59531) -> None:
    import debugpy

    debugpy.listen(("0.0.0.0", port))
    log.info(f"debugpy debugger ready to connect on port {port}")
    debugpy.wait_for_client()


def print_pair(candidate: dict, patent: dict, file=None) -> None:
    console = Console(file=file, width=200)
    if file:
        console.is_jupyter = False  # rich is buggy with jupyter and files

    if "title_min" in candidate:
        title = "      ".join(
            [
                f"{k}={candidate[k]:.3f}"
                for k in (
                    "title_min",
                    "title_max",
                    "abstract_min",
                    "abstract_max",
                    "author_overlap",
                )
            ]
        )
    else:
        title = ""

    table = Table(title=title)

    table.add_column("")
    table.add_column("Patent")
    table.add_column("Paper")

    inventors_postprocess = lambda invs: ", ".join(" ".join(inv) for inv in invs)
    authors_postprocess = lambda auths: ", ".join(auths)
    date_postprocess = lambda date: date.strftime("%Y-%m-%d")
    styles = iter(
        [
            Style(color="white"),
            Style(color="cyan"),
            Style(color="magenta"),
            Style(color="green"),
            Style(color="white"),
        ]
    )
    for label, patent_key, patent_postprocess, paper_key, paper_postprocess in (
        ("ID", "id", None, "paper", None),
        ("Title", "title", None, "title", None),
        (
            "Authors / Inventors",
            "inventors",
            inventors_postprocess,
            "author_names",
            authors_postprocess,
        ),
        ("Date", "application_date", date_postprocess, "date", date_postprocess),
        ("Abstract", "abstract", None, "abstract", None),
    ):
        patent_value = (
            patent[patent_key] if not patent_postprocess else patent_postprocess(patent[patent_key])
        )
        paper_value = (
            candidate[paper_key]
            if not paper_postprocess
            else paper_postprocess(candidate[paper_key])
        )
        table.add_row(label, patent_value, paper_value, style=next(styles))

    console.print(table)


def get_num_lines(p: Path, blocksize=int(2e6)) -> int:
    c = 0
    with p.open("r") as fp:
        s = " "
        while len(s) > 0:
            s = fp.read(blocksize)
            c += s.count("\n")
    return c


def is_compute_node():
    try:
        hostname = subprocess.check_output("hostname").decode("utf-8")
        return "login" not in hostname
    except Exception as e:
        log.error(f"Failed to get hostname: {e}")
        return False


def get_model_info(api_base: str, max_startup_time: int) -> dict:
    start = time.time()
    while True:
        try:
            r = requests.get(f"{api_base}/get_model_info")
            r.raise_for_status()
            return r.json()

        except Exception as e:
            if time.time() - start > max_startup_time:
                raise e
            log.warning(
                f"Couldn't get model info: {e}. Retrying in 3 secs. max_startup_time: {max_startup_time}"
            )
            time.sleep(3)


def is_blacklisted_section(title: str, blacklisted_titles: list[str], min_dist: int = 3) -> bool:
    """Determine if a section should be thrown out by comparing it to all blacklisted titles using edit distance"""
    title = title.lower()
    if title in blacklisted_titles:
        return True
    for bl_title in blacklisted_titles:
        ed = edit_distance(title, bl_title)
        if ed <= min_dist:
            return True
    return False
