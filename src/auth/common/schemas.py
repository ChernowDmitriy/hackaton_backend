from typing import Optional

from pydantic import BaseModel, Field


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class PartialUserUpdateSchema(BaseModel):
    first_name: Optional[str] = Field(None)
    last_jake: Optional[str] = Field(None)
    middle_name: Optional[str] = Field(None)
    refresh_token: Optional[str] = Field(None)
