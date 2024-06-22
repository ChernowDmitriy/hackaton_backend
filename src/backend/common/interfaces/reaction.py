from abc import ABC, abstractmethod
from typing import List

from core.db.models.reactions import ReactionsModel


class IReactionListUseCase(ABC):
    @abstractmethod
    async def get_list_reactions(self, *args, **kwargs) -> List[ReactionsModel]:
        ...


class ReactionReader(ABC):
    @abstractmethod
    async def list_reactions(self, *args, **kwargs):
        ...
