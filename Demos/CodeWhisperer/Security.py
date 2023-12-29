import logging
import urllib.parse

from flask import Flask, Response, redirect, request
from werkzeug.datastructures import Headers

logging.basicConfig(level=logging.CRITICAL)
app = Flask(__name__)


@app.route("/example")
def log():
    data = request.args["data"]
    # remove urllib.parse.quote
    app.logger.critical("%s", urllib.parse.quote(data))  # Noncompliant


import validators


@app.route("/redirecting")
def redirecting():
    url = request.args["url"]
    # remove validators
    if validators.url(url):  # import validators
        return redirect(url)  # Noncompliant
    else:
        raise RuntimeError("URL being redirected to is invalid.")  # import exceptions
