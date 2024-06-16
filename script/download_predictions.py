import pandas as pd
import ujson
from sqlalchemy import create_engine, Insert
from sqlalchemy.orm import sessionmaker

from core.db.models.predictions import PredictionModel
from core.settings import get_settings


def save_to_file():
    file_path = 'predictions.csv'
    set_1 = pd.read_csv(file_path)

    set_1 = set_1.astype(str)

    result = []
    counter = 0
    for row in set_1.iloc:
        counter += 1
        result.append({
            "id": counter,
            "unom": int(float(row['unom'])),
            "district": row["district"],
            "building_material": row['building_material'],
            "building_assignment": row["building_assignment"],
            "building_total_area": int(float(row["building_total_area"])),
            "area": row["area"],
            "project_number": int(float(row["project_number"])),
            "building_class": row["building_class"],
            "floors_number": int(float(row["floors_number"])),
            "entrances_number": int(float(row["entrances_number"])),
            "apartments_number": int(float(row["apartments_number"])),
            "heat_supply_volume": int(float(row["heat_supply_volume"])),
            "heat_reverse_supply_volume": int(float(row["heat_reverse_supply_volume"])),
            "backflow_difference": int(float(row["backflow_difference"])),
            "leakage_difference": int(float(row["leakage_difference"])),
            "supply_temperature": int(float(row["supply_temperature"])),
            "return_temperature": int(float(row["return_temperature"])),
            "counter_hours": int(float(row["counter_hours"])),
            "heat_energy_consumption": int(float(row["heat_energy_consumption"])),
            "municipal_district": row["municipal_district"],
            "emergency_status": int(float(row["emergency_status"])),
            "total_area": int(float(row["total_area"])),
            "total_area_lived_spaced": int(float(row["total_area_lived_spaced"])),
            "total_area_unlived_spaced": int(float(row["total_area_unlived_spaced"])),
            "depreciation": int(float(row["depreciation"])),
            "wall_material": int(float(row["wall_material"])),
            "freight_elevators_number": int(float(row["freight_elevators_number"])),
            "housing_type": int(float(row["housing_type"])),
            "elevators_number": int(float(row["elevators_number"])),
            "mkd_status": int(float(row["mkd_status"])),
            "predicted_label": row["Predicted_Label"],
            "occurrence_year": int(row["occurrence_year"]),
            "occurrence_month": int(row["occurrence_month"]),
            "occurrence_day": int(row["occurrence_day"]),
            "prediction_title": "Прогноз от 15.06.2024",
        })
    settings = get_settings()
    engine = create_engine(str(settings.db_url))
    Session = sessionmaker(bind=engine)
    session = Session()
    session.execute(Insert(PredictionModel), result)
    session.commit()
    # with open("json_data.json", "w") as f:
    #     to_write = ujson.dumps(result, indent=2, ensure_ascii=False)
    #     f.write(to_write)


save_to_file()
