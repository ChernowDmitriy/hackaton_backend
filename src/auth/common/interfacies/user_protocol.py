from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, Type

from core.db.models.user import UserModel


class UserReader(Protocol):
    @abstractmethod
    async def get_user_by_pk(self, *args, **kwargs) -> Type[UserModel] | None:
        ...

    @abstractmethod
    async def get_user_by_email(self, *args, **kwargs) -> Type[UserModel] | None:
        ...

    @abstractmethod
    async def get_user(self, *args, **kwargs) -> Type[UserModel] | None:
        ...


class UserUpdater(Protocol):
    @abstractmethod
    async def update_user_by_id(self, *args, **kwargs) -> None:
        ...


class UserCreator(Protocol):
    @abstractmethod
    async def create_user(self, *args, **kwargs) -> UserModel:
        ...


class UserContainer(
    UserReader,
    UserUpdater,
    UserCreator,
    ABC,
):
    pass
