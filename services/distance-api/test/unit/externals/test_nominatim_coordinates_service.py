from unittest import TestCase
from unittest.mock import patch

from src.externals.nominatim_coordinates_service import NominatimCoordinatesService


class TestNominatimCoordinatesService(TestCase):
    service = NominatimCoordinatesService(
        host='test-host',
        endpoint='search',
        headers='test-headers'
    )
    coords = {'lat': 0.0, 'lon': 0.0}

    @patch('src.externals.nominatim_coordinates_service.requests')
    def test_should_get_coordinates(self, mock_requests):
        mock_requests.get.return_value.json.return_value = [self.coords]
        result = self.service.get_coordinates('test-address')
        assert result == (0.0, 0.0)
