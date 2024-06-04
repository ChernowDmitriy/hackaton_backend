from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from src.auth.common.repositories.user_rep import UserRepository
from src.auth.services.auth_service import AuthService
from src.auth.services.user_service import UserService


async def get_user_repository(
    session: AsyncSession = Depends(get_db_session),
):
    return UserRepository(session)


async def get_auth_service(
    repository: UserRepository = Depends(get_user_repository),
):
    return AuthService(repository)


async def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
):
    return UserService(repository)
