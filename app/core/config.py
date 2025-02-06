from dataclasses import dataclass
import os
import typing
from typing import Literal

PhaseStr = Literal["dev", "qa", "prod"]


@dataclass
class Config:
    OLLAMA_URL: str
    REDIS_URL: str
    SESSION_SECRET_KEY: str
    TEMP_PATH: str


configs: dict[PhaseStr, Config] = {
    "dev": Config(
        OLLAMA_URL="http://127.0.0.1:11434",
        REDIS_URL="redis://127.0.0.1:6379",
        SESSION_SECRET_KEY="dev_session_secret_key",
        TEMP_PATH="./tmp",
    ),
    "qa": Config(
        OLLAMA_URL="http://127.0.0.1:11434",
        REDIS_URL="redis://127.0.0.1:6379",
        SESSION_SECRET_KEY="qa_session_secret_key",
        TEMP_PATH="./tmp",
    ),
    "prod": Config(
        OLLAMA_URL="http://127.0.0.1:11434",
        REDIS_URL="redis://127.0.0.1:6379",
        SESSION_SECRET_KEY="prod_session_secret_key",
        TEMP_PATH="./tmp",
    ),
}


CURRENT_PHASE: PhaseStr = typing.cast(PhaseStr, os.environ["PHASE"].lower())

CURRENT_CONFIG: Config = configs[CURRENT_PHASE]
