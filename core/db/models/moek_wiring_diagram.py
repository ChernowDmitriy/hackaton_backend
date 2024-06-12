"""
7. Схема подключений МОЭК
"""
from sqlalchemy import DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk, date_with_timezone


class MoekWiringDiagramModel(BaseModel):
    __tablename__ = "moek_wiring_diagrams"

    id: Mapped[bigint_pk]
    tp_number: Mapped[str] = mapped_column(nullable=True)
    address_tp: Mapped[str] = mapped_column(nullable=True)
    tp_type: Mapped[str] = mapped_column(nullable=True)
    placement_type: Mapped[str] = mapped_column(nullable=True)
    administrative_district: Mapped[str] = mapped_column(nullable=True)
    municipal_district: Mapped[str] = mapped_column(nullable=True)
    heat_supply_source: Mapped[str] = mapped_column(nullable=True)
    commissioning_date: Mapped[date_with_timezone] = mapped_column(nullable=True)
    balance_holder: Mapped[str] = mapped_column(nullable=True)
    building_street: Mapped[str] = mapped_column(nullable=True)

    heat_load_average: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_load_fact: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    building_heat_load: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    building_ventilation_heat_load: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)

    is_dispatching: Mapped[str] = mapped_column(nullable=True)

