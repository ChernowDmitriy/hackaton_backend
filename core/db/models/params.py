import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from core.db.base import DateMixin, BaseModel, str256


class ParamsModel(BaseModel):
    __tablename__ = "params"

    id: Mapped[int] = mapped_column(primary_key=True)

    uom_id: Mapped[int] = mapped_column(ForeignKey("uom.id"))
    name: Mapped[str256]
    ru_name: Mapped[str256] = mapped_column(nullable=True)
    typedata_id: Mapped[int]
    description: Mapped[str256] = mapped_column(nullable=True)
    source_id: Mapped[int] = mapped_column(nullable=True)
    create_at: Mapped[datetime.datetime] = mapped_column(nullable=True)
