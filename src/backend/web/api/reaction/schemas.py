from typing import Annotated, Optional, List

from pydantic import BaseModel, Field

from src.backend.services.paginator import PaginationParams


class ReactionPaginationParams(PaginationParams):
    page: Annotated[int, Field(strict=True, ge=1)] = 1
    page_size: Annotated[int, Field(strict=True, ge=30, le=300)] = 30


class ReactionsSchemasOutput(BaseModel):
    id: int
    tp_number: Optional[str] = Field(None)
    address_tp: Optional[str] = Field(None)
    heat_supply_source: Optional[str] = Field(None)
    short_address: Optional[str] = Field(None)
    unom: Optional[int] = Field(None)
    ods_number: Optional[str] = Field(None)
    ods_address: Optional[str] = Field(None)
    consumer: Optional[str] = Field(None)
