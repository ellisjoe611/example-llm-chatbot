from typing import Annotated

from fastapi import Path, status
from fastapi.routing import APIRouter
from ollama import ListResponse, ShowResponse

from app.domain.ai.model.ollama import OllamaModelService

router = APIRouter()


@router.get(
    "",
    summary="AI model list",
    description="Get the list of all available AI models",
    status_code=status.HTTP_200_OK,
    response_model=ListResponse,
)
async def get_list():
    return await OllamaModelService.get_model_list()


@router.get(
    "/{model_name}",
    summary="AI model info",
    description="Get info of all available AI models, otherwise throw error msg",
    status_code=status.HTTP_200_OK,
    response_model=ShowResponse,
)
async def get_info(
    model_name: Annotated[str, Path(description="Name of AI model")],
):
    return await OllamaModelService.get_model_info(model_name=model_name)
