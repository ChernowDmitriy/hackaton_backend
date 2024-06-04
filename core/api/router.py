from fastapi.routing import APIRouter

from core.api import docs, statics

core_router = APIRouter()

core_router.include_router(docs.router)
core_router.include_router(statics.router)
