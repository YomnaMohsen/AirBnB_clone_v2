#!/usr/bin/python3
"""Flask Module that display many pages /"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_states():
    """view fn to States in an HTML page"""
    all_states = storage.all(State).values()
    state_list = sorted(all_states, key=lambda x: x.name)
    for s in state_list:
        s.cities.sort(key=lambda x: x.name)      
    return render_template('8-cities_by_states.html', sort_list=state_list)


@app.teardown_appcontext
def teardown_db(exception):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
