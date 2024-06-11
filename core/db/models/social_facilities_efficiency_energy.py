"""
12. Класс энергоэффективности соцобъектов
"""
from sqlalchemy import DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class SocialFacilitiesEfficiencyEnergyModel(BaseModel):
    __tablename__ = "social_facilities_efficiency_energies"

    id: Mapped[bigint_pk]
    building: Mapped[str]
    count_buildings: Mapped[int]
    total_area: Mapped[float]
    heated_area: Mapped[float] = mapped_column(DOUBLE_PRECISION, nullable=True)
    employees_average_number: Mapped[int] = mapped_column(nullable=True)
    building_type: Mapped[str] = mapped_column(nullable=True)
    energy_efficiency_class: Mapped[str] = mapped_column(nullable=True)
    floors_count: Mapped[int] = mapped_column(nullable=True)
    elevators_number: Mapped[int] = mapped_column(nullable=True)
    building_actual_depreciation: Mapped[int] = mapped_column(nullable=True)
    entrance_count: Mapped[int] = mapped_column(nullable=True)
    building_start_year: Mapped[int] = mapped_column(nullable=True)
