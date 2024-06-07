from fastapi import APIRouter, UploadFile, status

router = APIRouter()


@router.post("",
             status_code=status.HTTP_201_CREATED,
             description="Загрузить датасет")
async def upload_file(
        file: UploadFile,
):
    return 1
