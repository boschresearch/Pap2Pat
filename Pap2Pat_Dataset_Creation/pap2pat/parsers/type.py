from typing import TypedDict


class Section(TypedDict):
    title: str
    paragraphs: list[str]
    subsections: list["Section"]


class Document(TypedDict):
    id: str
    authors: list[str]
    title: str
    date: str
    abstract: str
    sections: list[Section]
