from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from core.db.models.reactions import ReactionsModel
from src.backend.common.interfaces.reaction import ReactionReader
from src.backend.services.paginator import Paginator, PaginationResponse


class ReactionReaderRep(ReactionReader):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.paginator = Paginator

    async def list_reactions(self, *args, **kwargs) -> PaginationResponse | Any:
        pagination_params = kwargs.get('pagination_params')
        request = kwargs.get('request')
        base_url = f'{request.base_url}api/v1/reactions'
        r = aliased(ReactionsModel)
        stmt = select(r).order_by(r.short_address.asc())
        paginator = self.paginator(stmt,
                                   pagination_params,
                                   self.session,
                                   base_url)

        paginated_query_result = await paginator.paginate()
        if isinstance(paginated_query_result, PaginationResponse):
            return paginated_query_result
        paginated_response = paginator.build_response(paginated_query_result.scalars().all())
        return paginated_response
