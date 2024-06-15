from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class AddressModel(BaseModel):
    __tablename__ = "addresses"

    id: Mapped[bigint_pk]

    unom: Mapped[int] = mapped_column(nullable=True)
    latitude: Mapped[str] = mapped_column(nullable=True)
    longitude: Mapped[str] = mapped_column(nullable=True)
