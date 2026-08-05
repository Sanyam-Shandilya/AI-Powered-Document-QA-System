from dataclasses import dataclass

from backend.app.models.chunk import Chunk


@dataclass(slots=True)
class SearchResult:
    chunk: Chunk
    score: float