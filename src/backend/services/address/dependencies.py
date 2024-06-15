from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db.dependencies import get_db_session
from src.backend.common.interfaces.coord import CoordReader
from src.backend.common.repositories.address_rep import AddressReaderRep
from src.backend.services.address.address_service import AddressReaderUseCase


async def get_address_reader_rep(
    session: AsyncSession = Depends(get_db_session),
) -> AddressReaderRep:
    return AddressReaderRep(session)


async def get_address_reader_use_case(
    repository: CoordReader = Depends(get_address_reader_rep)
):
    return AddressReaderUseCase(repository)
