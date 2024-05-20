#!/usr/bin/python3
"""Flask Module that display many pages /"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    """view fn to States in an HTML page"""
    all_states = storage.all(State).values()
    sorted_list = sorted(all_states, key=lambda x: x.name)
    return render_template('7-states_list.html', sort_list=sorted_list)


@app.teardown_appcontext
def teardown_db(exception):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
