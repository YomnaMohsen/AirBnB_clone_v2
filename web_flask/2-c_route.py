#!/usr/bin/python3
"""Flask Module that display many pages /"""
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
