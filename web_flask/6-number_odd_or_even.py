#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
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
=======
    """display “C ” followed by the value of the text variable"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
<<<<<<< HEAD
    """Route that displays "Python", followed by value of text variable"""
=======
    """display “Python ”, followed by the value of the text variable"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
<<<<<<< HEAD
    """Route that displays "n is a number" only if n is an integer"""
=======
    """display “n is a number” only if n is an integer"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbersandtemplates(n):
<<<<<<< HEAD
    """Route that displays a HTML page only if n is an integer"""
=======
    """display a HTML page only if n is an integer"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
<<<<<<< HEAD
    """Route that displays a HTML page only if n is an integer"""
=======
    """display a HTML page only if n is an integer"""
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)
<<<<<<< HEAD

=======
>>>>>>> e6dac61fd9faa4ae61dfe158c73ccc71b9a7937e

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
