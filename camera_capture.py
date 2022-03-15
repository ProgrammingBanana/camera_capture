import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from mp_utils import mp_utilities
from database import Database as DB

class VideoCapture():

    def __init__(self):
        self.utils = mp_utilities()
        db = DB()
        self.sign_data = db.get_signs()
        self.selected_sign = self.select_sign()
        self.path = self.sign_data[self.selected_sign][2]
        self.recording_amount = self.get_recording_amount()
        self.capture_video()

    def select_sign(self):
        for index, sign in enumerate(self.sign_data):
            print(f'{index}) Sign:{sign[0]}\n   Count:{sign[1]}')
        return input("Select sign you want to work with:")

    def get_recording_amount(self):
        return input("Input how many videos you want to record this session:")

    def capture_video(self):
        # Connects to the webcam (the number can vary depending on machine)
        cap = cv2.VideoCapture(0)

        # TESTING THE FUNCTIONS WORKS 
        # Set mediapipe model
        with self.utils.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while cap.isOpened():
                
                # Read feed
                ret, frame = cap.read()
                
                # Make detections
                image, results = self.utils.mediapipe_detection(frame, holistic)
                
                self.utils.draw_styled_landmarks(image, results)
                
                # Show the camera feed
                cv2.imshow('OpenCV Camera Feed', image)
                
                # If pressing 'q' Quit the camera
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            
            # Close video capture
            cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)

# test = VideoCapture()

# test.capture_video()

def __main__():
    pass