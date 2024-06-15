from typing import Optional

from pydantic import BaseModel


class UnomsCoordsSchema(BaseModel):
    unom: int
    latitude: Optional[str]
    longitude: Optional[str]
