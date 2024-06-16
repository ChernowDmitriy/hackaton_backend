from datetime import datetime

import pandas as pd
import ujson
from sqlalchemy import create_engine, Insert
from sqlalchemy.orm import sessionmaker

from core.db.models.incidents import IncidentsModel
from core.settings import get_settings
from script.utils import convert_to_datetime, strfloat_to_int


def download_set_5(file_path):
    set_5 = pd.read_excel(file_path, sheet_name="Выгрузка")

    new_columns = ['name', 'source', 'external_system_creation_date', 'closed_at', 'area', "unom",
                   "address", "external_system_closed_date"]

    set_5.columns = new_columns
    set_5 = set_5.astype(str)
    result = [{
                "id": index,
                "name": row["name"],
                "external_system_creation_date": convert_to_datetime(row["external_system_creation_date"]),
                "closed_at": convert_to_datetime(row["closed_at"]),
                "area": row["area"],
                "unom": strfloat_to_int(row["unom"]),
                "address": row["address"],
                "external_system_closed_date": convert_to_datetime(row["external_system_closed_date"]),
            } for index, row in enumerate(set_5.iloc)]

    settings = get_settings()
    engine = create_engine(str(settings.db_url))
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Insert is starting...')
    session.execute(Insert(IncidentsModel), result)
    session.commit()

    # json_file_name = file_path.split(".")[0]
    # with open(f"{json_file_name}.json", 'w') as file:
    #     file.write(ujson.dumps(result, indent=4, ensure_ascii=False, default=str))


download_set_5('set_5_1.xlsx')
