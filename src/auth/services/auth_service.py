from src.auth.common.exceptions import LoginFailedException, RefreshTokenFailedException, UserAlreadyExistsException
from src.auth.common.interfacies.auth_protocol import AuthorizationProtocol
from src.auth.common.interfacies.user_protocol import UserContainer
from src.auth.common.schemas import PartialUserUpdateSchema, TokenSchema
from src.auth.services.security import SecurityService, JWTGrantType
from src.auth.web.api.auth.schemas import UserLoginSchema, RefreshTokenSchema, UserRegisterSchema


class AuthService(AuthorizationProtocol):
    def __init__(
        self,
        user_repo: UserContainer,
    ):
        self.security_service = SecurityService()
        self.user_repo = user_repo

    async def authorize(self, data: UserLoginSchema) -> TokenSchema:
        user = await self.user_repo.get_user_by_email(data.email)

        if user is None:
            print(1)
            raise LoginFailedException

        if not self.security_service.verify_password(data.password, user.password):
            print(data.password)
            print(user.password)
            raise LoginFailedException

        response = self.security_service.create_auth_tokens(user)
        await self.user_repo.update_user_by_id(
            PartialUserUpdateSchema(
                refresh_token=response.refresh_token,
            ),
            user.id,
        )
        await self.user_repo.session.commit()
        return response

    async def refresh_token(self, data: RefreshTokenSchema) -> TokenSchema:
        payload = self.security_service.verify_token(data.refresh_token)

        user_id = payload.get("sub")
        grant_type = payload.get("grant_type")

        if grant_type != JWTGrantType.REFRESH_TOKEN:
            raise RefreshTokenFailedException

        user = await self.user_repo.get_user_by_pk(user_id)
        user_token = user.refresh_token

        if user is None:
            raise RefreshTokenFailedException

        if data.refresh_token != user.refresh_token or (
            not self.security_service.verify_token(data.refresh_token)
            or not self.security_service.verify_token(user_token)
        ):
            raise RefreshTokenFailedException

        auth_tokens = self.security_service.create_auth_tokens(user)
        await self.user_repo.update_user_by_id(
            PartialUserUpdateSchema(
                refresh_token=auth_tokens.refresh_token,
            ),
            user.id,
        )
        await self.user_repo.session.commit()
        return auth_tokens

    async def register(self, data: UserRegisterSchema) -> TokenSchema:
        user = await self.user_repo.get_user_by_email(data.email)
        if user:
            raise UserAlreadyExistsException

        auth_data = UserLoginSchema(email=data.email, password=data.password)
        hashed_password = self.security_service.hash_password(data.password)
        data.password = hashed_password

        new_user = await self.user_repo.create_user(data)
        await self.user_repo.session.commit()
        await self.user_repo.session.refresh(new_user)

        result = await self.authorize(auth_data)
        return result
