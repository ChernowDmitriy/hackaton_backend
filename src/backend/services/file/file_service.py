from typing import List

import aiofiles

from fastapi import UploadFile

from core.const import CORE_DIR
from core.db.models.file import FileModel
from src.backend.common.interfaces.file import IUploadFileUseCase, FileUploader
from src.backend.web.api.file.schemas import UploadDatasetSchemaInput


class FileUploaderUseCase(IUploadFileUseCase):
    STORE_DIR = f"{CORE_DIR}/static/files"

    def __init__(self, repository: FileUploader) -> None:
        self.repository = repository

    @staticmethod
    def get_extension(filename: str) -> str:
        return filename.split('.')[-1]

    async def save_file_to_disk(self,
                                data: UploadDatasetSchemaInput,
                                content: bytes) -> None:
        filename = data.name.split('.')[-1]
        async with aiofiles.open(f"{self.STORE_DIR}/{filename}.{data.ext}", 'wb') as out_file:
            await out_file.write(content)

    def get_file_path_by_name(self, filename: str):
        return f"{self.STORE_DIR}/{filename}"

    async def _upload_file(self, file_data: UploadDatasetSchemaInput) -> FileModel:
        file_db = await self.repository.upload_file(file_data)
        return file_db

    async def upload_file(self, file: UploadFile, file_content: bytes):
        extension = self.get_extension(file.filename)
        file_data = UploadDatasetSchemaInput(
            name=file.filename,
            path=f"{self.STORE_DIR}/{file.filename}.{extension}",
            ext=extension,
            byte_size=file.size
        )
        await self.save_file_to_disk(file_data, file_content)
        await self._upload_file(file_data)

    async def upload_multiple_files(self, files: List[UploadFile], content: bytes):
        for file in files:
            await self.upload_file(file, content)
            await self.repository.session.commit()
