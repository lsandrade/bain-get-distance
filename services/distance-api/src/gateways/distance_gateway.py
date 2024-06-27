import os

from src.interfaces.idistance_gateway import IDistanceGateway

COLLECTION_NAME = os.getenv("HISTORICAL_DISTANCES_COLLECTION_NAME", "historical_distances")


class DistanceGateway(IDistanceGateway):

    def save_historical_distance(self, address1: str, address2: str, distance: float):
        historical_distance = {
            "source_address": address1,
            "destination_address": address2,
            "distance": distance
        }
        return self.repository.save(instance=historical_distance, collection_name=COLLECTION_NAME)

    def get_historical_distances(self) -> list:
        return self.repository.get_all(collection_name=COLLECTION_NAME)
