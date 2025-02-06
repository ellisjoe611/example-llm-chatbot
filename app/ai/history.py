from langchain_redis import RedisChatMessageHistory

from app.core.config import CURRENT_CONFIG


def get_redis_chat_history(session_id: str) -> RedisChatMessageHistory:
    return RedisChatMessageHistory(
        session_id=session_id,
        redis_url=CURRENT_CONFIG.REDIS_URL,
    )
