from enum import Enum


class DocumentStatus(str, Enum):
    UPLOADED = "UPLOADED"
    PROCESSING = "PROCESSING"
    PARSED = "PARSED"
    CHUNKED = "CHUNKED"
    EMBEDDED = "EMBEDDED"
    INDEXED = "INDEXED"
    READY = "READY"
    FAILED = "FAILED"


class ProviderType(str, Enum):
    OLLAMA = "OLLAMA"
    GEMINI = "GEMINI"


class ChunkingStrategy(str, Enum):
    FIXED = "FIXED"
    RECURSIVE = "RECURSIVE"
    SEMANTIC = "SEMANTIC"


class EmbeddingProvider(str, Enum):
    OLLAMA = "OLLAMA"
    SENTENCE_TRANSFORMER = "SENTENCE_TRANSFORMER"


class RetrievalStrategy(str, Enum):
    VECTOR = "VECTOR"
    HYBRID = "HYBRID"


class ParserType(str, Enum):
    PDF = "PDF"