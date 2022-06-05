# Machine Learning Sing Language Recognition Video Capture
This project focuses on the main processes necessary to capture and store video data for a machine learning project that uses Mediapipe Holistic data captured from video webcam.

## Files:
* camera_capture.py: has the camera logic
* database.py: contains the methods necessary to store and update information about the recordings
* folder_creation.py: Contains the logic for creating the folders where the data will be stored.
* mp_utils.py: Contains the logic for managing Mediapipe Holistic and the data it produces
* database_setup.py: Contains the script for inserting the initial sign data into the database

### Note:
Although a database is being used to store data about the signs, it is not necessary to do so.  Using the database simplifies the recording process as it allows the user to record the videos for a specific sign through multiple sessions, instead of in one sitting.  It does so by storing information about the sign file locations, and the amount of videos recorded.  By remembering how many videos have been recorded through the different recording sessions, it allows the user to continue from where they left off.

## Installation and Set up
Having an updated version of Python installed on the computer is necessary for the project to work
1. Run the command ```pip install pipenv``` in your command line terminal
2. Download code from the repository
3. Go to the project location in command line and run the command ```pipenv shell``` to start the virtual environment
4. In command line and run the command ```pipenv install --ignore-pipfile``` to install dependencies named in the pipfile.lock document
5. Run the command ```python folder_creation.py``` before any other script to create the data collection folders in the project directory.
6. Once you do so, you can run the command ```python database_setup.py``` to create the database and add the entries for each individual sign to the database.  Each entry will start with the sign name, 0 for the count, and the filepaths defined in the previous step.

## Running the application
You are now ready to run the video capture application.  To do so, run the command ```python camera_capture.py```.  Doing so will prompt you to select the sign you want to record, and the amount of videos you want to record. After entering that information, the app will start recording data for the sign selected.