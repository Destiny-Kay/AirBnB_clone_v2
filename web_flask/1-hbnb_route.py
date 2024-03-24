#!/usr/bin/python3
'''A simple flask server'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    '''serves requests on the / route'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Serves requests on the /hbnb route'''
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
