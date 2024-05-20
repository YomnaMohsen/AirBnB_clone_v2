#!/usr/bin/python3
"""Flask Module that display many pages /"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def display_cities_states_ament():
    """view fn to list cities by States and amenities in an HTML page"""
    all_states = storage.all(State).values()
    state_list = sorted(all_states, key=lambda x: x.name)
    for s in state_list:
        s.cities.sort(key=lambda x: x.name)
    all_ament = storage.all(Amenity).values()
    ament_list = sorted(all_ament, key=lambda x: x.name)    
    return render_template('10-hbnb_filters.html', sort_list=state_list, A_list=ament_list)


@app.teardown_appcontext
def teardown_db(exception):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
