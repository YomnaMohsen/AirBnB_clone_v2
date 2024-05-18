#!/usr/bin/python3
"""Flask Module that display many pages /"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_bnb():
    """view fn to display string at root page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """view fn to display string at /hbnb url"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """view fn to display text of /c/text url"""
    return "C" + " " + text.replace('_', " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """view fn to display text of /python/text url"""
    return "Python" + " " + text.replace('_', " ")


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """view fn to display number of /python/int num url"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_temp(n):
    """view fn to display number in an HTML page"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
