from abc import abstractmethod, ABC

from src.auth.common.schemas import TokenSchema


class AuthorizationProtocol(ABC):
    @abstractmethod
    async def authorize(self, *args, **kwargs) -> TokenSchema:
        ...

    @abstractmethod
    async def refresh_token(self, *args, **kwargs) -> TokenSchema:
        ...

    @abstractmethod
    async def register(self, *args, **kwargs) -> TokenSchema:
        ...
