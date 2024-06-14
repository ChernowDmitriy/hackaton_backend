from fastapi import APIRouter, UploadFile, BackgroundTasks, Depends

from src.backend.common.interfaces.file import IUploadFileUseCase
from src.backend.services.file.dependencies import get_file_uploader_use_case

router = APIRouter()


@router.post("/test",
             description="Загрузить датасет")
async def upload_file(
        background_tasks: BackgroundTasks,
        files: list[UploadFile],
        use_case: IUploadFileUseCase = Depends(get_file_uploader_use_case)
):
    for file in files:
        content = await file.read()
        await use_case.upload_file(file, content)
        # background_tasks.add_task(use_case.upload_file, file, content)

    return {"filenames": [file.filename for file in files]}
