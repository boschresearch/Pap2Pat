import csv
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Generator, Optional

import pandas as pd
from lxml import html

csv.field_size_limit(sys.maxsize)

LIST_FIELDS = ["authors", "author_names", "locations", "urls", "pdf_urls", "licenses"]
FLOAT_FIELDS = [
    "author_overlap",
    "title_min",
    "abstract_min",
    "title_max",
    "abstract_max",
]
DATE_FIELDS = ["date"]
DELIMITER = ";"

convert_none = lambda x: x if x != "None" else None
abstract_pattern = re.compile(r"^Abstract\s*")


def _convert_types(
    row: dict, list_fields: list[str], float_fields: list[str], date_fields: list[str]
) -> dict:
    for list_field in list_fields:
        if list_field in row:
            row[list_field] = [
                convert_none(value[1] or value[2])
                for value in re.findall(r"('([^']*)'|(None))", row[list_field])
            ]

    for float_field in float_fields:
        if float_field in row:
            row[float_field] = float(row[float_field])

    for date_field in date_fields:
        if date_field in row:
            row[date_field] = datetime.strptime(row[date_field], "%Y-%m-%d")

    return row


def normalize_abstract(abstract: str) -> str:
    abstract = abstract_pattern.sub("", abstract).strip()
    try:
        abstract_without_xml = str(html.fromstring(abstract).text_content())
    except:  # noqa
        abstract_without_xml = abstract
    return abstract_without_xml


def load_csv_generator(
    path: Path | str,
    batch_size: int,
    list_fields: list[str] = LIST_FIELDS,
    float_fields: list[str] = FLOAT_FIELDS,
    date_fields: list[str] = DATE_FIELDS,
    dont_split_along: Optional[str] = None,
) -> Generator[list[dict], None, None]:
    with open(path, "r", newline="", encoding="utf-8") as fp:
        reader = csv.DictReader(fp, delimiter=DELIMITER)
        batch = []
        for row in reader:
            row = _convert_types(row, list_fields, float_fields, date_fields)
            row["abstract"] = normalize_abstract(row["abstract"])

            if len(batch) < batch_size or (  # if batch size is not yet reached
                dont_split_along is not None
                and row[dont_split_along] == batch[-1][dont_split_along]
            ):
                batch.append(row)
            else:
                yield batch
                batch = [row]
        if batch:
            yield batch


def load_csv(path: Path | str) -> pd.DataFrame:
    df = pd.read_csv(path, sep=DELIMITER)

    for list_field in LIST_FIELDS:
        if list_field in df.columns:
            df[list_field] = df[list_field].apply(
                lambda v: [
                    convert_none(value[1] or value[2])
                    for value in re.findall(r"('([^']*)'|(None))", v)
                ]
            )

    for date_field in DATE_FIELDS:
        if date_field in df.columns:
            df[date_field] = pd.to_datetime(df[date_field])

    if "abstract" in df.columns:
        df["abstract"] = df["abstract"].apply(normalize_abstract)

    return df
