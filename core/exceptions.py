import dataclasses
from typing import Any

from fastapi.responses import UJSONResponse


class CoreError(Exception):
    pass


@dataclasses.dataclass
class BaseHTTPException(Exception):
    status_code: int
    msg: Any

    def __post_init__(self):
        self.msg = {"error_message": self.msg}


def unicorn_exception_handler(_, exc: BaseHTTPException):
    return UJSONResponse(status_code=exc.status_code, content=exc.msg)
