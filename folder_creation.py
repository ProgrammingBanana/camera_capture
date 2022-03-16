import os
import numpy as np

"""
This script will create a folder structure in the following way:

    MP_Data/
    |
    |__ ayuda/
    |    |
    |    |__ 0/
    |    |   |
    |    |   |__ 0
    |    |   |
    |    |   |__ 1
    |    |   .
    |    |   .
    |    |   .
    |    |   |__ 59
    |    |
    |    |__ 1/
    |    |   |  
    |    |   |__ 0
    .
    .
    .
    |    |__ 199/
    |    |   |  
    |    |   |__ 0
    .
    .
    .
    |__ clase
    |    |
    |    |__ 0/
    |    |   |
    |    |   |__ 0
    |    |   |
    |    |   |__ 1
    |    |   .
    |    |   .
    |    |   .
    |    |   |__ 59
    |    |
    |    |__ 1/
    |    |   |  
    |    |   |__ 0
    .
    .
        .
"""


# Variable that contains the path for the exported data numpy arrays
DATA_PATH = os.path.join('MP_Data') 

# Actions (signs) we are trying to detect
actions = np.array(['ayuda', 'clase', 'donde', 'gracias', 'hola', 'necesitar', 'no_entender', 'repetir'])

# Thirty videos worth of data
no_sequences = 200

for action in actions:
    for sequence in range(no_sequences):
        try: 
            # Joins DATA_PATH with the action name and sequence number and makes the directory
            # This creates a path like this 'MP_Data/hello/0'
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence))) 
        except:
            # If the folders already exist, we are going to skip to the next sequence
            pass

