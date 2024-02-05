#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
<<<<<<< HEAD
    """return Hello HBNB!"""
=======
    """returns Hello HBNB!"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """return HBNB"""
=======
    """returns HBNB"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
<<<<<<< HEAD
    """display "C" followed by value of text variable"""
=======
    """display “C ” followed by the value of the text variable"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
<<<<<<< HEAD
    """displays "Python", followed by value of text variable"""
=======
    """display “Python ”, followed by the value of the text variable"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
<<<<<<< HEAD
    """displays "n is a number" only if n is an integer"""
    return "{:d} is a number".format(n)

=======
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
