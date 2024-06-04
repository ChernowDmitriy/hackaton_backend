from typing import Annotated

from fastapi import APIRouter, Depends, Request

from src.auth.services.dependencies import get_user_service
from src.auth.services.user_service import UserService
from src.auth.web.api.users.schemas import RetrieveUserByIDSchema

router = APIRouter()


@router.get(
    "/users/me",
    response_model=RetrieveUserByIDSchema,
    summary="Получить информацию о пользователе по ID",
)
async def get_user_by_id(
    request: Request,
    service: Annotated[UserService, Depends(get_user_service)],
):
    result = await service.get_user_by_id(request.state.user_id)
    response = RetrieveUserByIDSchema.model_validate(result, from_attributes=True)
    return response
