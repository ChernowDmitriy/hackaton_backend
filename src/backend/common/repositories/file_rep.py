from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.common.interfaces.file import FileUploader


class FileUploaderRep(FileUploader):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upload_file(self, file: UploadFile) -> None:
        """
        Добавить файл в хранилище UoW для последующей записи
        :param file: Upload File
        :return: None
        """
        pass
