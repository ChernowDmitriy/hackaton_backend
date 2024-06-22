import pandas as pd
from sqlalchemy import create_engine, Insert
from sqlalchemy.orm import sessionmaker

from core.db.models.reactions import ReactionsModel
from core.settings import get_settings
from script.utils import strfloat_to_int


def download_set_5(file_path):
    set_5 = pd.read_csv(file_path)

    set_5 = set_5.astype(str)
    result = [{
                "id": index,
                "tp_number": row["tp_number"],
                "address_tp": row["address_tp"],
                "heat_supply_source": row["heat_supply_source"],
                "short_address": row["short_address"],
                "unom": strfloat_to_int(row["unom"]),
                "ods_number": row["ods_number"],
                "ods_address": row["ods_address"],
                "consumer": row["consumer"],
                "geodata_y": row["geodata_y"],
                "geodata_center_y": row["geodata_center_y"],
            } for index, row in enumerate(set_5.iloc)]

    settings = get_settings()
    engine = create_engine(str(settings.db_url_sync))
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Insert is starting...')
    session.execute(Insert(ReactionsModel), result)
    session.commit()


download_set_5('reaction_data.csv')
