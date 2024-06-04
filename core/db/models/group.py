import uuid
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, DateMixin, str50


class GroupModel(BaseModel, DateMixin):
    __tablename__ = "groups"

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
