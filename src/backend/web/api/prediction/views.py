from typing import Optional, Union, List

from fastapi import APIRouter, Depends, Request

from src.backend.common.interfaces.prediction import IPredictionReaderUseCase
from src.backend.services.paginator import PaginationResponse
from src.backend.services.prediction.dependencies import get_prediction_reader_use_case
from src.backend.web.api.prediction.schemas import PredictionsPaginationParams, PredictionSchemaOutput, \
    CoordinatesSchema

router = APIRouter()


@router.get("", response_model=PaginationResponse)
async def get_predictions(
        request: Request,
        address: Optional[str] = None,
        area: Optional[str] = None,
        page: Optional[int] = 1,
        page_size: Optional[int] = 30,
        use_case: IPredictionReaderUseCase = Depends(get_prediction_reader_use_case)
):
    pagination_params = PredictionsPaginationParams(
        page=page,
        page_size=page_size
    )
    paginated_result = await use_case.list_predictions_with_coords(request=request,
                                                                   pagination_params=pagination_params,
                                                                   address=address,
                                                                   areas=area)
    if not paginated_result.count:
        return paginated_result
    data = [
        PredictionSchemaOutput(
            id=prediction.id,
            unom=prediction.unom,
            district=prediction.district,
            building_material=prediction.building_material,
            building_assignment=prediction.building_assignment,
            building_total_area=prediction.building_total_area,
            area=prediction.area,
            project_number=prediction.project_number,
            building_class=prediction.building_class,
            floors_number=prediction.floors_number,
            entrances_number=prediction.entrances_number,
            apartments_number=prediction.apartments_number,
            heat_supply_volume=prediction.heat_supply_volume,
            heat_reverse_supply_volume=prediction.heat_reverse_supply_volume,
            backflow_difference=prediction.backflow_difference,
            leakage_difference=prediction.leakage_difference,
            supply_temperature=prediction.supply_temperature,
            return_temperature=prediction.return_temperature,
            counter_hours=prediction.counter_hours,
            heat_energy_consumption=prediction.heat_energy_consumption,
            municipal_district=prediction.municipal_district,
            emergency_status=prediction.emergency_status,
            total_area=prediction.total_area,
            total_area_lived_spaced=prediction.total_area_lived_spaced,
            total_area_unlived_spaced=prediction.total_area_unlived_spaced,
            depreciation=prediction.depreciation,
            wall_material=prediction.wall_material,
            freight_elevators_number=prediction.freight_elevators_number,
            housing_type=prediction.housing_type,
            elevators_number=prediction.elevators_number,
            mkd_status=prediction.mkd_status,
            occurrence_year=prediction.occurrence_year,
            occurrence_month=prediction.occurrence_month,
            occurrence_day=prediction.occurrence_day,
            predicted_label=prediction.predicted_label,
            prediction_title=prediction.prediction_title,
            address=adr_objs.address,
            coordinates=CoordinatesSchema(
                latitude=coordinates.latitude,
                longitude=coordinates.longitude
            )
        ) for prediction, coordinates, adr_objs in paginated_result.data
    ]
    paginated_result.data = data
    available_areas = await use_case.get_list_available_areas()
    paginated_result.metadata = {
        "available_areas": available_areas
    }
    return paginated_result
