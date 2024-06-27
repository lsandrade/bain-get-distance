from src.interfaces.icoordinates_service import ICoordinatesService
from src.interfaces.idistance_calculator_service import IDistanceCalculatorService
from src.interfaces.idistance_gateway import IDistanceGateway


class DistanceCalculatorUseCases:
    @classmethod
    def get_distance(
            cls,
            coordinates_service: ICoordinatesService,
            distance_service: IDistanceCalculatorService,
            address1: str,
            address2: str
    ) -> float:
        coordinates1 = coordinates_service.get_coordinates(address1)
        coordinates2 = coordinates_service.get_coordinates(address2)
        return distance_service.calculate_distance(coordinates1, coordinates2)

    @classmethod
    def save_historical_distance(cls, gateway: IDistanceGateway, address1: str, address2: str, distance: float):
        return gateway.save_historical_distance(address1=address1, address2=address2, distance=distance)
