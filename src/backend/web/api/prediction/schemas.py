from typing import Optional, Annotated

from pydantic import BaseModel, Field

from src.backend.services.paginator import PaginationParams


class CoordinatesSchema(BaseModel):
    latitude: Optional[str] = Field(None)
    longitude: Optional[str] = Field(None)


class PredictionSchemaOutput(BaseModel):
    id: int
    unom: Optional[int] = Field(None)
    district: Optional[str] = Field(None)
    building_material: Optional[str] = Field(None)
    building_assignment: Optional[str] = Field(None)
    building_total_area: Optional[int] = Field(None)
    area: Optional[str] = Field(None)
    project_number: Optional[int] = Field(None)
    building_class: Optional[str] = Field(None)
    floors_number: Optional[int] = Field(None)
    entrances_number: Optional[int] = Field(None)
    apartments_number: Optional[int] = Field(None)
    heat_supply_volume: Optional[int] = Field(None)
    heat_reverse_supply_volume: Optional[int] = Field(None)
    backflow_difference: Optional[int] = Field(None)
    leakage_difference: Optional[int] = Field(None)
    supply_temperature: Optional[int] = Field(None)
    return_temperature: Optional[int] = Field(None)
    counter_hours: Optional[int] = Field(None)
    heat_energy_consumption: Optional[int] = Field(None)
    municipal_district: Optional[str] = Field(None)
    emergency_status: Optional[int] = Field(None)
    total_area: Optional[int] = Field(None)
    total_area_lived_spaced: Optional[int] = Field(None)
    total_area_unlived_spaced: Optional[int] = Field(None)
    depreciation: Optional[int] = Field(None)
    wall_material: Optional[int] = Field(None)
    freight_elevators_number: Optional[int] = Field(None)
    housing_type: Optional[int] = Field(None)
    elevators_number: Optional[int] = Field(None)
    mkd_status: Optional[int] = Field(None)
    occurrence_year: Optional[int] = Field(None)
    occurrence_month: Optional[int] = Field(None)
    occurrence_day: Optional[int] = Field(None)
    predicted_label: Optional[str] = Field(None)
    prediction_title: Optional[str] = Field(None)
    address: Optional[str] = Field(None)
    coordinates: CoordinatesSchema


class PredictionsPaginationParams(PaginationParams):
    page: Annotated[int, Field(strict=True, ge=1)] = 1
    page_size: Annotated[int, Field(strict=True, ge=30, le=300)] = 30
