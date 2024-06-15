from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from core.db.models.addresses import AddressModel
from src.backend.common.interfaces.coord import CoordReader
from src.backend.services.paginator import Paginator, PaginationResponse


class AddressReaderRep(CoordReader):
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
        paginated_response = await paginator.paginate()
        return paginated_response

    async def coord_item(self) -> AddressModel:
        pass
