from typing import Annotated
from fastapi import status, Body
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter

from app.ai.runnable.ollama import ollama_basic_runnables
from app.api.chatbot.serializer.request import QuestionBody
from app.ai.streaming.answer import answer_text_stream

# TODO 임시 세션 id임. 추후에 로그인 id 등으로 대체할 예정
SESSION_ID = "guest"

router = APIRouter()


@router.post(
    "",
    summary="Chatbot Streaming",
    description="Ask question to chatbot.",
    status_code=status.HTTP_200_OK,
    response_class=StreamingResponse,
)
async def get_ok(
    question_body: Annotated[QuestionBody, Body()],
):
    runnable = ollama_basic_runnables["llama3.1:8b"]

    return StreamingResponse(
        content=answer_text_stream(
            runnable=runnable,
            session_id=SESSION_ID,
            question=question_body.question,
        ),
        status_code=status.HTTP_200_OK,
        media_type="text/plain; charset=utf-8",
    )


@router.delete(
    "/history",
    summary="Clear Chat History",
    description="Clear all chat history with chatbot",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def clear_history():
    runnable = ollama_basic_runnables["llama3.1:8b"]
    session_history = runnable.get_session_history(session_id=SESSION_ID)

    await session_history.aclear()

    return None
