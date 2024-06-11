from sqlalchemy.orm import Mapped

from core.db.base import BaseModel, bigint_pk, date_with_timezone


class MoekWiringDiagramModel(BaseModel):
    __tablename__ = "moek_wiring_diagrams"

    id: Mapped[bigint_pk]
    tp_number: Mapped[str]
    address_tp: Mapped[str]
    tp_type: Mapped[str]
    placement_type: Mapped[str]
    administrative_district: Mapped[str]
    commissioning_date: Mapped[date_with_timezone]
    balance_holder: Mapped[str]
    building_street: Mapped[str]
    heat_load_average: Mapped[str]
    heat_load_fact: Mapped[str]
    building_heat_load: Mapped[str]
    is_dispatching: Mapped[str]

