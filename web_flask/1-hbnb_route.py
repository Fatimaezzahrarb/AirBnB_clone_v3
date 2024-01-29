#!/usr/bin/python3
<<<<<<< HEAD
"""
Begin a Flask web application
"""

from flask import Flask
=======
"""starts a Flask web application."""


from flask import Flask

>>>>>>> 1db505bb0e3d96f42605b64550b9f804ed57535d
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def index():
    """return Hello HBNB!"""
=======
def hello():
    """display “Hello HBNB!”"""
>>>>>>> 1db505bb0e3d96f42605b64550b9f804ed57535d
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """return HBNB"""
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
    """display HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 1db505bb0e3d96f42605b64550b9f804ed57535d
