import datetime

from sqlalchemy.orm import mapped_column, Mapped

from core.db.base import DateMixin, BaseModel


class DataBooleanModel(BaseModel, DateMixin):
    __tablename__ = "databoolean"

    id: Mapped[int] = mapped_column(primary_key=True)
    param_id: Mapped[int]
    borehole_id: Mapped[int]
    source_time: Mapped[datetime.datetime]
    server_time: Mapped[datetime.datetime]
    value: Mapped[float]
    source_id: Mapped[int] = mapped_column(nullable=True)
