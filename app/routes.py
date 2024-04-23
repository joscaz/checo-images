from app import flask_app
from app.s3_manager import get_random_image

@flask_app.route("/checo", methods=['GET'])
def get_random_checo_image():
    return get_random_image()