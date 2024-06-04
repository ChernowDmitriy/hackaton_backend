import uuid
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, DateMixin, str100


class ModuleModel(BaseModel, DateMixin):
    __tablename__ = "modules"

    id: Mapped[
        Annotated[
            uuid.UUID,
            mapped_column(
                server_default=func.gen_random_uuid(),
                primary_key=True,
            ),
        ]
    ]

    name: Mapped[str100]
