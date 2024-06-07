from abc import ABC, abstractmethod

from fastapi import UploadFile


class IUploadFileUseCase(ABC):
    @abstractmethod
    async def upload_file(self, file: UploadFile):
        ...


class FileUploader(ABC):
    @abstractmethod
    async def upload_file(self, file: UploadFile) -> UploadFile:
        ...
