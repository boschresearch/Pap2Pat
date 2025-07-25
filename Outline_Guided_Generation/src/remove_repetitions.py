from datetime import datetime
import json
from pathlib import Path
import re
import subprocess
from typing import Callable

from hydralette import Config, Field
from pyrootutils import setup_root
from tqdm import tqdm

from src.utils.general import get_logger
from src.generate import postprocess

log = get_logger(__name__)
root = setup_root(__file__)


def equal(w1: list[str], w2: list[str]) -> bool:
    return w1 == w2


def norm_numbers(w1: list[str], w2: list[str]) -> tuple[list[str], list[str]]:
    for l in (w1, w2):
        for i in range(len(l)):
            try:
                _ = float(l[i])
            except:  # noqa
                pass
            else:
                l[i] = "<<number>>"
    return w1, w2


def equals_with_numbers(w1: list[str], w2: list[str]) -> bool:
    w1, w2 = norm_numbers(w1, w2)
    return w1 == w2


def equals_with_numbers_and_threshold(w1: list[str], w2: list[str]) -> bool:
    w1, w2 = norm_numbers(w1, w2)
    n_matched = sum(c1 == c2 for c1, c2 in zip(w1, w2))
    return n_matched / len(w1) > 0.9


match_fn = Callable[[list[str], list[str]], bool]


cfg = Config(
    dir=Field(type=Path), 
    min_length=50, 
    max_cycle_length=300, 
    matcher=Field(convert=lambda s: globals()[s], default=equal),
    data_dir=root.parent / "Pap2Pat" / "data"
)


def get_whitespaces(s: str, words: list[str]):
    for word in words:
        i = s.index(word)
        yield s[:i]
        s = s[i + len(word) :]


def remove_repetitions(matches: match_fn, s: str, min_length: int, max_cycle_length: int):
    words = s.split()
    whitespaces = list(get_whitespaces(s, words))
    remove_indices = detect_repetitions(
        matches, words, min_length=min_length, max_cycle_length=max_cycle_length
    )
    return "".join([
        whitespace + word 
        for i, (word, whitespace) in enumerate(zip(words, whitespaces))
        if i not in remove_indices
    ])


def detect_repetitions(
    matches: match_fn, words: list[str], min_length: int, max_cycle_length: int
) -> list[int]:
    for k in range(1, max_cycle_length):
        # if words[-k:] == words[-2 * k : -k]:
        if matches(words[-k:], words[-2 * k : -k]):
            i = 2
            # while words[-k:] == words[-(i + 1) * k : -i * k]:
            while matches(words[-k:], words[-(i + 1) * k : -i * k]):
                i += 1
            i -= 1

            remove_slice = slice(-i * k, None)
            remove_indices = list(range(len(words)))[remove_slice]

            total_length = len(remove_indices) + k

            if total_length >= min_length:
                remove_rest = detect_repetitions(
                    matches,
                    words[: remove_slice.start - k],
                    min_length=min_length,
                    max_cycle_length=max_cycle_length,
                )
                return [*remove_indices, *remove_rest]
    return []


def main(cfg: Config):
    data_dir: Path = cfg.data_dir
    src_dir: Path = cfg.dir
    out_dir: Path = src_dir.parent / (src_dir.name + "-no_reps")
    if out_dir.exists():
        out_dir = src_dir.parent / (
            src_dir.name + "-no_reps-" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        )
        assert not out_dir.exists()

    log.info(f"Saving to {out_dir}")
    log.info("Copying files")
    subprocess.call(f"cp -r {src_dir}/ {out_dir}/", shell=True)

    log.info("Removing repetitions")
    for sample_dir in tqdm(list(out_dir.glob("predictions/*/*"))):
        sample_id = sample_dir.name
        ref_description = json.loads(data_dir.joinpath(f"{sample_id}/patent.json").read_text())["sections"][0]

        chunks = []

        for assistant_f in sorted(
            list(sample_dir.glob(r"conversations/chunk-*-assistant.md")),
            key=lambda f: int(re.findall(r"chunk-(\d+)-assistant.md", f.name)[0])
        ):
            assistant_s = assistant_f.read_text()
            chunk_start, chunk_end = next(re.finditer(r"```md(.*)```", assistant_s, re.DOTALL)).span(1)
            chunk = assistant_s[chunk_start:chunk_end]
            chunk_processed = remove_repetitions(cfg.matcher, chunk, min_length=cfg.min_length, max_cycle_length=cfg.max_cycle_length)
            assistant_s_processed = assistant_s[:chunk_start] + chunk_processed + assistant_s[chunk_end:]
            assistant_f.write_text(assistant_s_processed)
            chunks.append([{"role": "assistant", "content": assistant_s_processed}])

        combined_processed = postprocess(chunks, ref_description)
        gen_path = sample_dir / "generated.md"
        gen_path.write_text(combined_processed)

    log.info("Done")


if __name__ == "__main__":
    cfg.apply()
    main(cfg)
