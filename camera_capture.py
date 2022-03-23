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
        """ VideoCapture constructor:
            - Initializes utilities and the database
            - Gets signs data
            - User selection for sign to record
            - User input for amount of videos to record
            - Commences video capture utilizing previously stated data 
        """

        self.utils = mp_utilities()
        self.db = DB()
        self.sign_data = self.db.get_signs()
        self.name, self.count, self.path = self.select_sign()
        self.recording_amount = self.get_recording_amount()
        self.starting_sequence = self.get_starting_sequence()
        self.ending_sequence = self.get_ending_sequence()
        self.sequence_length = 30
        self.capture_video()

    def select_sign(self):
        """ Prints on console on the console the signs to record and the amount of videos recorded for each sign
            late giving the user the chance to select which sign they want to work with in the session.

        Returns:
            Tuple: Python tuple containing the selected sign name, video count and file path.
        """

        self.remove_done()

        for index, sign in enumerate(self.sign_data):
            print(f'{index}) Sign:{sign[0]}\n   Count:{sign[1]}')

        selection = int(input("Select sign you want to work with:"))
        return (self.sign_data[selection][0],self.sign_data[selection][1],self.sign_data[selection][2])

    def remove_done(self):
        """ Function that removes sign data for signs that already have 200 recordings
        """
        
        temp = []

        for sign in self.sign_data:
            if sign[1] < 200:
                temp.append(sign)

        self.sign_data = temp

    def get_recording_amount(self):
        """ Allows the user to decide how many videos they want to record in the current session

        Returns:
            Integer: Amount of videos the user wants to record
        """

        return int(input(f"Input how many videos you want to record for {self.name} this session:"))

    def get_starting_sequence(self):
        """ Gets the number ID for the most current video.  Used to specify collection folder
            for the first video of the session. The first video data recorded in the session 
            will be saved in the folder for the specified by this number. This data is saved 
            during the execution of capture_video().

        Returns:
            Integer: Most current video number to start recording at
        """

        return self.count

    def get_ending_sequence(self):
        """ Gets the number ID of the video the recording session will finish at.  The last file saved will
            be stored in a folder identified by self.starting_sequence + self.recording_amount - 1.  This is
            due to the looping logic used in the capture_video() function

        Returns:
            Integer: ID of the video the recording session will finish at
        """

        return self.starting_sequence + self.recording_amount 

    def capture_video(self):
        """ Utilizing the data collected in the constructor method, the video capture is started
            In this function, the camera feed is used to process in mediapipe holistic and then stored
            in a folder for the current video sequence number
        """

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
                        cv2.putText(image, 'Collecting frames for {} Video Number: {}'.format(self.name, sequence), (20, 20), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4, cv2.LINE_AA)
                        # Show the camera feed
                        cv2.imshow('OpenCV Camera Feed', image)
                        
                        cv2.waitKey(2000)
                    else:
                        cv2.putText(image, 'Collecting frames for {} Video Number: {}'.format(self.name, sequence), (20, 20), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4, cv2.LINE_AA)
                        # Show the camera feed
                        cv2.imshow('OpenCV Camera Feed', image)

                    # Extracts keypoints from the results for each frame and saves it in the corresponding file
                    keypoints = self.utils.extract_keypoints(results)
                    # print(keypoints)    
                    npy_path = os.path.join(self.path, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints) 
                    # The previous two lines create an .npy file in the following filepath:
                    # ./ML_Camera_Capture/MP_Data/{sign_name}/{self.count}/{frame_num}.npy

                    
                    # If pressing 'q' Quit the camera
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
            
            self.db.update_sign(self.name, self.recording_amount)
            
            # Close video capture
            cap.release()
            cv2.destroyAllWindows()
            cv2.waitKey(1)

