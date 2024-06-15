from fastapi import APIRouter

from core.exceptions import BaseValidationErrorResponse
from src.backend.web.api import file, address, prediction

main_backend_router = APIRouter(responses={422: {"model": BaseValidationErrorResponse}})

main_backend_router.include_router(file.router, prefix="/files", tags=["Файлы"])
main_backend_router.include_router(address.router, prefix="/unoms", tags=["УНОМ"])
main_backend_router.include_router(prediction.router, prefix="/predictions", tags=["Предсказания"])
