from abc import ABC, abstractmethod

from src.interfaces.idb_connection import IDBConnection


class IDistanceGateway(ABC):
    """
    Intarface of the distance gateway.
    """
    def __init__(self, repository: IDBConnection):
        self.repository = repository

    @abstractmethod
    def save_historical_distance(self, address1: str, address2: str, distance: float):
        pass
