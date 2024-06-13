
import aiofiles

from fastapi import APIRouter, UploadFile, File

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
