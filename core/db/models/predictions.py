from sqlalchemy import DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class PredictionsModel(BaseModel):
    __tablename__ = "predictions"

    id: Mapped[bigint_pk]

    unom: Mapped[int] = mapped_column(nullable=True)
    building_material: Mapped[str] = mapped_column(nullable=True)
    building_assignment: Mapped[str] = mapped_column(nullable=True)
    building_class: Mapped[str] = mapped_column(nullable=True)

    building_floors_number: Mapped[int] = mapped_column(nullable=True)

    heat_supply_volume: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_reverse_supply_volume: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    backflow_difference: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    leakage_difference: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    supply_temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    return_temperature: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    counter_hours: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    heat_energy_consumption: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)

    series_number_meter: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    floors_count: Mapped[int] = mapped_column(nullable=True)
    entrance_count: Mapped[int] = mapped_column(nullable=True)
    apartment_count: Mapped[int] = mapped_column(nullable=True)
    total_area: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    total_living_area: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    object_deprecation_bti: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    material_wall: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    building_failure_sign_of: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    elevators_number: Mapped[int] = mapped_column(nullable=True)
    roofing_material_bti: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    mkd_status: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    predictions: Mapped[int] = mapped_column(nullable=True)
    predicted_labels: Mapped[int] = mapped_column(nullable=True)
