from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class PredictionModel(BaseModel):
    __tablename__ = "predictions"

    id: Mapped[bigint_pk]

    unom: Mapped[int] = mapped_column(nullable=True)
    district: Mapped[str] = mapped_column(nullable=True)
    building_material: Mapped[str] = mapped_column(nullable=True)
    building_assignment: Mapped[str] = mapped_column(nullable=True)
    building_total_area: Mapped[int] = mapped_column(nullable=True)
    area: Mapped[str] = mapped_column(nullable=True)
    project_number: Mapped[int] = mapped_column(nullable=True)
    floors_number: Mapped[int] = mapped_column(nullable=True)
    entrances_number: Mapped[int] = mapped_column(nullable=True)
    apartments_number: Mapped[int] = mapped_column(nullable=True)

    building_class: Mapped[str] = mapped_column(nullable=True)

    heat_supply_volume: Mapped[int] = mapped_column(nullable=True)
    heat_reverse_supply_volume: Mapped[int] = mapped_column(nullable=True)
    backflow_difference: Mapped[int] = mapped_column(nullable=True)
    leakage_difference: Mapped[int] = mapped_column(nullable=True)
    supply_temperature: Mapped[int] = mapped_column(nullable=True)
    return_temperature: Mapped[int] = mapped_column(nullable=True)
    counter_hours: Mapped[int] = mapped_column(nullable=True)
    heat_energy_consumption: Mapped[int] = mapped_column(nullable=True)
    municipal_district: Mapped[str] = mapped_column(nullable=True)
    emergency_status: Mapped[int] = mapped_column(nullable=True)

    total_area: Mapped[int] = mapped_column(nullable=True)

    total_area_lived_spaced: Mapped[int] = mapped_column(nullable=True)
    total_area_unlived_spaced: Mapped[int] = mapped_column(nullable=True)
    depreciation: Mapped[int] = mapped_column(nullable=True)
    wall_material: Mapped[int] = mapped_column(nullable=True)
    freight_elevators_number: Mapped[int] = mapped_column(nullable=True)
    housing_type: Mapped[int] = mapped_column(nullable=True)
    mkd_status: Mapped[int] = mapped_column(nullable=True)
    occurrence_year: Mapped[int] = mapped_column(nullable=True)
    occurrence_month: Mapped[int] = mapped_column(nullable=True)
    occurrence_day: Mapped[int] = mapped_column(nullable=True)
    predicted_label: Mapped[str] = mapped_column(nullable=True)

    elevators_number: Mapped[int] = mapped_column(nullable=True)
    prediction_title: Mapped[str] = mapped_column(nullable=True)
