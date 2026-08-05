from pydantic import BaseModel

from backend.app.models.enums import DocumentStatus


class UploadResponse(BaseModel):
    id: str
    filename: str
    status: DocumentStatus
    message: str