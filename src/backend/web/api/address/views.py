from typing import Optional

from fastapi import APIRouter, Depends, Request

from src.backend.common.interfaces.coord import CoordReaderUseCase
from src.backend.services.address.dependencies import get_address_reader_use_case
from src.backend.services.paginator import PaginationParams
from src.backend.web.api.address.schemas import UnomsCoordsSchema

router = APIRouter()


@router.get('/coords')
async def get_unoms_with_coords(
        request: Request,
        page: Optional[int] = 1,
        page_size: Optional[int] = 1000,
        use_case: CoordReaderUseCase = Depends(get_address_reader_use_case)
):
    pagination_params = PaginationParams(
        page=page,
        page_size=page_size
    )
    result = await use_case.get_unoms_with_coords(request=request, pagination_params=pagination_params)
    result.data = [UnomsCoordsSchema.model_validate(row, from_attributes=True) for row in result.data]
    return result
