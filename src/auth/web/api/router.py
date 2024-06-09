from fastapi.routing import APIRouter

from core.exceptions import BaseValidationErrorResponse
from src.auth.web.api import auth, users

auth_router = APIRouter(responses={422: {"model": BaseValidationErrorResponse}})

auth_router.include_router(auth.router, prefix="/auth", tags=["Авторизация"])
auth_router.include_router(users.router, tags=["Пользователи"])
