from fastapi.routing import APIRouter

from core.api import docs

core_router = APIRouter()

core_router.include_router(docs.router)
