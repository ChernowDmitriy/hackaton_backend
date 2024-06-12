import datetime

import aiofiles
import pandas as pd

from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from core.tkq import broker

router = APIRouter()


@broker.task
async def process_file(file_path: str):
    # Process the file here (e.g., read the file, process data)
    print('=' * 254)
    print(f"Processing file: {file_path}")


@router.post("",
             description="Загрузить датасет")
async def upload_file(
        file: UploadFile = File(...),
):
    # Save the uploaded file to disk
    async with aiofiles.open(f"/tmp/{file.filename}", 'wb') as out_file:
        content = await file.read()  # async read
        await out_file.write(content)  # async write

    # Enqueue the task to process the file
    await process_file.kiq(f"/tmp/{file.filename}")

    return {"filename": file.filename, "status": "File uploaded and processing started"}


def convert_to_datetime(date_str):
    if not date_str:
        return None
    if str(date_str) == 'nan':
        return None
    return datetime.datetime.strptime(str(date_str), '%Y-%m-%d %H:%M:%S.%f')


def convert_to_datetime_1(date_str):
    if not date_str:
        return None
    if str(date_str) == 'nan':
        return None
    print(date_str, type(date_str))
    return datetime.datetime.strptime(str(date_str), '%Y-%m-%d %H:%M:%S')


def convert_to_stmt(value):
    try:
        if value == 'nan':
            return None
        return int(value)
    except:
        return None


def convert_to_float(value):
    if value == 'nan':
        return None
    new_v = value.replace(',', '.')
    return float(new_v)


@router.get("/hello")
async def hello(
        session: AsyncSession = Depends(get_db_session)
):
    import pandas as pd

    file_path = '/app/src/script/9.xlsx'

    set_9 = pd.read_excel(file_path, header=None, skiprows=2)

    new_columns = ['id', 'city', 'administrative_district', 'municipal_district', 'locality', 'street', 'house_type',
                   'house_numbers', 'housing_numbers', 'building_type_number', 'building_number', 'unom', 'unad',
                   'building_material', 'building_assignment', 'building_class', 'building_type',
                   'building_floors_number', 'building_attribute', 'building_total_area']

    set_9.columns = new_columns

    set_9 = set_9.astype(str)


    # await session.commit()
    return 1
