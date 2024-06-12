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

    name: Mapped[str] = mapped_column(nullable=True)
    source: Mapped[str] = mapped_column(nullable=True)
    external_system_creation_date: Mapped[date_with_timezone] = mapped_column(nullable=True)
    closed_at: Mapped[date_with_timezone] = mapped_column(nullable=True)
    area: Mapped[str] = mapped_column(nullable=True)
    unom: Mapped[int] = mapped_column(BIGINT, nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    external_system_closed_date: Mapped[date_with_timezone] = mapped_column(nullable=True)
