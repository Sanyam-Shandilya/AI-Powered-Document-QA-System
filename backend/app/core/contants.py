from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

STORAGE_DIR = PROJECT_ROOT / "storage"

UPLOAD_DIR = STORAGE_DIR / "uploads"

CHROMA_DIR = STORAGE_DIR / "chroma"

CACHE_DIR = STORAGE_DIR / "cache"

MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

SUPPORTED_FILE_TYPES = {
    ".pdf",
}

SUPPORTED_CONTENT_TYPES = {
    "application/pdf",
}