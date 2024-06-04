import uuid
from typing import Optional, List

from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import BaseModel, DateMixin, str50, str100, guid

user_role_model = Table(
    "user_roles",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


class UserModel(BaseModel, DateMixin):
    __tablename__ = "users"

    id: Mapped[guid]

    email: Mapped[str100]
    password: Mapped[str50]

    first_name: Mapped[str50]
    last_name: Mapped[str50]
    middle_name: Mapped[Optional[str50]]

    is_active: Mapped[bool]

    refresh_token: Mapped[str50] = mapped_column(nullable=True)

    roles: Mapped[List["RoleModel"]] = relationship(
        secondary=user_role_model, back_populates="users"
    )


class UserGroupModel(BaseModel, DateMixin):
    __tablename__ = "user_groups"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"),
                                               primary_key=True)

    group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("groups.id"),
                                                primary_key=True)
