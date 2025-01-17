#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
<<<<<<< HEAD
    """
    Route that displays "HBNB".
    """
=======
    """returns HBNB"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
<<<<<<< HEAD
def c_text(text):
    """
    Route that displays "C "
    """
    return 'C {}'.format(text.replace('_', ' '))
=======
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
<<<<<<< HEAD
def python_text(text='is cool'):
    """
    Route that displays "Python "
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def text_if_int(n):
    """
    Route that displays only if int given.
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_if_int(n):
    """
    Route that displays a HTML page only if int given
    """
=======
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
    """display a HTML page only if n is an integer"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
