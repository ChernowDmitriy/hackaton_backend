from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class ReactionsModel(BaseModel):
    __tablename__ = "reactions"

    id: Mapped[bigint_pk]
    tp_number: Mapped[str] = mapped_column(nullable=True)
    address_tp: Mapped[str] = mapped_column(nullable=True)
    heat_supply_source: Mapped[str] = mapped_column(nullable=True)
    short_address: Mapped[str] = mapped_column(nullable=True)
    unom: Mapped[int] = mapped_column(nullable=True)
    ods_number: Mapped[str] = mapped_column(nullable=True)
    ods_address: Mapped[str] = mapped_column(nullable=True)
    consumer: Mapped[str] = mapped_column(nullable=True)
    geodata_y: Mapped[str] = mapped_column(nullable=True)
    geodata_center_y: Mapped[str] = mapped_column(nullable=True)


