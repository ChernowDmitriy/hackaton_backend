import uuid
from typing import List

from sqlalchemy import String, ForeignKey, UUID, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import BaseModel, str100, DateMixin


class ScreenModel(BaseModel, DateMixin):
    __tablename__ = "screens"

    id = mapped_column(UUID, server_default=func.gen_random_uuid(),
                       primary_key=True)
    title: Mapped[str100]
    description: Mapped[str] = mapped_column(String(), nullable=True)

    width: Mapped[int]
    height: Mapped[int]
    positionX: Mapped[int]
    positionY: Mapped[int]

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))

    image_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("files.id"))
    image: Mapped["FileModel"] = relationship(lazy="selectin")

    parent_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("screens.id"),
        nullable=True)
    # parent: Mapped["ScreenModel"] = relationship(back_populates="children",
    #                                              remote_side=[id])

    children: Mapped[List["ScreenModel"]] = relationship(
        lazy="selectin",
        join_depth=100
    )
