from redis.asyncio.client import Redis

from app.core.config import CURRENT_CONFIG


chat_cache_redis = Redis.from_url(url=CURRENT_CONFIG.REDIS_URL)


async def close_redis_connections() -> None:
    print("redis 연결 해제 중...")

    await chat_cache_redis.aclose()

    print("redis 연결 해제 완료!")
