from abc import ABC, abstractmethod
from typing import List

from fastapi import UploadFile

from core.db.models.file import FileModel
from src.backend.web.api.file.schemas import UploadDatasetSchemaInput


class IUploadFileUseCase(ABC):
    @abstractmethod
    async def upload_file(self, file: UploadFile, content: bytes):
        ...

    @abstractmethod
    async def upload_multiple_files(self, files: List[UploadFile], content: bytes):
        ...


class FileUploader(ABC):
    @abstractmethod
    async def upload_file(self, file: UploadDatasetSchemaInput) -> FileModel:
        ...
