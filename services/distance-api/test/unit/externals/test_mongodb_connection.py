from unittest import TestCase
from unittest.mock import Mock

from src.externals.mongodb_connection import MongoDBConnection


class TestMongoDBConnection(TestCase):
    instance = {'source_address': 'SP', 'destination_address': 'RJ', 'distance': 300}
    collection_name = "test"
    mock_collection = Mock()

    def setUp(self):
        self.db = {
            self.collection_name: self.mock_collection
        }
        self.db_conn = MongoDBConnection(db=self.db)

    def test_should_save_instance(self):
        self.mock_collection.insert_one.return_value = self.instance
        result = self.db_conn.save(instance=self.instance, collection_name=self.collection_name)
        self.mock_collection.insert_one.assert_called_once_with(self.instance)
        assert self.instance == result

    def test_should_get_all_instances(self):
        self.mock_collection.find.return_value = [self.instance]
        result = self.db_conn.get_all(collection_name=self.collection_name)
        assert self.instance == result[-1]
