from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, DateMixin, str100


class UOMModel(BaseModel, DateMixin):
    __tablename__ = "uom"

    id: Mapped[int] = mapped_column(primary_key=True)

    code: Mapped[str100]
    blockflag: Mapped[bool] = mapped_column(default="False")
