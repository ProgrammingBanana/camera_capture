import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from mp_utils import mp_utilities


utils = mp_utilities()


# Connects to the webcam (the number can vary depending on machine)
cap = cv2.VideoCapture(0)

# TESTING THE FUNCTIONS WORKS 
# Set mediapipe model
with utils.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        
        # Read feed
        ret, frame = cap.read()
        
        # Make detections
        image, results = utils.mediapipe_detection(frame, holistic)
        
        utils.draw_styled_landmarks(image, results)
        
        # Show the camera feed
        cv2.imshow('OpenCV Camera Feed', image)
        
        # If pressing 'q' Quit the camera
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    
    # Close video capture
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)