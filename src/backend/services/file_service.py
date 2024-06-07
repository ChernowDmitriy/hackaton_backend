from fastapi import UploadFile

from src.backend.common.interfaces.file import IUploadFileUseCase


class UploadFileUseCase(IUploadFileUseCase):
    async def upload_file(self, file: UploadFile):
        pass
