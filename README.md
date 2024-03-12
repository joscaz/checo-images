# API that returns a random image of Checo Perez

This is a small personal project I'm doing just for fun. I'm a big fan of Checo Perez (F1 driver) and basically when you call '/checo/' endpoint, it returns a random image (meme) related to Checo Pérez.

I created a S3 AWS bucket to store the images, and then I used AWS SDK for python (Boto3) to make the connection to the bucket and retrieve the images.

Created by me: José Carlos Zertuche
