from typing import List

from core.db.models.reactions import ReactionsModel
from src.backend.common.interfaces.reaction import IReactionListUseCase, ReactionReader


class ReactionListUseCase(IReactionListUseCase):
    def __init__(self, repository: ReactionReader):
        self.repository = repository

    async def get_list_reactions(self, *args, **kwargs) -> List[ReactionsModel]:
        result = await self.repository.list_reactions(**kwargs)
        return result
