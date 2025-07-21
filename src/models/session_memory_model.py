from pydantic import BaseModel, Field  # type:ignore
from enum import Enum


class SessionEntryRole(str, Enum):
    USER = "user"
    LLM = "llm"
    SYSTEM = "system"


class SessionEntry(BaseModel):
    role: SessionEntryRole
    content: str = Field(..., min_length=1)
