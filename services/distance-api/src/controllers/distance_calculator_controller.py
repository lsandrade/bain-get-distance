from typing import List

from src.gateways.distance_gateway import DistanceGateway
from src.interfaces.icoordinates_service import ICoordinatesService
from src.interfaces.idb_connection import IDBConnection
from src.interfaces.idistance_calculator_service import IDistanceCalculatorService
from src.use_cases.distance_calculator_use_cases import DistanceCalculatorUseCases


class DistanceCalculatorController:
    @classmethod
    def get_distance(
            cls,
            coordinates_service: ICoordinatesService,
            distance_service: IDistanceCalculatorService,
            address1: str,
            address2: str
    ) -> float:
        return DistanceCalculatorUseCases.get_distance(
            coordinates_service=coordinates_service,
            distance_service=distance_service,
            address1=address1,
            address2=address2
        )

    @classmethod
    def save_historical_distance(cls, db: IDBConnection, address1: str, address2: str, distance: float):
        gateway = DistanceGateway(repository=db)
        DistanceCalculatorUseCases.save_historical_distance(
            gateway=gateway,
            address1=address1,
            address2=address2,
            distance=distance
        )

    @classmethod
    def get_historical_distances(cls, db: IDBConnection) -> List[dict]:
        gateway = DistanceGateway(repository=db)
        return gateway.get_historical_distances()
