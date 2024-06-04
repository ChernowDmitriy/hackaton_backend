import uuid
from typing import Annotated, List

from sqlalchemy import ForeignKey, func, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.db.base import BaseModel, DateMixin, str50, guid
from core.db.models.user import user_role_model

role_permission_model = Table(
    "role_permissions",
    BaseModel.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
)


class PermissionModel(BaseModel, DateMixin):
    __tablename__ = "permissions"

    id: Mapped[guid]

    name: Mapped[str50]

    roles: Mapped[List["RoleModel"]] = relationship(
        secondary=role_permission_model, back_populates="permissions"
    )


class RoleModel(BaseModel, DateMixin):
    __tablename__ = "roles"

    id: Mapped[
        Annotated[
            uuid.UUID,
            mapped_column(
                server_default=func.gen_random_uuid(),
                primary_key=True,
            ),
        ]
    ]

    name: Mapped[str50]
    alias: Mapped[str50]
    is_active: Mapped[bool]

    users: Mapped[List["UserModel"]] = relationship(
        secondary=user_role_model, back_populates="roles"
    )
    permissions: Mapped[List["PermissionModel"]] = relationship(
        secondary=role_permission_model, back_populates="roles"
    )
