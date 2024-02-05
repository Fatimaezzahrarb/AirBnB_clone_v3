i#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
<<<<<<< HEAD
    """Route that displays states and cities listed in alphabetical order"""
=======
    """display the states and cities listed in alphabetical order"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
<<<<<<< HEAD
    """Route that displays closes storage on teardown"""
=======
    """closes the storage on teardown"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
