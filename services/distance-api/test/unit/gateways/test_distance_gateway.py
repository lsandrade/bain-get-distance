from unittest import TestCase
from unittest.mock import Mock

from src.gateways.distance_gateway import DistanceGateway


class TestDistanceGateway(TestCase):
    def setUp(self):
        self.mock_repo = Mock()
        self.gateway = DistanceGateway(repository=self.mock_repo)
        self.instance = {'source_address': 'SP', 'destination_address': 'RJ', 'distance': 300}

    def test_should_save_historical_distance(self):
        self.mock_repo.save.return_value = self.instance
        result = self.gateway.save_historical_distance(address1='SP', address2='RJ', distance=300)
        self.mock_repo.save.assert_called_once_with(instance=self.instance, collection_name='historical_distances')
        assert self.instance == result

    def test_should_get_historical_distances(self):
        self.mock_repo.get_all.return_value = [self.instance]
        result = self.gateway.get_historical_distances()
        self.mock_repo.get_all.assert_called_once_with(collection_name='historical_distances')
        assert [self.instance] == result
