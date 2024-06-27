from unittest import TestCase
from unittest.mock import patch, Mock

from src.controllers.distance_calculator_controller import DistanceCalculatorController


class TestDistanceCalculatorController(TestCase):

    @patch('src.controllers.distance_calculator_controller.DistanceCalculatorUseCases')
    def test_should_get_distance(self, mock_use_cases):
        mock_use_cases.get_distance.return_value = 10.0
        mock_coords_service = Mock()
        mock_distance_service = Mock()
        result = DistanceCalculatorController.get_distance(
            coordinates_service=mock_coords_service,
            distance_service=mock_distance_service,
            address1='address1',
            address2='address2'
        )
        mock_use_cases.get_distance.assert_called_with(
            coordinates_service=mock_coords_service,
            distance_service=mock_distance_service,
            address1='address1',
            address2='address2'
        )
        assert result == 10.0

    @patch('src.controllers.distance_calculator_controller.DistanceGateway')
    @patch('src.controllers.distance_calculator_controller.DistanceCalculatorUseCases')
    def test_should_save_historical_distance(self, mock_use_cases, mock_gateway):
        mock_use_cases.save_historical_distance.return_value = None
        mock_db = Mock()
        DistanceCalculatorController.save_historical_distance(
            db=mock_db,
            address1='address1',
            address2='address2',
            distance=10.0
        )
        mock_use_cases.save_historical_distance.assert_called_with(
            gateway=mock_gateway.return_value,
            address1='address1',
            address2='address2',
            distance=10.0
        )

    @patch('src.controllers.distance_calculator_controller.DistanceGateway')
    def test_should_get_historical_distances(self, mock_gateway):
        expected_distance = {
            'source_address': 'address1',
            'destination_address': 'address2',
            'distance': 10.0
        }
        mock_gateway.return_value.get_historical_distances.return_value = [expected_distance]
        mock_db = Mock()
        result = DistanceCalculatorController.get_historical_distances(db=mock_db)
        assert result == [expected_distance]
