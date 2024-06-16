from datetime import datetime, timedelta
from enum import Enum

import jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Request
from jwt import DecodeError, ExpiredSignatureError
from passlib.context import CryptContext

from core.settings import get_settings
from src.auth.common.exceptions import (SignatureVerificationFailed,
                                        AccessForbiddenException)
from src.auth.common.schemas import TokenSchema
from core.db.models.user import UserModel


class JWTGrantType(str, Enum):
    ACCESS_TOKEN = "access"
    REFRESH_TOKEN = "refresh"


class SecurityService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    settings = get_settings()

    def create_auth_tokens(self, user: UserModel) -> TokenSchema:
        exp_access = datetime.utcnow() + timedelta(
            minutes=self.settings.ACCESS_TOKEN_EXPIRE,
        )
        exp_refresh = datetime.utcnow() + timedelta(
            minutes=self.settings.REFRESH_TOKEN_EXPIRE,
        )
        iat = datetime.utcnow()

        access_token_payload = {
            "sub": int(user.id),
            "grant_type": JWTGrantType.ACCESS_TOKEN,
            "exp": exp_access,
            "iat": iat,
        }

        refresh_token_payload = {
            "sub": int(user.id),
            "exp": exp_refresh,
            "grant_type": JWTGrantType.REFRESH_TOKEN,
            "iat": iat,
        }
        access_token = jwt.encode(
            access_token_payload,
            self.settings.JWT_SECRET_KEY,
            algorithm="HS256",
        )
        refresh_token = jwt.encode(
            refresh_token_payload,
            self.settings.JWT_SECRET_KEY,
            algorithm="HS256",
        )
        return TokenSchema(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
        )

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)

    def verify_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.settings.JWT_SECRET_KEY, algorithms="HS256")
            return payload
        except (ExpiredSignatureError, DecodeError):
            raise SignatureVerificationFailed


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.security_service = SecurityService()
        self.WHITE_LIST = [
            "/api/v1/auth/login",
            "/api/v1/auth/refresh_token",
            "/api/v1/auth/register",
            "/api/v1/docs",
            "/api/v1/files/*"
        ]

    async def __call__(self, request: Request):
        for pattern in self.WHITE_LIST:
            if (pattern.endswith("*") and request.url.path.startswith(pattern[:-1]) or
                    request.url.path in self.WHITE_LIST):
                return
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self).__call__(request)
        payload = self.security_service.verify_token(credentials.credentials)
        grant_type = payload.get("grant_type")
        if grant_type == JWTGrantType.REFRESH_TOKEN:
            raise AccessForbiddenException
        user_id = payload.get("sub")
        if not user_id:
            raise AccessForbiddenException
        request.state.user_id = user_id
        return credentials
