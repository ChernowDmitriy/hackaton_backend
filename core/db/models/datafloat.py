import datetime

from sqlalchemy import Index
from sqlalchemy.orm import mapped_column, Mapped

from core.db.base import BaseModel, DateMixin


class DataFloatModel(BaseModel, DateMixin):
    __tablename__ = "datafloat"
    __table_args__ = (
        Index("idx_col345",
              "param_id",
              "borehole_id",
              "source_time"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    param_id: Mapped[int]
    borehole_id: Mapped[int]
    source_time: Mapped[datetime.datetime]
    server_time: Mapped[datetime.datetime]
    value: Mapped[float]
    source_id: Mapped[int] = mapped_column(nullable=True)
