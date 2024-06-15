from typing import Optional

from fastapi import APIRouter, Depends, Request

from src.backend.common.interfaces.prediction import IPredictionReaderUseCase
from src.backend.services.prediction.dependencies import get_prediction_reader_use_case
from src.backend.web.api.prediction.schemas import PredictionsPaginationParams, PredictionSchemaOutput, \
    CoordinatesSchema

router = APIRouter()


@router.get("")
async def get_predictions(
        request: Request,
        page: Optional[int] = 1,
        page_size: Optional[int] = 30,
        use_case: IPredictionReaderUseCase = Depends(get_prediction_reader_use_case)
):
    pagination_params = PredictionsPaginationParams(
        page=page,
        page_size=page_size
    )
    paginated_result = await use_case.list_predictions_with_coords(request=request, pagination_params=pagination_params)
    data = []
    for prediction, coordinates in paginated_result.data:
        data.append(
            PredictionSchemaOutput(
                id=prediction.id,
                unom=prediction.unom,
                predicted_labels=prediction.predicted_labels,
                coordinates=CoordinatesSchema(
                    latitude=coordinates.latitude,
                    longitude=coordinates.longitude
                )
            ).model_dump(exclude_none=True)
        )
    paginated_result.data = data
    return paginated_result
