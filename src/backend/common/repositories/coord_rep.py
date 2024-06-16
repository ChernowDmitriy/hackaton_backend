from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from core.db.models.addresses import AddressModel
from src.backend.common.interfaces.coord import CoordReader
from src.backend.services.paginator import Paginator, PaginationResponse


class CoordinatesReaderRep(CoordReader):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.paginator = Paginator

    async def list_unom_with_coord(self, **kwargs) -> PaginationResponse:
        a = aliased(AddressModel)
        stmt = select(a).order_by(a.id.desc())

        pagination_params = kwargs.get('pagination_params')
        request = kwargs.get('request')

        paginator = self.paginator(stmt,
                                   pagination_params,
                                   self.session,
                                   f'{request.base_url}api/v1/unoms/coords')
        paginated_query_result = await paginator.paginate()
        paginated_response = paginator.build_response(paginated_query_result.scalars().all())
        return paginated_response
