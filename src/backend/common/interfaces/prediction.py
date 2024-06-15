from abc import ABC, abstractmethod


class PredictionReader(ABC):
    @abstractmethod
    async def list_predictions_with_coords(self, *args, **kwargs):
        ...


class IPredictionReaderUseCase(ABC):
    @abstractmethod
    async def list_predictions_with_coords(self, *args, **kwargs):
        ...
