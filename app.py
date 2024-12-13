from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from datetime import datetime
import os
import uuid

from requests import RequestException

app = Flask(__name__, static_folder='static')

@app.route("/hello")
def hello() -> str:
    return "hello there"

@app.route("/double/<x>")
def double(x: str) -> str:
    return str(2. * float(x))


if __name__ == '__main__':
   app.run()
