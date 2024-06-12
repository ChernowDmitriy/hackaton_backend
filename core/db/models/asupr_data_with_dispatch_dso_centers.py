"""
8. Данные АСУПР с диспетчерскими ОДС
"""

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class AsuprDataWithDispatchDsoCentersModel(BaseModel):
    __tablename__ = "asupr_data_with_dispatch_dso_center"

    id: Mapped[bigint_pk]
    short_address: Mapped[str] = mapped_column(nullable=True)
    full_address: Mapped[str] = mapped_column(nullable=True)
    area: Mapped[str] = mapped_column(nullable=True)
    unom: Mapped[int] = mapped_column(BIGINT, nullable=True)
    group: Mapped[str] = mapped_column(nullable=True)
    ods_number: Mapped[str] = mapped_column(nullable=True)
    ods_address: Mapped[str] = mapped_column(nullable=True)
    consumer: Mapped[str] = mapped_column(nullable=True)
    ctp: Mapped[str] = mapped_column(nullable=True)
