#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5000
@app.route('/', strict_slashes=False)
def norm_print():
    print('Hello HBNB')


if __name__ == "__main__":
    app.run(HOST, PORT)
