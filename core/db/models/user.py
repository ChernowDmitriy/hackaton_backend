import uuid
from typing import Annotated, Optional, List

from sqlalchemy import ForeignKey, func, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import BaseModel, DateMixin, str50, str100

user_role_model = Table(
    "user_roles",
    BaseModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


class UserModel(BaseModel, DateMixin):
    __tablename__ = "users"

    id: Mapped[
        Annotated[
            uuid.UUID,
            mapped_column(
                server_default=func.gen_random_uuid(),
                primary_key=True,
            ),
        ]
    ]

    email: Mapped[str100]
    login: Mapped[str100]
    password: Mapped[str50]

    first_name: Mapped[str50]
    last_name: Mapped[str50]
    middle_name: Mapped[Optional[str50]]

    company_id: Mapped[uuid.UUID]
    position: Mapped[str100]
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
