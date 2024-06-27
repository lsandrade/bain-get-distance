from flask import Flask, request

from src.controllers.distance_calculator_controller import DistanceCalculatorController
from src.interfaces.icoordinates_service import ICoordinatesService
from src.interfaces.idb_connection import IDBConnection
from src.interfaces.idistance_calculator_service import IDistanceCalculatorService


class DistanceApp:

    def __init__(
            self,
            db: IDBConnection,
            coordinates_service: ICoordinatesService,
            distance_calculator_service: IDistanceCalculatorService
    ):
        self._db = db
        self._coordinates_service = coordinates_service
        self._distance_calculator_service = distance_calculator_service

    def start(self, app: Flask):
        app = self._get_routes(app=app)
        return app

    def _get_routes(self, app: Flask):
        @app.route("/distance", methods=['GET'])
        def get_distance():
            req = request.get_json()

            if 'source_address' not in req or 'destination_address' not in req:
                return {"error": "Missing source_address or destination_address"}, 400

            address1 = req.get('source_address')
            address2 = req.get('destination_address')

            if not address1 or not address2:
                return {"error": "Missing source_address or destination_address"}, 400

            try:
                distance = DistanceCalculatorController.get_distance(
                    coordinates_service=self._coordinates_service,
                    distance_service=self._distance_calculator_service,
                    address1=address1,
                    address2=address2
                )
                DistanceCalculatorController.save_historical_distance(
                    db=self._db,
                    address1=address1,
                    address2=address2,
                    distance=distance
                )
                return {"distance": distance}
            except Exception as e:
                return {"error": str(e)}, 500

        @app.route("/distance/historical", methods=['GET'])
        def get_historical_distances():
            try:
                return DistanceCalculatorController.get_historical_distances(db=self._db)
            except Exception as e:
                return {"error": str(e)}, 500

        return app
