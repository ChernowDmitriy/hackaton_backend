from abc import ABC, abstractmethod
from typing import List

from core.db.models.addresses import AddressModel


class CoordReader(ABC):
    @abstractmethod
    async def list_unom_with_coord(self, **kwargs) -> List[AddressModel]:
        ...

    @abstractmethod
    async def coord_item(self) -> AddressModel:
        ...


class CoordReaderUseCase(ABC):
    @abstractmethod
    async def get_unoms_with_coords(self, *args, **kwargs):
        ...
