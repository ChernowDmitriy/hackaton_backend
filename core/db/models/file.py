from sqlalchemy.orm import Mapped

from core.db.base import BaseModel, DateMixin, bigint_pk


class FileModel(BaseModel, DateMixin):
    __tablename__ = "files"

    id: Mapped[bigint_pk]
    name: Mapped[str]
    path: Mapped[str]
    ext: Mapped[str]
    byte_size: Mapped[int]
