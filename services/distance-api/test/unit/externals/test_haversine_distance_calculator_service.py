from unittest import TestCase

from src.externals.haversine_distance_calculator_service import HaversineDistanceCalculatorService


class TestHaversineDistanceCalculatorService(TestCase):
    service = HaversineDistanceCalculatorService()

    def test_should_calculate_distance(self):
        coordinates1 = (-23.588068, -46.656419)
        coordinates2 = (-25.588068, -41.656419)
        result = self.service.calculate_distance(coordinates1, coordinates2)
        assert 552.24 <= result <= 552.25
