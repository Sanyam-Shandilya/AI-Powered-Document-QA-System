from dataclasses import dataclass


@dataclass(slots=True)
class ParsedDocument:
    document_id: str
    text: str
    pages: list[str]
    page_count: int
    character_count: int