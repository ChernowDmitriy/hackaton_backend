from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from core.db.models.addresses import AddressModel
from core.db.models.predictions import PredictionModel
from src.backend.common.interfaces.prediction import PredictionReader
from src.backend.services.paginator import Paginator


class PredictionReaderRep(PredictionReader):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.paginator = Paginator

    async def list_predictions_with_coords(self, *args, **kwargs):
        p = aliased(PredictionModel)
        a = aliased(AddressModel)
        pagination_params = kwargs.get('pagination_params')
        request = kwargs.get('request')
        stmt = select(p, a).join(a, p.unom == a.unom)
        paginator = self.paginator(stmt,
                                   pagination_params,
                                   self.session,
                                   f'{request.base_url}api/v1/predictions')
        paginated_query_result = await paginator.paginate()
        paginated_response = paginator.build_response(paginated_query_result.fetchall())
        return paginated_response
