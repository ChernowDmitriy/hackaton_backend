"""
14.xlsx
"""

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class EconomicCharacteristicHouseModel(BaseModel):
    __tablename__ = "economic_characteristics_houses"

    id: Mapped[bigint_pk]
    name: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    unom: Mapped[int] = mapped_column(nullable=True)
    district: Mapped[str] = mapped_column(nullable=True)
    area: Mapped[str] = mapped_column(nullable=True)
    col_758: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_759: Mapped[int] = mapped_column(nullable=True)
    col_760: Mapped[int] = mapped_column(nullable=True)
    col_761: Mapped[int] = mapped_column(nullable=True)
    col_762: Mapped[float] = mapped_column(nullable=True)
    col_763: Mapped[float] = mapped_column(nullable=True)
    col_764: Mapped[float] = mapped_column(nullable=True)
    col_766: Mapped[int] = mapped_column(nullable=True)
    col_769: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_770: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_771: Mapped[int] = mapped_column(nullable=True)
    col_772: Mapped[int] = mapped_column(nullable=True)
    col_775: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_781: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_1945_del: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_2463: Mapped[int] = mapped_column(BIGINT, nullable=True)
    col_3163: Mapped[int] = mapped_column(BIGINT, nullable=True)
