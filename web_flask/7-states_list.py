#!/usr/bin/python3
<<<<<<< HEAD

"""Script that starts a Flask web application"""
=======
"""
starts a Flask web application
"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
<<<<<<< HEAD
    """Route that display a HTML page with states listed in alphabetical order"""
=======
    """display a HTML page with the states listed in alphabetical order"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


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
