import os

from flask import Flask
from pymongo import MongoClient

from src.api.distance_app import DistanceApp
from src.externals.haversine_distance_calculator_service import HaversineDistanceCalculatorService
from src.externals.mongodb_connection import MongoDBConnection
from src.externals.nominatim_coordinates_service import NominatimCoordinatesService

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
DB_NAME = os.environ.get('DB_NAME', 'distance')

COORDS_HOST = os.environ.get('COORDS_HOST', 'https://nominatim.openstreetmap.org/')
COORDS_ENDPOINT = os.environ.get('COORDS_ENDPOINT', 'search')
HEADERS = os.environ.get('COORDS_HEADERS', 'Mozilla/5.0 (compatible; BainDistanceApi/1.0)')


def get_flask_app():
    # start flask app
    app = Flask(__name__)

    # start db
    client = MongoClient(MONGO_URI)
    db = client.get_database(DB_NAME)
    db_connection = MongoDBConnection(db=db)

    # start coords service
    coords_service = NominatimCoordinatesService(
        host=COORDS_HOST,
        endpoint=COORDS_ENDPOINT,
        headers=HEADERS
    )

    # start distance calculator service
    distance_calc_service = HaversineDistanceCalculatorService()

    # start app
    distance_app = DistanceApp(
        db=db_connection,
        coordinates_service=coords_service,
        distance_calculator_service=distance_calc_service
    )

    app = distance_app.start(app=app)
    return app


app = get_flask_app()

if __name__ == '__main__':  # pragma: no cover
    port = int(os.environ.get('PORT', 5001))
    host = os.environ.get('HOST', '0.0.0.0')
    app.run(debug=True, host=host, port=port)
