#!/usr/bin/python3
"""
starts a Flask web application
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


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
<<<<<<< HEAD
    """Route that displays "C" followed by value of text variable"""
    return 'C ' + text.replace('_', ' ')

=======
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
