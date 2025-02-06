from fastapi.routing import APIRouter

from .ai_model.base import router as ai_model_router
from .chatbot.basic import router as chatbot_basic_router

api_router = APIRouter(prefix="/api")


# ai_model
api_router.include_router(ai_model_router, prefix="/ai_model", tags=["AI Model"])

# chatbot
api_router.include_router(
    chatbot_basic_router, prefix="/chatbot", tags=["Chatbot - Basic"]
)
