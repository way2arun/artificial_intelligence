
#Import the cloud vision apis
from google.cloud import vision
from google.cloud.vision import types

"""Function to initialize the vision api """
def init_vision():
    client = vision.ImageAnnotatorClient()
    return client

""" Function to detect the image and return the image properties and labels"""
def detect_image(image_file, max_results=4):
    if image_file == None:
        return False
    client  = init_vision()
    content = image_file.read()
    image = types.Image(content=content)
    return client.face_detection(image=image, max_results=max_results).face_annotations
