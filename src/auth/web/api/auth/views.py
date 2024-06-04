from typing import Annotated

from fastapi import APIRouter, Depends

from src.auth.common.interfacies.auth_protocol import AuthorizationProtocol
from src.auth.services.auth_service import AuthService
from src.auth.services.dependencies import get_auth_service
from src.auth.web.api.auth.schemas import (
    RefreshTokenSchema,
    SuccessLoginSchema,
    SuccessRefreshTokenSchema,
    UserLoginSchema, SuccessRegistrationSchemaOutput, UserRegisterSchema,
)

router = APIRouter()


@router.post(
    "/login",
    response_model=SuccessLoginSchema,
    summary="Authorization",
)
async def login(
    data: UserLoginSchema,
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    result = await service.authorize(data)
    return result


@router.post(
    "/refresh_token",
    response_model=SuccessRefreshTokenSchema,
    summary="Refresh token and retrieve new tokens pair",
)
async def refresh_token(
    data: RefreshTokenSchema,
    service: Annotated[AuthService, Depends(get_auth_service)],
):
    result = await service.refresh_token(data)
    return result


@router.post(
    "/register",
    response_model=SuccessRegistrationSchemaOutput,
    summary="Register new user"
)
async def register_user(
    data: UserRegisterSchema,
    service: Annotated[AuthorizationProtocol, Depends(get_auth_service)],
):
    result = await service.register(data)
    return result
