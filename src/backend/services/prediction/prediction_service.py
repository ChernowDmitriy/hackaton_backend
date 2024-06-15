from src.backend.common.interfaces.prediction import PredictionReader, IPredictionReaderUseCase


class PredictionReaderUseCase(IPredictionReaderUseCase):
    def __init__(self, repository: PredictionReader):
        self.repository = repository

    async def list_predictions_with_coords(self, *args, **kwargs):
        result = await self.repository.list_predictions_with_coords(**kwargs)
        return result
