from typing import Any, List

from src.interfaces.idb_connection import IDBConnection


class LocalDBConnection(IDBConnection):

    def __init__(self):
        self.distances = []

    def save(self, instance: dict, collection_name: str = "") -> Any:
        self.distances.append(instance)
        return instance

    def get_all(self, collection_name: str = "") -> List[Any]:
        return self.distances
