from src.backend.common.interfaces.coord import CoordReaderUseCase, CoordReader


class AddressReaderUseCase(CoordReaderUseCase):
    def __init__(self, repository: CoordReader):
        self.repository = repository

    async def get_unoms_with_coords(self, **kwargs):
        result = await self.repository.list_unom_with_coord(**kwargs)
        return result
