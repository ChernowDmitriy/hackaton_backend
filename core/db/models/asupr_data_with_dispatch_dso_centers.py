"""
8. Данные АСУПР с диспетчерскими ОДС
"""

from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class AsuprDataWithDispatchDsoCentersModel(BaseModel):
    __tablename__ = "asupr_data_with_dispatch_dso_center"

    id: Mapped[bigint_pk]
    short_address: Mapped[str]
    full_address: Mapped[str]
    full_address: Mapped[str]
    area: Mapped[str]
    unom: Mapped[int] = mapped_column(BIGINT)
    group: Mapped[str]
    ods_number: Mapped[str] = mapped_column(nullable=True)
    ods_address: Mapped[str] = mapped_column(nullable=True)
    consumer: Mapped[str]
    ctp: Mapped[str]
