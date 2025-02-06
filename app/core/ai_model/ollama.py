from ollama import AsyncClient

from app.core.config import CURRENT_CONFIG

ollama_client = AsyncClient(
    host=CURRENT_CONFIG.OLLAMA_URL,
)
