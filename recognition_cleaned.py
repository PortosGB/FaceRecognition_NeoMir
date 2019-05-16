import face_recognition
import cv2
import numpy as np
import os


FACES_FILES_PATH = "."

class Recognition:
    _face_locations = []
    _face_encodings = []
    _face_names = []
    _process_this_frame = True
    def __init__(self):
        self._get_video_capture = cv2.VideoCapture(0)

    '''
        For release : create array with all the images in knowns faces
    '''
    def load_know_faces(self, path):
        self.obama_image = face_recognition.load_image_file("obama.jpg")
        self.obama_face_encoding = face_recognition.face_encodings(self.obama_image)[0]

        # Load a second sample picture and learn how to recognize it.
        self.biden_image = face_recognition.load_image_file("biden.jpg")
        self.biden_face_encoding = face_recognition.face_encodings(self.biden_image)[0]

        self.q_g__image = face_recognition.load_image_file("Quentin_Glasses.jpg")
        self.q_g_face_encoding = face_recognition.face_encodings(self.q_g__image)[0]

        self.q_image = face_recognition.load_image_file("Quentin.jpg")
        self.q_face_encoding = face_recognition.face_encodings(self.q_image)[0]

        self.marwin_image = face_recognition.load_image_file("Marwin.jpg")
        self.marwin_face_encoding = face_recognition.face_encodings(self.marwin_image)[0]

        self.jose_image = face_recognition.load_image_file("jose.jpg")
        self.jose_face_encoding = face_recognition.face_encodings(self.jose_image)[0]

        self.known_face_encodings = [
            self.obama_face_encoding,
            self.biden_face_encoding,
            self.q_g_face_encoding,
            self.q_face_encoding,
            self.marwin_face_encoding,
            self.jose_face_encoding
        ]
        known_face_names = [
            "Barack Obama",
            "Joe Biden",
            "Quentin (Glasses On)",
            "Quentin",
            "Marwin",
            "Jose Obusan"
        ]
