from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from src.backend.common.interfaces.prediction import IPredictionReaderUseCase, PredictionReader
from src.backend.common.repositories.prediction_rep import PredictionReaderRep
from src.backend.services.prediction.prediction_service import PredictionReaderUseCase


async def get_prediction_reader_rep(
    session: AsyncSession = Depends(get_db_session),
) -> PredictionReader:
    return PredictionReaderRep(session)


async def get_prediction_reader_use_case(
    repository: PredictionReader = Depends(get_prediction_reader_rep)
) -> IPredictionReaderUseCase:
    return PredictionReaderUseCase(repository)
