# pyenv shell 3.9.4
# python -m flask --app exercise1.py run
from flask import Flask

app = Flask(__name__)

#server hello, world
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
