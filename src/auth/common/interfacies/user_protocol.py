from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, Type

from core.db.models.user import UserModel


class UserReader(Protocol):
    @abstractmethod
    async def get_user_by_pk(self, *args, **kwargs) -> Type[UserModel] | None:
        pass

    @abstractmethod
    async def get_user_by_email(self, *args, **kwargs) -> Type[UserModel] | None:
        pass

    @abstractmethod
    async def get_user(self, *args, **kwargs) -> Type[UserModel] | None:
        pass


class UserUpdater(Protocol):
    @abstractmethod
    async def update_user_by_id(self, *args, **kwargs) -> None:
        pass


class UserContainer(
    UserReader,
    UserUpdater,
    ABC,
):
    pass
