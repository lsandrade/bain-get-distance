from unittest import TestCase

from src.externals.localdb_connection import LocalDBConnection


class TestLocalDBConnection(TestCase):
    db_con = LocalDBConnection()
    instance = {'source_address': 'SP', 'destination_address': 'RJ', 'distance': 300}

    def test_should_save_instance(self):
        result = self.db_con.save(self.instance)
        assert self.instance == result

    def test_should_get_all_instances(self):
        result = self.db_con.get_all()
        len_before = len(result)
        self.db_con.save(self.instance)
        result = self.db_con.get_all()
        len_after = len(result)
        assert len_before + 1 == len_after
        assert self.instance == result[-1]
