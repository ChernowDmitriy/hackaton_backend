from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class BTIUnloadingModel(BaseModel):
    __tablename__ = "bti_unloading"

    id: Mapped[bigint_pk]

    city: Mapped[str]
    administrative_district: Mapped[str]
    municipal_district: Mapped[str]
    locality: Mapped[str] = mapped_column(nullable=True)
    street: Mapped[str] = mapped_column(nullable=True)
    house_type: Mapped[str] = mapped_column(nullable=True)
    house_numbers: Mapped[int] = mapped_column(nullable=True)
    housing_numbers: Mapped[int] = mapped_column(nullable=True)
    building_type_number: Mapped[str] = mapped_column(nullable=True)
    building_number: Mapped[str] = mapped_column(nullable=True)

    unom: Mapped[int] = mapped_column(BIGINT)
    unad: Mapped[int] = mapped_column(nullable=True)

    building_material: Mapped[str] = mapped_column(nullable=True)
    building_assignment: Mapped[str] = mapped_column(nullable=True)
    building_class: Mapped[str] = mapped_column(nullable=True)
    building_type: Mapped[str] = mapped_column(nullable=True)
    building_floors_number: Mapped[int] = mapped_column(nullable=True)
    building_attribute: Mapped[str] = mapped_column(nullable=True)
    building_total_area: Mapped[str] = mapped_column(nullable=True)
