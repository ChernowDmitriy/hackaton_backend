import datetime

from sqlalchemy import BIGINT, DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class UnloadingOdpuHeating(BaseModel):
    __tablename__ = "unloading_odpu_heating"

    id_uu: Mapped[bigint_pk]
    id_tu: Mapped[int]

    area: Mapped[str]
    district: Mapped[str]
    consumer: Mapped[str]
    group: Mapped[str]
    unom: Mapped[int] = mapped_column(BIGINT)
    address: Mapped[str] = mapped_column(nullable=True)
    central_heating: Mapped[str] = mapped_column(nullable=True)
    meter_brand: Mapped[str]
    series_number_meter: Mapped[int]
    month_year: Mapped[str] = mapped_column(nullable=True)
    day_month_year: Mapped[str] = mapped_column(nullable=True)
    unit: Mapped[str]

    heat_supply_volume: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_reverse_supply_volume: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    backflow_difference: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    leakage_difference: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    supply_temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    return_temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    counter_hours: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_energy_consumption: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    errors: Mapped[str] = mapped_column(nullable=True)
