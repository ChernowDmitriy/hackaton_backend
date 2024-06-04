from fastapi import APIRouter, Depends

from starlette.responses import FileResponse

from src.IR_Test.services.file.dependencies import get_file_service
from src.IR_Test.services.file.file_service import FileService

router = APIRouter()


@router.get("/files/{filename}",
            include_in_schema=False)
async def get_image(
    filename: str,
    service: FileService = Depends(get_file_service)
):
    file_path = service.get_file_path_by_name(filename)
    return FileResponse(file_path)
