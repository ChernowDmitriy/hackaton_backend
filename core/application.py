from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from core.const import CORE_DIR
from core.exceptions import BaseHTTPException, request_exception_handler, validation_exception_handler
from core.api.router import core_router
from core.settings import get_settings
from src.auth.services.security import JWTBearer
from src.auth.web.api.router import auth_router
from core.lifetime import register_shutdown_event, register_startup_event
from src.backend.web.api.router import main_backend_router

APP_ROOT = Path(__file__).parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    settings = get_settings()
    app = FastAPI(
        title="Hackaton Backend",
        docs_url=None,
        dependencies=[Depends(JWTBearer())],
        redoc_url=None,
        openapi_url="/api/v1/openapi.json",
        default_response_class=UJSONResponse,
    )

    register_startup_event(app)
    register_shutdown_event(app)

    app.include_router(router=core_router, prefix=settings.API_PREFIX)
    app.include_router(router=auth_router, prefix=settings.API_PREFIX)
    app.include_router(router=main_backend_router, prefix=settings.API_PREFIX)

    app.mount(
        "/static",
        StaticFiles(directory=CORE_DIR / "static"),
        name="static",
    )

    app.add_exception_handler(BaseHTTPException, request_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
