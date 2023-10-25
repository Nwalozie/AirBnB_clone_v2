#!/usr/bin/python3
"""Script that displays and the render the sstates"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    states = sorted(storage.all('State').values(), key=lambda i: i.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_strorage(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
