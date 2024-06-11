import datetime
from typing import Annotated

from sqlalchemy import text, VARCHAR, BIGINT, Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from core.db.meta import meta

date_with_timezone = Annotated[
    datetime.datetime,
    mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('utc', now())"),
    ),
]

created_at = date_with_timezone
updated_at = Annotated[
    date_with_timezone,
    mapped_column(
        onupdate=datetime.datetime.utcnow,
    ),
]

str50 = Annotated[str, VARCHAR(100)]
str100 = Annotated[str, VARCHAR(100)]
str256 = Annotated[str, VARCHAR(256)]
bigint_pk = Annotated[
    int,
    mapped_column(BIGINT,
                  autoincrement=True,
                  primary_key=True,
                  index=True),
]


class BaseModel(DeclarativeBase):
    """Base for all models."""

    type_annotation_map = {
        int: BIGINT,
        datetime: TIMESTAMP(timezone=True),
        bool: Boolean,
    }

    metadata = meta


class DateMixin(AbstractConcreteBase):
    created_at: Mapped[created_at]
    modify_at: Mapped[updated_at]
