"""
События за период_01.01.2024-30.04.2024
События за период_01.10.2023-31.12.2023
"""

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk, date_with_timezone


class IncidentsModel(BaseModel):
    __tablename__ = "incidents"

    id: Mapped[bigint_pk]

    name: Mapped[str]
    source: Mapped[str]
    external_system_creation_date: Mapped[date_with_timezone]
    closed_at: Mapped[date_with_timezone]
    area: Mapped[str]
    unom: Mapped[int] = mapped_column(BIGINT)
    address: Mapped[str]
    external_system_closed_date: Mapped[date_with_timezone]
