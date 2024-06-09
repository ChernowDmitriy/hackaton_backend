import dataclasses
from typing import Any, List

from fastapi.responses import UJSONResponse
from pydantic import BaseModel
from starlette import status


class CoreError(Exception):
    pass


@dataclasses.dataclass
class BaseHTTPException(Exception):
    status_code: int
    msg: Any

    def __post_init__(self):
        self.msg = {"error_message": self.msg}


class ParamsSchema(BaseModel):
    parameter: str
    message: str


class BaseValidationErrorResponse(BaseModel):
    errors: List[ParamsSchema]


async def request_exception_handler(_, exc):
    return UJSONResponse(status_code=exc.status_code, content=exc.msg)


async def validation_exception_handler(_, exc):
    content = BaseValidationErrorResponse(
        errors=[
            ParamsSchema(
                parameter=item.get("loc")[-1],
                message=item.get('ctx').get('error').__str__() if item.get('ctx') else item.get('msg')
            )
            for item in exc.errors()]
    )
    return UJSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=content.model_dump(mode="json"))
