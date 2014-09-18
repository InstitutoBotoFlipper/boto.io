# -*- coding: utf-8 -*-

# python 3 import support
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "hello Wolrd!! <strong>I\'m learning Flask</strong>", 200

app.run()
