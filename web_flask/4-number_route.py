#!/usr/bin/python3
<<<<<<< HEAD
"""
Fourth view function
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
=======
    """display HBNB"""
>>>>>>> 1db505bb0e3d96f42605b64550b9f804ed57535d
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
<<<<<<< HEAD
    """show “C ” followed by value of text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """show “Python ”, followed by the value of text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """show “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')i
=======
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """display “Python ”, followed by the value of the text"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 1db505bb0e3d96f42605b64550b9f804ed57535d
