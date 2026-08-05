from pydantic import BaseModel, ConfigDict


class UploadRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid"
    )