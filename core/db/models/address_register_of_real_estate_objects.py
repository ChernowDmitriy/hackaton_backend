from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped, mapped_column

from core.db.base import BaseModel, bigint_pk


class AddressRegisterOfRealEstateObjectsModel(BaseModel):
    __tablename__ = "address_register_of_real_estate_objects"

    useless_id: Mapped[bigint_pk]
    global_id: Mapped[int] = mapped_column(BIGINT, nullable=True)

    obj_type: Mapped[str] = mapped_column(nullable=True)
    OnTerritoryOfMoscow: Mapped[str] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    unom: Mapped[int] = mapped_column(BIGINT, nullable=True)
    P1: Mapped[str] = mapped_column(nullable=True)
    P3: Mapped[str] = mapped_column(nullable=True)
    P4: Mapped[str] = mapped_column(nullable=True)
    P5: Mapped[str] = mapped_column(nullable=True)
    P6: Mapped[str] = mapped_column(nullable=True)
    P7: Mapped[str] = mapped_column(nullable=True)
    P90: Mapped[str] = mapped_column(nullable=True)
    simple_address: Mapped[str] = mapped_column(nullable=True)
    P91: Mapped[str] = mapped_column(nullable=True)
    l1_type: Mapped[str] = mapped_column(nullable=True)
    l1_value: Mapped[str] = mapped_column(nullable=True)
    l2_type: Mapped[str] = mapped_column(nullable=True)
    p0: Mapped[str] = mapped_column(nullable=True)
    l2_value: Mapped[str] = mapped_column(nullable=True)
    l3_type: Mapped[str] = mapped_column(nullable=True)
    P2: Mapped[str] = mapped_column(nullable=True)
    l3_value: Mapped[str] = mapped_column(nullable=True)
    l4_type: Mapped[str] = mapped_column(nullable=True)
    l4_value: Mapped[str] = mapped_column(nullable=True)
    l5_type: Mapped[str] = mapped_column(nullable=True)
    l5_value: Mapped[str] = mapped_column(nullable=True)
    adm_area: Mapped[str] = mapped_column(nullable=True)
    district: Mapped[str] = mapped_column(nullable=True)
    nreg: Mapped[str] = mapped_column(nullable=True)
    dreg: Mapped[str] = mapped_column(nullable=True)
    n_fias: Mapped[str] = mapped_column(nullable=True)
    d_fias: Mapped[str] = mapped_column(nullable=True)
    kad_n: Mapped[str] = mapped_column(nullable=True)
    kad_zu: Mapped[str] = mapped_column(nullable=True)
    kladr: Mapped[str] = mapped_column(nullable=True)
    tdoc: Mapped[str] = mapped_column(nullable=True)
    ndoc: Mapped[str] = mapped_column(nullable=True)
    ddoc: Mapped[str] = mapped_column(nullable=True)
    adr_type: Mapped[str] = mapped_column(nullable=True)
    vid: Mapped[str] = mapped_column(nullable=True)
    sostad: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=True)
    geodata: Mapped[str] = mapped_column(nullable=True)
    geodata_center: Mapped[str] = mapped_column(nullable=True)
