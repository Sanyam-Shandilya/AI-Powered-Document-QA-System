from dataclasses import dataclass

from backend.app.models.chunk import Chunk


@dataclass(slots=True)
class EmbeddedChunk:
    chunk: Chunk
    embedding: list[float]