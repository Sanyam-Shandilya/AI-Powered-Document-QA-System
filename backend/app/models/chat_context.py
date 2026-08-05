from dataclasses import dataclass

from backend.app.models.search_result import SearchResult


@dataclass(slots=True)
class ChatContext:
    question: str
    retrieved_chunks: list[SearchResult]
    prompt: str