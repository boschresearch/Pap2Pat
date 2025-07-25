import logging
import random
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import debugpy
import numpy as np
import torch
from pyrootutils import setup_root
from rich.logging import RichHandler

root = setup_root(__file__)


def get_logger(name=__name__) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = RichHandler()
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
    return logger


log = get_logger()


def launch_debugger(port=59531) -> None:
    debugpy.listen(("0.0.0.0", port))
    log.info(f"debugpy debugger ready to connect on port {port}")
    debugpy.wait_for_client()


def is_compute_node():
    try:
        hostname = subprocess.check_output("hostname").decode("utf-8")
        return "login" not in hostname
    except Exception as e:
        log.error(f"Failed to get hostname: {e}")
        return False


def get_run_dir(jobname: str, base_run_dir: Path = root / "outputs" / "runs") -> Path:
    jobname = jobname.replace("/", "-")
    run_dir = base_run_dir / jobname
    if run_dir.exists():
        run_dir = base_run_dir / f"{jobname}-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
    return run_dir


def set_seed(seed: int | None):
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)


def format_patent(patent_sections: list[dict], level=0):
    s = ""
    for section in patent_sections:
        s += f"\n\n{'#'*(level+1)} {section['title']}"
        if section["paragraphs"]:
            s += "\n\n"
            s += "\n\n".join(section["paragraphs"])
        s += format_patent(section["subsections"], level=level + 1)
    return s


class redirect_stdout_stderr:
    def __init__(self, file_object):
        self.file_object = file_object
        self.stdout_original = sys.stdout
        self.stderr_original = sys.stderr

    def __enter__(self):
        sys.stdout = self
        sys.stderr = self
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.stdout_original
        sys.stderr = self.stderr_original

    def write(self, data):
        self.file_object.write(data)
        self.stdout_original.write(data)
        self.file_object.flush()
        self.stdout_original.flush()

    def flush(self):
        self.file_object.flush()
        self.stdout_original.flush()
