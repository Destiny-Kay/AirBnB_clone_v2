#!Q/usr/bin/python3
'''
    Configures a new flask web application
'''
from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def state_list():
    '''Handles the statelist endpoint'''
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def appteardown(exception):
    '''Handles app teardown'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
