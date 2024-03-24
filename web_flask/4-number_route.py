#!/usr/bin/python3
'''A simple flask server'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    '''serves requests on the / route'''
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Serves requests on the /hbnb route'''
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    '''Serves all requests from the /c/ route'''
    new_text = text.replace("_", " ")
    return f"C {escape(new_text)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text=None):
    '''Serves all routes in the python path'''
    new_text = "is cool"
    if text:
        new_text = text.replace("_", " ")
    return f"Python {escape(new_text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    '''Serves requests in the /number/<> path'''
    return (f"{n} is a number")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
