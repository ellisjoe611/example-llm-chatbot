from langchain_core.runnables.history import RunnableWithMessageHistory

from app.ai.history import get_redis_chat_history
from app.ai.model.ollama import OllamaModelStr, ollama_models
from app.ai.prompt.basic import basic_prompt


ollama_basic_runnables: dict[OllamaModelStr, RunnableWithMessageHistory] = {
    "llama2:7b": RunnableWithMessageHistory(
        basic_prompt | ollama_models["llama2:7b"],  # type: ignore
        get_session_history=get_redis_chat_history,
        input_messages_key="question",
        history_messages_key="history",
    ),
    "llama3:8b": RunnableWithMessageHistory(
        basic_prompt | ollama_models["llama3:8b"],  # type: ignore
        get_session_history=get_redis_chat_history,
        input_messages_key="question",
        history_messages_key="history",
    ),
    "llama3.1:8b": RunnableWithMessageHistory(
        basic_prompt | ollama_models["llama3.1:8b"],  # type: ignore
        get_session_history=get_redis_chat_history,
        input_messages_key="question",
        history_messages_key="history",
    ),
    "llama3.2:3b": RunnableWithMessageHistory(
        basic_prompt | ollama_models["llama3.2:3b"],  # type: ignore
        get_session_history=get_redis_chat_history,
        input_messages_key="question",
        history_messages_key="history",
    ),
}
