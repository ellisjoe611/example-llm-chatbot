from typing import Literal
from langchain_community.cache import AsyncRedisCache
from langchain_ollama import ChatOllama

from app.core.cache.redis import chat_cache_redis

OllamaModelStr = Literal[
    "llama2:7b",
    "llama3:8b",
    "llama3.1:8b",
    "llama3.2:3b",
]


ollama_models: dict[OllamaModelStr, ChatOllama] = {
    "llama2:7b": ChatOllama(
        model="llama2:7b",
        cache=AsyncRedisCache(chat_cache_redis),
    ),
    "llama3:8b": ChatOllama(
        model="llama3:8b",
        cache=AsyncRedisCache(chat_cache_redis),
    ),
    "llama3.1:8b": ChatOllama(
        model="llama3.1:8b",
        cache=AsyncRedisCache(chat_cache_redis),
    ),
    "llama3.2:3b": ChatOllama(
        model="llama3.2:3b",
        cache=AsyncRedisCache(chat_cache_redis),
    ),
}
