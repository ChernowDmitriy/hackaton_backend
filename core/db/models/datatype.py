from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import DateMixin, BaseModel, str100


class DataTypeModel(BaseModel, DateMixin):
    __tablename__ = "datatype"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str100]
    ru_type: Mapped[str100] = mapped_column(nullable=True)
