# Machine Learning Sing Language Recognition Video Capture
This project focuses on the main processes necessary to capture and store video data for a machine learning project that uses Mediapipe Holistic data captured from video webcam.

## Files:
* camera_capture.py: has the camera logic
* database.py: contains the methods necessary to store and update information about the recordings
* folder_creation.py: Contains the logic for creating the folders where the data will be stored.
* mp_utils.py: Contains the logic for managing Mediapipe Holistic and the data it produces

### Note:
Although a database is being used to store data about the signs, it is not necessary to do so.  Using the database simplifies the recording process as it allows the user to record the videos for a specific sign through multiple sessions, instead of in one sitting.  It does so by storing information about the sign file locations, and the amount of videos recorded.  By remembering how many videos have been recorded through the different recording sessions, it allows the user to continue from where they left off.