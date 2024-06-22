from typing import Optional

from fastapi import APIRouter, Depends, Request

from src.backend.common.interfaces.reaction import IReactionListUseCase
from src.backend.services.reaction.dependencies import get_reaction_list_use_case
from src.backend.web.api.reaction.schemas import ReactionPaginationParams, ReactionsSchemasOutput

router = APIRouter()


@router.get("")
async def list_reactions(
        request: Request,
        page: Optional[int] = 1,
        page_size: Optional[int] = 30,
        service: IReactionListUseCase = Depends(get_reaction_list_use_case)
):
    pagination_params = ReactionPaginationParams(
        page=page,
        page_size=page_size
    )
    paginated_result = await service.get_list_reactions(request=request,
                                                        pagination_params=pagination_params)

    if not paginated_result.count:
        return paginated_result
    data = [ReactionsSchemasOutput.model_validate(row, from_attributes=True) for row in paginated_result.data]
    paginated_result.data = data
    return paginated_result
