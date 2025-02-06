from typing import AsyncGenerator

from langchain_core.runnables.base import Runnable


async def answer_text_stream(
    runnable: Runnable,
    session_id: str,
    question: str,
) -> AsyncGenerator[str, None]:
    try:
        async for chunk in runnable.astream(
            input={"question": question},
            config={
                "configurable": {"session_id": session_id},
            },
        ):
            print(chunk)
            yield chunk.content
    except Exception as e:
        print(type(e), e)
        yield "Chatbot engine is not responding... (づ •. •)?"
