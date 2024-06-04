import uuid
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, DateMixin, str50, guid


class GroupModel(BaseModel, DateMixin):
    __tablename__ = "groups"

    id: Mapped[guid]

    name: Mapped[str50]
