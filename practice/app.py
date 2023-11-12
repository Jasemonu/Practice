#!/usr/bin/env python3

# a script that runs flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "hello world"


if __name__ == "__main__":
	app.run(debug=True)

