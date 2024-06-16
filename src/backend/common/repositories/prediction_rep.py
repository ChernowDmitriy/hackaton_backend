from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased

from core.db.models.address_register_of_real_estate_objects import AddressRegisterOfRealEstateObjectsModel
from core.db.models.addresses import AddressModel
from core.db.models.predictions import PredictionModel
from src.backend.common.interfaces.prediction import PredictionReader
from src.backend.services.paginator import Paginator, PaginationResponse


class PredictionReaderRep(PredictionReader):
    def __init__(self, session: AsyncSession):
        self.session = session
        self.paginator = Paginator

    async def list_predictions_with_coords(self, *args, **kwargs) -> PaginationResponse:
        p = aliased(PredictionModel)
        a = aliased(AddressModel)
        adr_obj = aliased(AddressRegisterOfRealEstateObjectsModel)

        pagination_params = kwargs.get('pagination_params')
        request = kwargs.get('request')
        search_address = kwargs.get('address')
        area = kwargs.get("areas")

        base_url = f'{request.base_url}api/v1/predictions'

        stmt = select(
            p, a, adr_obj
        ).join(
            a,
            p.unom == a.unom
        ).join(
            adr_obj,
            p.unom == adr_obj.unom
        ).order_by(
            adr_obj.address.asc()
        )
        if search_address:
            stmt = stmt.filter(adr_obj.address.ilike(f"%{search_address}%"))
            base_url = base_url + f"?address={search_address}"

        if area:
            stmt = stmt.filter(p.area.ilike(f"%{area}%"))
            if "?" in base_url:
                base_url = base_url + f"&area={area}"
            else:
                base_url = base_url + f"?area={area}"

        paginator = self.paginator(stmt,
                                   pagination_params,
                                   self.session,
                                   base_url)
        paginated_query_result = await paginator.paginate()
        if isinstance(paginated_query_result, PaginationResponse):
            return paginated_query_result
        paginated_response = paginator.build_response(paginated_query_result.fetchall())
        return paginated_response

    async def get_list_available_areas(self, *args, **kwargs):
        p = aliased(PredictionModel)
        stmt = select(p.area)
        result = await self.session.scalars(stmt)
        return result.all()
