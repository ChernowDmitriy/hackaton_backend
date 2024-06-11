"""
6. Плановые-Внеплановые отключения 01.10.2023-30.04.2023
"""

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk, date_with_timezone


class PlannedUnplannedShutdownsModel(BaseModel):
    __tablename__ = "planned_unplanned_shutdowns"

    id: Mapped[bigint_pk]

    cause: Mapped[str]
    source: Mapped[str]
    registration_disconnection_date: Mapped[date_with_timezone]
    planned_shutdown_date: Mapped[date_with_timezone]
    planned_switch_on_date: Mapped[date_with_timezone]
    actual_shutdown_date: Mapped[date_with_timezone]
    actual_switch_on_date: Mapped[date_with_timezone]

    shutdown_type: Mapped[str]
    unom: Mapped[int] = mapped_column(BIGINT)
    address: Mapped[date_with_timezone]
