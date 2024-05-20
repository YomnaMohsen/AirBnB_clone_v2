#!/usr/bin/python3
"""Flask Module that display many pages /"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def display_states_id(id=None):
    """view fn to list cities by States in an HTML page"""
    all_states = storage.all(State).values()
    state_list = sorted(all_states, key=lambda x: x.name)
    if id is None:
        return render_template('9-states.html', sr_list=state_list, n_id=True)
    else:
        for st in state_list:
            if (st.id == id):
                st.cities.sort(key=lambda x: x.name)
                return render_template('9-states.html', st_city=st)
        return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
