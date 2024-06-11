from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, DateMixin, str50, str100, bigint_pk


class UserModel(BaseModel, DateMixin):
    __tablename__ = "users"

    id: Mapped[bigint_pk]

    email: Mapped[str100]
    password: Mapped[str50]

    first_name: Mapped[str50]
    last_name: Mapped[str50]
    middle_name: Mapped[Optional[str50]]

    is_active: Mapped[bool] = mapped_column(server_default="True", default=True)

    refresh_token: Mapped[str50] = mapped_column(nullable=True)
