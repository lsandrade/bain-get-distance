from typing import Tuple

from haversine import haversine

from src.interfaces.idistance_calculator_service import IDistanceCalculatorService


class HaversineDistanceCalculatorService(IDistanceCalculatorService):
    def calculate_distance(self, coordinates1: Tuple[float, float], coordinates2: Tuple[float, float]) -> float:
        return haversine(coordinates1, coordinates2)
