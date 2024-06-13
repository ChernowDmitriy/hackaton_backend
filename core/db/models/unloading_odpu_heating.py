"""
11.Выгрузка_ОДПУ_отопление_ВАО_20240522
"""

from sqlalchemy import BIGINT, DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, guid


class UnloadingOdpuHeatingModel(BaseModel):
    __tablename__ = "unloading_odpu_heating"

    useless_id: Mapped[guid]

    id_uu: Mapped[int] = mapped_column(BIGINT, nullable=True, primary_key=True)
    id_tu: Mapped[int] = mapped_column(nullable=True)

    area: Mapped[str] = mapped_column(nullable=True)
    district: Mapped[str] = mapped_column(nullable=True)
    consumer: Mapped[str] = mapped_column(nullable=True)
    group: Mapped[str] = mapped_column(nullable=True)

    unom: Mapped[int] = mapped_column(BIGINT, nullable=True)

    address: Mapped[str] = mapped_column(nullable=True)
    central_heating: Mapped[str] = mapped_column(nullable=True)
    meter_brand: Mapped[str] = mapped_column(nullable=True)

    series_number_meter: Mapped[int] = mapped_column(nullable=True)

    month_year: Mapped[str] = mapped_column(nullable=True)
    day_month_year: Mapped[str] = mapped_column(nullable=True)
    unit: Mapped[str] = mapped_column(nullable=True)

    heat_supply_volume: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_reverse_supply_volume: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    backflow_difference: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    leakage_difference: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    supply_temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    return_temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    counter_hours: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_energy_consumption: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)

    errors: Mapped[str] = mapped_column(nullable=True)
