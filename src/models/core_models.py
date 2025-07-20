from pydantic import BaseModel  # type:ignore
from typing import Literal


class RouteDecision(BaseModel):
    prediction: Literal["command", "prompt"]


class ExitCode(BaseModel):
    exit_code: Literal[0, 1]
