import asyncio

import aiofiles

from fastapi import APIRouter, UploadFile, File


router = APIRouter()


@router.post("/test",
             description="Загрузить датасет")
async def upload_file(
        file: UploadFile = File(...),
):
    # Save the uploaded file to disk
    # async with aiofiles.open(f"/tmp/{file.filename}", 'wb') as out_file:
    #     content = await file.read()  # async read
    #     await out_file.write(content)  # async write

    # Enqueue the task to process the file
    # await process_file.kiq(f"/tmp/{file.filename}")
    task = await add_one.kiq(1)
    # Wait for the result.
    result = await task.wait_result(timeout=2)
    return {"filename": file.filename, "status": "File uploaded and processing started"}
