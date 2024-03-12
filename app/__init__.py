from flask import Flask
from flask_cors import CORS
import logging

flask_app = Flask(__name__)
CORS(flask_app)

flask_app.config.from_object('config')

logging.getLogger().setLevel(logging.INFO)
flask_app.logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
flask_app.logger.addHandler(handler)

@flask_app.route("/")
def hello_world():
    return "<p>Helo, world!</p>"

import app.routes