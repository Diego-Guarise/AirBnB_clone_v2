#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """print hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """print hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def Cis(text):
    """print C is string"""
    return "C %s" % escape(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Pythonis(text="is cool"):
    """print Python is string"""
    return "Python %s" % escape(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """print Python is string"""
    return "%s is a number" % escape(int(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def numberinhtml(n):
    """the number in html"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numberinhtmlevenold(n):
    """the number in html"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
