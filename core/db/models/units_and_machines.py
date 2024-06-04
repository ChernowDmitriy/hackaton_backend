import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Table, Column

from core.db.base import BaseModel, guid, str256, str100


class UnitModel(BaseModel):
    __tablename__ = "unit_models"

    id: Mapped[guid]
    name: Mapped[str256]
    alias: Mapped[str256] = mapped_column(nullable=True)
    type: Mapped[str100]
    is_deleted: Mapped[bool] = mapped_column(server_default="False", default=False)


class UnitGroupModel(BaseModel):
    __tablename__ = "unit_groups"

    id: Mapped[guid]
    name: Mapped[str256]
    alias: Mapped[str256] = mapped_column(nullable=True)
    type: Mapped[str100]
    is_deleted: Mapped[bool] = mapped_column(server_default="False", default=False)


class UnitNameModel(BaseModel):
    __tablename__ = "unit_names"

    id: Mapped[guid]
    name: Mapped[str256]
    alias: Mapped[str256] = mapped_column(nullable=True)
    type: Mapped[str100]
    is_deleted: Mapped[bool] = mapped_column(server_default="False", default=False)


class MachineModel(BaseModel):
    __tablename__ = "machines"

    id: Mapped[guid]
    serial_number: Mapped[str256]
    is_deleted: Mapped[bool] = mapped_column(server_default="False", default=False)

    unit_name: Mapped[uuid.UUID] = mapped_column(ForeignKey("unit_names.id"))
    unit_group: Mapped[uuid.UUID] = mapped_column(ForeignKey("unit_groups.id"))
    unit_model: Mapped[uuid.UUID] = mapped_column(ForeignKey("unit_models.id"))


machine_images = Table(
    "machine_images",
    BaseModel.metadata,
    Column("machine_id", ForeignKey("machines.id"), primary_key=True),
    Column("image_id", ForeignKey("files.id"), primary_key=True),
)
