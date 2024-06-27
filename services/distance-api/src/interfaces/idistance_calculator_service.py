from abc import abstractmethod, ABC
from typing import Tuple


class IDistanceCalculatorService(ABC):
    @abstractmethod
    def calculate_distance(self, coordinates1: Tuple[float, float], coordinates2: Tuple[float, float]) -> float:
        pass
