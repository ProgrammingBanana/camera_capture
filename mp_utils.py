import cv2
import mediapipe as mp
import numpy as np

class mp_utilities():
    def __init__(self):
        # Setting up necessary mediapipe utils and model
        # Mediapipe holistic model
        self.mp_holistic = mp.solutions.holistic
        # Drawing utilities
        self.mp_drawing = mp.solutions.drawing_utils


    def mediapipe_detection(self, image, model):
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

    # Draws the landmarks on each frame of the video
    def draw_styled_landmarks(self, image, results):
        """ Takes in an image and the mediapipe results and 
            draws the landmarks on the image

        Args:
            image (CV2 image): Image captured from video frame
            results (Mediapipe solution output): Landmark data generated by Mediapipe model prediction
        """

        # VERIFY THIS INFORMATION
        # the last arguments is the type of connections to use when drawing
        # It shows what landmark is connected to what other landmark
        self.mp_drawing.draw_landmarks(image, results.face_landmarks, self.mp_holistic.FACE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(230, 216, 173), thickness=1, circle_radius=1),
                                self.mp_drawing.DrawingSpec(color=(255, 121, 80), thickness=1, circle_radius=1))
        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(230, 216, 173), thickness=2, circle_radius=4),
                                self.mp_drawing.DrawingSpec(color=(255, 121, 80), thickness=1, circle_radius=2))
        self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(230, 216, 173), thickness=2, circle_radius=4),
                                self.mp_drawing.DrawingSpec(color=(255, 121, 80), thickness=1, circle_radius=2))
        self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS,
                                self.mp_drawing.DrawingSpec(color=(230, 216, 173), thickness=2, circle_radius=4),
                                self.mp_drawing.DrawingSpec(color=(255, 121, 80), thickness=1, circle_radius=2))

    def extract_keypoints(self, results):
        pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(132) # If null array is array of zeros, else array of coordinates
        left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(63) # If null array is array of zeros, else array of coordinates
        right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(63) # If null array is array of zeros, else array of coordinates
        face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(1404) # If null array is array of zeros, else array of coordinates
        return np.concatenate([pose, face, left_hand, right_hand])