from pydantic_settings import BaseSettings
from pydantic import Field

class Config(BaseSettings):
    HISTORY_TOKEN_LIMIT: int = Field(
        50000,
        ge=10000, 
        le=500000,
        description="Token limit must be between 10K and 500K"
    )
    
    CHARS_PER_TOKEN_RATIO: int = Field(
        default=4,
        ge=2,
        le=7,
        description="Characters per token for estimation must be between 2 and 7"
    )
    
    model_config = {
        "env_file": ".env",
    }

settings = Config()  # Ignore the IntelliSense error (if any)