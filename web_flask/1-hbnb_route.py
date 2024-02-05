i#!/usr/bin/python3
"""
<<<<<<< HEAD
A Flask web application listen on 0.0.0.0.
=======
starts a Flask web application
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
<<<<<<< HEAD
    """Route that displays return Hello HBNB!"""
=======
    """returns Hello HBNB!"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """Route that displays return HBNB"""
=======
    """returns HBNB"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
