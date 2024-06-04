import uuid

from src.auth.common.exceptions import UserNotFound
from src.auth.common.interfacies.user_protocol import UserContainer


class UserService:
    def __init__(self, user_repo: UserContainer):
        self.user_repo = user_repo

    async def get_user_by_id(self, user_id: uuid.UUID):
        user = await self.user_repo.get_user(user_id)

        if user is None:
            raise UserNotFound

        return user
