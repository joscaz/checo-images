# from flask import jsonify, send_file
from flask import current_app, redirect
import random
import boto3
import logging

logging.basicConfig(level=logging.DEBUG)  # Set the desired logging level

def get_s3_client():
    return boto3.client('s3',
                    aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])

def get_random_image():
    s3 = get_s3_client()
    BUCKET_NAME = "checoperezimages"
    IMAGE_PREFIX = current_app.config['IMAGE_PREFIX']

    if not isinstance(IMAGE_PREFIX, str):
        # Si no es una cadena, intenta convertirla a una cadena
        IMAGE_PREFIX = str(IMAGE_PREFIX)

    objects = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=IMAGE_PREFIX)
    image_keys = [obj['Key'] for obj in objects.get('Contents', [])]
    random_image_key = random.choice(image_keys)
    image_url = f"https://{BUCKET_NAME}.s3.us-east-2.amazonaws.com/{random_image_key}"
    return redirect(image_url)