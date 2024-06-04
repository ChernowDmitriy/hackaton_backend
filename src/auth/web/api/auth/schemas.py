from typing import Optional

from pydantic import BaseModel, Field

from src.auth.common.schemas import TokenSchema


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserRegisterSchema(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = Field(None)
    email: str
    password: str


class SuccessLoginSchema(TokenSchema):
    pass


class RefreshTokenSchema(BaseModel):
    refresh_token: str


class SuccessRefreshTokenSchema(TokenSchema):
    pass


class SuccessRegistrationSchemaOutput(TokenSchema):
    pass
