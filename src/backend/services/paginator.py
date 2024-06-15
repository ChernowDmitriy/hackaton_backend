from typing import TypeVar, Annotated, Optional, Generic

from pydantic import BaseModel, Field
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')


class PaginationParams(BaseModel):
    page: Annotated[int, Field(strict=True, ge=1)] = 1
    page_size: Annotated[int, Field(strict=True, ge=100, le=1000)] = 1000


class PaginationResponse(BaseModel):
    next_page: Optional[str]
    previous_page: Optional[str]
    pages_count: int
    count: int
    data: list


class Paginator(Generic[T]):
    def __init__(self, query, params: PaginationParams, session: AsyncSession, base_url: str):
        self.query = query
        self.params = params
        self.session = session
        self.base_url = base_url

    async def paginate(self) -> PaginationResponse:
        offset = (self.params.page - 1) * self.params.page_size
        total_query = select(func.count()).select_from(self.query.subquery())
        total_result = await self.session.execute(total_query)
        total = total_result.scalar_one()

        if total == 0:
            return PaginationResponse(
                next_page="",
                previous_page="",
                pages_count=0,
                count=0,
                data=[]
            )

        items = await self.session.scalars(
            self.query.offset(offset).limit(self.params.page_size)
        )
        items = items.all()

        next_page = self.params.page + 1 if total > offset + self.params.page_size else None
        prev_page = self.params.page - 1 if self.params.page > 1 else None

        next_page_url = f"{self.base_url}?page={next_page}&page_size={self.params.page_size}" if next_page else None
        prev_page_url = f"{self.base_url}?page={prev_page}&page_size={self.params.page_size}" if prev_page else None

        return PaginationResponse(
            next_page=next_page_url,
            previous_page=prev_page_url,
            pages_count=(total + self.params.page_size - 1) // self.params.page_size,
            count=total,
            data=items
        )
