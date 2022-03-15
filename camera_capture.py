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
        self.name, self.count, self.path = self.select_sign()
        self.recording_amount = self.get_recording_amount()
        self.starting_sequence = self.get_starting_sequence()
        self.ending_sequence = self.get_ending_sequence()
        self.sequence_length = 60
        self.capture_video()

    def select_sign(self):
        for index, sign in enumerate(self.sign_data):
            print(f'{index}) Sign:{sign[0]}\n   Count:{sign[1]}')
        selection = int(input("Select sign you want to work with:"))
        return (self.sign_data[selection][0],self.sign_data[selection][1],self.sign_data[selection][2])

    def get_recording_amount(self):
        return int(input("Input how many videos you want to record this session:"))

    def get_starting_sequence(self):
        return self.count

    def get_ending_sequence(self):
        return self.starting_sequence + self.recording_amount 

    def capture_video(self):
        # Connects to the webcam (the number can vary depending on machine)
        cap = cv2.VideoCapture(0)

        # TESTING THE FUNCTIONS WORKS 
        # Set mediapipe model
        with self.utils.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            print('waiting before recording new action')
            cv2.waitKey(5000)

            for sequence in range(self.starting_sequence, self.ending_sequence):
                for frame_num in range(self.sequence_length):
            
                    # Read feed
                    ret, frame = cap.read()
                    
                    # Make detections
                    image, results = self.utils.mediapipe_detection(frame, holistic)
                    
                    self.utils.draw_styled_landmarks(image, results)
                    
                        # wait logic (gives us a break to reposition before every clip)
                    if frame_num == 0:
                        cv2.putText(image, 'STARTING COLLECTION', (120, 200), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv2.LINE_AA)
                        cv2.putText(image, 'Collecting frames for {} Video Number: {}'.format(self.name, sequence), (15, 12), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4, cv2.LINE_AA)
                        # Show the camera feed
                        cv2.imshow('OpenCV Camera Feed', image)
                        
                        cv2.waitKey(2000)
                    else:
                        cv2.putText(image, 'Collecting frames for {} Video Number: {}'.format(self.name, sequence), (15, 12), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4, cv2.LINE_AA)
                        # Show the camera feed
                        cv2.imshow('OpenCV Camera Feed', image)
                    
                    # If pressing 'q' Quit the camera
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
            
            # Close video capture
            cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)

