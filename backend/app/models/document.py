from dataclasses import dataclass
from datetime import datetime

from backend.app.models.enums import DocumentStatus


@dataclass(slots=True)
class Document:
    id: str
    filename: str
    stored_filename: str
    content_type: str
    file_size: int
    status: DocumentStatus
    created_at: datetime
    updated_at: datetime