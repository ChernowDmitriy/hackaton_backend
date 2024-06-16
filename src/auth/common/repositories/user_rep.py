from __future__ import annotations

import uuid
from typing import Type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core.db.models.user import UserModel
from src.auth.common.interfacies.user_protocol import UserContainer
from src.auth.common.schemas import PartialUserUpdateSchema
from src.auth.web.api.auth.schemas import UserRegisterSchema


class UserRepository(UserContainer):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_pk(self, pk) -> Type[UserModel] | None:
        user = await self.session.get(UserModel, pk)
        return user

    async def get_user_by_email(self, email: str) -> Type[UserModel] | None:
        query = select(UserModel).filter_by(email=email)
        executed = await self.session.execute(query)
        return executed.scalar_one_or_none()

    async def update_user_by_id(
        self,
        data: PartialUserUpdateSchema,
        user_id: uuid.UUID,
    ) -> None:
        """
        Partial update the user model. Add the obj to the session state.
        @param data: the data for update the instance
        @param user_id: user ID
        @return: None
        """
        user = await self.session.get(UserModel, user_id)
        for key, value in data.model_dump(exclude_none=True).items():
            setattr(user, key, value)
        self.session.add(user)

    async def get_user(self, user_id: int) -> Type[UserModel] | None:
        """
        Getting a user object with roles and permissions
        @param user_id: user ID
        @return: Type[UserModel] | None
        """
        query = await self.session.execute(
            select(
                UserModel,
            ).filter_by(id=int(user_id))
        )

        return query.scalar_one_or_none()

    async def create_user(self, data: UserRegisterSchema) -> UserModel:
        """
        Creating a user object and add to UoW store
        :param data: UserRegisterSchema
        :return: UserModel
        """
        user = UserModel(**data.model_dump())
        self.session.add(user)
        return user
