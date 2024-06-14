from sqlalchemy.ext.asyncio import AsyncSession

from core.db.models.file import FileModel
from src.backend.common.interfaces.file import FileUploader
from src.backend.web.api.file.schemas import UploadDatasetSchemaInput


class FileUploaderRep(FileUploader):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upload_file(self, file: UploadDatasetSchemaInput) -> FileModel:
        """
        Добавить файл в хранилище UoW для последующей записи
        :param file: Upload File
        :return: None
        """
        new_file = FileModel(
            name=file.name,
            path=file.path,
            ext=file.ext,
            byte_size=file.byte_size
        )
        self.session.add(new_file)
        return new_file
