#!/usr/bin/python3
'''Starts a simple flask application'''
from flask import Flask
from flask import render_template
from models import storage
import models
from models import *


app = Flask(__name__)


@app.route('cities_by_states', strict_slashes=False)
def cities_by_stateS():
    '''renders template containing cities'''
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def appteardown(exception):
    '''Handles app teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
