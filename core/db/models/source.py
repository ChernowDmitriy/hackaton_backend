from sqlalchemy.orm import mapped_column, Mapped

from core.db.base import DateMixin, BaseModel, str256, str50, str100


class SourceModel(BaseModel, DateMixin):
    __tablename__ = "source"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str256]
    type: Mapped[str50]
    ip_address: Mapped[str50]
    port: Mapped[int]
    login: Mapped[str100] = mapped_column(nullable=True)
    password: Mapped[str100] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    disabled: Mapped[bool]
    connected: Mapped[bool]
    protocol: Mapped[str100]
    path_to_resource: Mapped[str100]
