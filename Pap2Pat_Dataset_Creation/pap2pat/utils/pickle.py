import pickle
from functools import lru_cache
from pathlib import Path
from typing import Generator, Optional

from tqdm import tqdm

from .csv import normalize_abstract

index_cache = {}


def _get_index(path: Path) -> dict:
    global index_cache
    if path not in index_cache:
        with open(path, "rb") as fp:
            index = pickle.load(fp)
            index_cache[path] = index
    else:
        index = index_cache[path]
    return index


def load_pickle(data_path: Path, index_path: Path, desc="Files"):
    num_docs = get_num_pickles(index_path)
    return list(tqdm(load_pickle_generator(data_path), total=num_docs, desc=f"Loading {desc}"))


def load_pickle_generator(
    data_path: Path, index_path: Optional[Path] = None, skip: int = 0
) -> Generator[dict, None, None]:
    with open(data_path, "rb") as fp:
        if skip > 0:
            assert index_path is not None, "index_path is required to use skip"
            index = _get_index(index_path)
            index_keys = iter(index.keys())
            for _ in range(skip + 1):
                key = next(index_keys)
            fp.seek(index[key])  # type: ignore

        while True:
            try:
                d = pickle.load(fp)
                if "abstract" in d:
                    d["abstract"] = normalize_abstract(d["abstract"])
                yield d
            except EOFError:
                break


def load_pickle_by_index(i: int, data_path: Path, index_path: Path) -> dict:
    index = _get_index(index_path)
    with open(data_path, "rb") as fp:
        fp.seek(list(index.values())[i])
        d = pickle.load(fp)
        if "abstract" in d:
            d["abstract"] = normalize_abstract(d["abstract"])
        return d


@lru_cache(maxsize=200)
def load_pickle_by_id(id: str, data_path: Path, index_path: Path) -> dict:
    index = _get_index(index_path)
    with open(data_path, "rb") as fp:
        fp.seek(index[id])
        d = pickle.load(fp)
        if "abstract" in d:
            d["abstract"] = normalize_abstract(d["abstract"])
        return d


def get_num_pickles(index_path: Path) -> int:
    index = _get_index(index_path)
    return len(index)
