from typing import List, Any

from src.interfaces.idb_connection import IDBConnection


class MongoDBConnection(IDBConnection):

    def __init__(self, db: object):
        self._db = db

    def save(self, instance: dict, collection_name: str = "") -> Any:
        collection = self._db[collection_name]
        return collection.insert_one(instance)

    def get_all(self, collection_name: str = "") -> List[Any]:
        collection = self._db[collection_name]
        return list(collection.find({}, {"_id": 0}))
