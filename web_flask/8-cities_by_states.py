#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """Close the storage engine."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    state_d = storage.all("State").values()
    return render_template('8-cities_by_states.html', state_d=state_d)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
