from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from src.backend.common.interfaces.reaction import ReactionReader, IReactionListUseCase
from src.backend.common.repositories.reaction_rep import ReactionReaderRep
from src.backend.services.reaction.reaction_service import ReactionListUseCase


async def get_reaction_reader_rep(
        session: AsyncSession = Depends(get_db_session),
) -> ReactionReaderRep:
    return ReactionReaderRep(session)


async def get_reaction_list_use_case(
        repository: ReactionReader = Depends(get_reaction_reader_rep)
) -> IReactionListUseCase:
    return ReactionListUseCase(repository)
