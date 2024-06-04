import datetime

from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import DateMixin, BaseModel


class DataIntegerModel(BaseModel, DateMixin):
    __tablename__ = "datainteger"

    id: Mapped[int] = mapped_column(primary_key=True)
    param_id: Mapped[int]
    borehole_id: Mapped[int]
    source_time: Mapped[datetime.datetime]
    server_time: Mapped[datetime.datetime]
    value: Mapped[int]
    source_id: Mapped[int] = mapped_column(nullable=True)
