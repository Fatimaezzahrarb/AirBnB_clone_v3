#!/usr/bin/python3
"""starts a Flask web application."""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays an HTML page with the number n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd_even=odd_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
