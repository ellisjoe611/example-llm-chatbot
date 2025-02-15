from fastapi import status
from fastapi.exceptions import HTTPException
from ollama import ListResponse, ResponseError, ShowResponse, StatusResponse

from app.core.ai_client.ollama import ollama_client


class OllamaModelService:
    @staticmethod
    async def get_model_list() -> ListResponse:
        try:
            return await ollama_client.list()
        except ConnectionError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e)
            )
        except ResponseError as e:
            raise HTTPException(status_code=e.status_code, detail=e.error)

    @staticmethod
    async def get_model_info(model_name: str) -> ShowResponse:
        try:
            return await ollama_client.show(model=model_name)
        except ConnectionError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e)
            )
        except ResponseError as e:
            raise HTTPException(status_code=e.status_code, detail=e.error)

    @staticmethod
    async def delete_model(model_name: str) -> StatusResponse:
        try:
            return await ollama_client.delete(model=model_name)
        except ConnectionError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(e)
            )
        except ResponseError as e:
            raise HTTPException(status_code=e.status_code, detail=e.error)
