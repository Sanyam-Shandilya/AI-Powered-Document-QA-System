from datetime import datetime

from pydantic import BaseModel

from backend.app.models.enums import DocumentStatus


class DocumentResponse(BaseModel):
    id: str
    filename: str
    stored_filename: str
    content_type: str
    file_size: int
    status: DocumentStatus
    created_at: datetime
    updated_at: datetime