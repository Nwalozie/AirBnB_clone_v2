#!/usr/bin/python3
"""
script that starts a Flask web application
Including another route to return a diffeerent page
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Funtion return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Function return HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Function that accepts Argument"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python",  strict_slashes=False)
def python_is_fun(text="is cool"):
    """Function that accepts Argument"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_display(n):
    """Funtion that displays the number entered"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Function that render template with the number entered"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
