from pydantic import BaseModel

from src.auth.common.schemas import TokenSchema


class UserLoginSchema(BaseModel):
    email: str
    password: str


class SuccessLoginSchema(TokenSchema):
    pass


class RefreshTokenSchema(BaseModel):
    refresh_token: str


class SuccessRefreshTokenSchema(TokenSchema):
    pass
