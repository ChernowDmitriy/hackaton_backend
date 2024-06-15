from typing import Optional, Annotated

from pydantic import BaseModel, Field

from src.backend.services.paginator import PaginationParams


class CoordinatesSchema(BaseModel):
    latitude: Optional[str] = Field(None)
    longitude: Optional[str] = Field(None)


class PredictionSchemaOutput(BaseModel):
    id: int
    unom: Optional[int] = Field(None)
    building_material: Optional[str] = Field(None)
    building_assignment: Optional[str] = Field(None)
    building_class: Optional[str] = Field(None)
    building_floors_number: Optional[int] = Field(None)
    heat_supply_volume: Optional[float] = Field(None)
    heat_reverse_supply_volume: Optional[float] = Field(None)
    backflow_difference: Optional[float] = Field(None)
    leakage_difference: Optional[float] = Field(None)
    supply_temperature: Optional[float] = Field(None)
    return_temperature: Optional[float] = Field(None)
    counter_hours: Optional[float] = Field(None)
    heat_energy_consumption: Optional[float] = Field(None)
    series_number_meter: Optional[float] = Field(None)
    floors_count: Optional[int] = Field(None)
    entrance_count: Optional[int] = Field(None)
    apartment_count: Optional[int] = Field(None)
    total_area: Optional[float] = Field(None)
    total_living_area: Optional[float] = Field(None)
    object_deprecation_bti: Optional[float] = Field(None)
    material_wall: Optional[float] = Field(None)
    building_failure_sign_of: Optional[float] = Field(None)
    elevators_number: Optional[int] = Field(None)
    roofing_material_bti: Optional[float] = Field(None)
    mkd_status: Optional[float] = Field(None)
    predictions: Optional[float] = Field(None)
    predicted_labels: Optional[str] = Field(None)
    prediction_title: Optional[str] = Field(None)
    coordinates: CoordinatesSchema


class PredictionsPaginationParams(PaginationParams):
    page: Annotated[int, Field(strict=True, ge=1)] = 1
    page_size: Annotated[int, Field(strict=True, ge=30, le=300)] = 30
