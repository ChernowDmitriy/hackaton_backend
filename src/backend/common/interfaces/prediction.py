from abc import ABC, abstractmethod


class PredictionReader(ABC):
    @abstractmethod
    async def list_predictions_with_coords(self, *args, **kwargs):
        ...

    @abstractmethod
    async def get_list_available_areas(self, *args, **kwargs):
        ...


class IPredictionReaderUseCase(ABC):
    @abstractmethod
    async def list_predictions_with_coords(self, *args, **kwargs):
        ...

    @abstractmethod
    async def get_list_available_areas(self, *args, **kwargs):
        ...
