#!/usr/bin/python3
<<<<<<< HEAD
"""Flask web application"""

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
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000') 
=======
def hello():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 1db505bb0e3d96f42605b64550b9f804ed57535d
