from flask import Flask
from flask_cors import CORS

flask_app = Flask(__name__)

@flask_app.route("/")
def hello_world():
    return "<p>Helo, world!</p>"