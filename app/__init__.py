from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from app.api import api_router
from app.core.config import CURRENT_CONFIG
from app.core.cache.redis import close_redis_connections


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    print("서버 시작")

    yield

    # close backend
    await close_redis_connections()


def get_app() -> FastAPI:
    app = FastAPI(
        debug=True,
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        redirect_slashes=False,
    )

    # add middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["http://127.0.0.1"],
        allow_headers=["*"],
        allow_methods=["*"],
    )
    app.add_middleware(
        SessionMiddleware,
        secret_key=CURRENT_CONFIG.SESSION_SECRET_KEY,
        max_age=60 * 60,
    )

    # include routers
    app.include_router(api_router)

    return app
