from sqlalchemy.orm import Mapped

from core.db.base import BaseModel, guid, DateMixin


class FileModel(BaseModel, DateMixin):
    __tablename__ = "files"

    id: Mapped[guid]
    name: Mapped[str]
    path: Mapped[str]
    ext: Mapped[str]
    byte_size: Mapped[int]
