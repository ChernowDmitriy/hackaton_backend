from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from src.backend.common.interfaces.coord import CoordReader
from src.backend.common.repositories.coord_rep import CoordinatesReaderRep
from src.backend.services.address.address_service import AddressReaderUseCase


async def get_address_reader_rep(
    session: AsyncSession = Depends(get_db_session),
) -> CoordinatesReaderRep:
    return CoordinatesReaderRep(session)


async def get_address_reader_use_case(
    repository: CoordReader = Depends(get_address_reader_rep)
):
    return AddressReaderUseCase(repository)
