#!/usr/bin/python3
"""app.py to connect to API"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')
CORS(app, resources={"/*": {"origins": os.getenv('CORS_ALLOWED_ORIGIN', '0.0.0.0')}})


@app.teardown_appcontext
def teardown_appcontext(exception):
    """teardown_appcontext: Closes the database connection after each request"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """page_not_found: Handles 404 errors"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(
        host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
        port=int(os.getenv('HBNB_API_PORT', '5000'))
    )
