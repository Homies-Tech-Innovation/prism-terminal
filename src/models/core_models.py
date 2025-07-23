from pydantic import BaseModel  # type:ignore
from typing import Literal

class RouteDecision(BaseModel):
    prediction: Literal["command", "prompt"]


class ExitCode(BaseModel):
    exit_code: Literal[0, 1]  # 0 for clean exit; 1 for error
