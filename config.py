# Statement for enabling the development environment

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

BUCKET_NAME = os.environ.get('BUCKET_NAME')
IMAGE_PREFIX = os.environ.get('IMAGE_PREFIX')