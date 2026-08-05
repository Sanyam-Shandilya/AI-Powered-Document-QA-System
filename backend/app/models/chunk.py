from dataclasses import dataclass


@dataclass(slots=True)
class Chunk:
    id: str
    document_id: str
    page_number: int
    chunk_index: int
    text: str
    start_char: int
    end_char: int