from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from src.backend.common.interfaces.file import IUploadFileUseCase
from src.backend.common.repositories.file_rep import FileUploaderRep
from src.backend.services.file.file_service import FileUploaderUseCase


async def get_file_repository(
    session: AsyncSession = Depends(get_db_session),
):
    return FileUploaderRep(session)


async def get_file_uploader_use_case(
    repository: IUploadFileUseCase = Depends(get_file_repository)
):
    return FileUploaderUseCase(repository)
