from unittest import TestCase
from unittest.mock import Mock

from src.use_cases.distance_calculator_use_cases import DistanceCalculatorUseCases


class TestDistanceCalculatorUseCases(TestCase):
    coords_service = Mock()
    distance_service = Mock()

    def test_should_calculate_distance(self):
        self.coords_service.get_coordinates.return_value = (0, 0)
        self.distance_service.calculate_distance.return_value = 10.0
        result = DistanceCalculatorUseCases.get_distance(
            coordinates_service=self.coords_service,
            distance_service=self.distance_service,
            address1='address1',
            address2='address2'
        )
        self.coords_service.get_coordinates.assert_any_call('address1')
        self.coords_service.get_coordinates.assert_any_call('address2')
        self.distance_service.calculate_distance.assert_called_with((0, 0), (0, 0))
        assert result == 10.0

    def test_should_save_historical_distance(self):
        gateway = Mock()
        gateway.save_historical_distance.return_value = None
        DistanceCalculatorUseCases.save_historical_distance(
            gateway=gateway,
            address1='address1',
            address2='address2',
            distance=10.0
        )
        gateway.save_historical_distance.assert_called_with(address1='address1', address2='address2', distance=10.0)
        assert gateway.save_historical_distance.called
