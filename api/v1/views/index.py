#!/usr/bin/python3
"""index.py to connect to API"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

HBNB_TEXT = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app_views.route('/status', strict_slashes=False)
def hbnb_status():
    """Endpoint for checking API status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def hbnb_stats():
    """Endpoint for providing API statistics"""
    return_dict = {}
    for key, value in HBNB_TEXT.items():
        return_dict[key] = storage.count(value)
    return jsonify(return_dict)


if __name__ == "__main__":
    pass