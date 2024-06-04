from fastapi.routing import APIRouter

from src.auth.web.api import auth, users

auth_router = APIRouter()
auth_router.include_router(auth.router, prefix="/auth", tags=["Авторизация"])
auth_router.include_router(users.router, tags=["Пользователи"])
