from typing import Tuple

import requests

from src.interfaces.icoordinates_service import ICoordinatesService


class NominatimCoordinatesService(ICoordinatesService):

    def __init__(self, host: str, endpoint: str, headers: str):
        self.host = host
        self.endpoint = endpoint
        self.headers = headers

    def get_coordinates(self, address: str) -> Tuple[float, float]:
        address_info = self.get_address_info(
            address=address,
            host=self.host,
            coords=self.endpoint,
            headers=self.headers
        )

        if len(address_info) == 0 or 'lat' not in address_info[0] or 'lon' not in address_info[0]:
            raise ValueError(f'Address {address} not found')

        lat, long = float(address_info[0]['lat']), float(address_info[0]['lon'])
        return lat, long

    @staticmethod
    def get_address_info(address: str, host: str, coords: str, headers: str) -> dict:
        url = f'{host}{coords}'
        params = {
            'q': address,
            'format': 'json'
        }
        headers = {
            'User-Agent': headers
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
