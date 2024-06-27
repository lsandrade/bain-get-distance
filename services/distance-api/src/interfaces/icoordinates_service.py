from abc import abstractmethod, ABC
from typing import Tuple


class ICoordinatesService(ABC):

    @abstractmethod
    def get_coordinates(self, address: str) -> Tuple[float, float]:
        pass
