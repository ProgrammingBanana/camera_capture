import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp


# Setting up necessary mediapipe utils and model
# Mediapipe holistic model
mp_holistic = mp.solutions.holistic
# Drawing utilities
mp_drawing = mp.solutions.drawing_utils


def mediapipe_detection(image, model):
    """ Receives image and model and applies the necessary
        methods to process the image with mediapipe model received

    Args:
        image (CV2 image): Image captured from video frame
        model (Mediapipe model): Pre-trained Mediapipe Model

    Returns:
        image: original image
        results: model processing results
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # converts color format from BGR to RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Apply mediapipe holistic model
    image.flags.writeable = True                   # Image is now  writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # converts color format from RGB to BGR
    return image, results