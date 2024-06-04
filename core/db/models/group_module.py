import uuid
from typing import Annotated

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, DateMixin


class GroupModuleModel(BaseModel, DateMixin):
    __tablename__ = "group_modules"

    id: Mapped[
        Annotated[
            uuid.UUID,
            mapped_column(
                server_default=func.gen_random_uuid(),
                primary_key=True,
            ),
        ]
    ]

    group_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("groups.id"))
    module_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("modules.id"))
