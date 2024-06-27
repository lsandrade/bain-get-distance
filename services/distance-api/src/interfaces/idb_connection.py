from abc import ABC, abstractmethod
from typing import Any, List


class IDBConnection(ABC):  # pragma: no cover
    @abstractmethod
    def save(self, instance: dict, collection_name: str = "") -> Any:
        pass

    @abstractmethod
    def get_all(self, collection_name: str = "") -> List[Any]:
        pass
