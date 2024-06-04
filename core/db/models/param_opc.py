from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, str256


class ParamOPCModel(BaseModel):
    __tablename__ = "param_opc"

    param_id: Mapped[int] = mapped_column(Integer,
                                          primary_key=True,
                                          nullable=True)
    opc_address: Mapped[str256] = mapped_column(nullable=True)
    address_to_write: Mapped[str256] = mapped_column(nullable=True)
    source_id_to_write: Mapped[str256] = mapped_column(nullable=True)
    source_name_to_write: Mapped[str256] = mapped_column(nullable=True)
