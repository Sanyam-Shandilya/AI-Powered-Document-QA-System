from pydantic import BaseModel, ConfigDict, Field


class ChatRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )

    question: str = Field(
        ...,
        min_length=1,
        max_length=5000
    )

    temperature: float = Field(
        default=0.7,
        ge=0,
        le=2
    )

    top_k: int = Field(
        default=5,
        ge=1,
        le=20
    )