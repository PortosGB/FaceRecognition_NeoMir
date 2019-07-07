import face_recognition
import cv2
import numpy as np
import os
from pathlib import Path
import datetime


FACES_FILES_PATH = "."
PATH_TO_RESULT_FILE = "identification.txt"

class Recognition:
    _faces = []
    _face = dict()
    _frame = None
    _face_locations = []
    _face_names = []

    _process_this_frame = True
    def __init__(self):
        # maybe this function calls will be moved out of the __init__ for performance purposes
        self._get_video_capture = cv2.VideoCapture(0)  
        self.load_know_faces()

    '''
        Function called at the start of the program that loads all the pictures in the FACES_FILE_PATH
    '''
    def load_know_faces(self):

        for p in Path(FACES_FILES_PATH).glob('./faces/*'):
            if p.is_file():
                current_face = dict()
                current_face["name"] = p
                current_face["image"] = face_recognition.load_image_file(p)
                current_face["encoding"] = face_recognition.face_encodings(current_face["image"])[0]
                self._faces.append(current_face)
                print(p) #temporary print of the loaded faces


    def process_image(self):

        # Grab a single frame of video
        ret, self._frame = self._get_video_capture.read()

        _process_this_frame = True

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(self._frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self._process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self._face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, self._face_locations)

            self._face_names = []
            if len(face_encodings) == 0:
                self.write_result(3)
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces([d['encoding'] for d in self._faces], face_encoding)
                name = "Unknown"

                '''
                    If a match was found in known_face_encodings, just use the first one.
                '''
                # if True in matches:
                #     first_match_index = matches.index(True)    NOTE : doesnt work, needs to be investigated !
                #     name = known_face_names[first_match_index]

                '''
                        I still need to do tests to compare the two methods and find the best
                '''
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance([d['encoding'] for d in self._faces], face_encoding)
                best_match_index = np.argmin(face_distances)   #do some tests here to prevent false positve !!!!!!!!!!!!
                if matches[best_match_index]:
                    name = [d['name'] for d in self._faces][best_match_index]
                    self.write_result(1, str(name))
                else:
                    self.write_result(2, "Unknown")
                self._face_names.append(str(name))

        process_this_frame = not self._process_this_frame

    '''
        exact protocol TBD
    '''

    def write_result(self, code, name="No face detected"):
        try:
            dt = str(datetime.datetime.now())
            print(name)
            if os.sep in name and "." in name:
                name = name.split(os.sep)[-1].split('.')[0]
            if code == 1:
                os.system( "echo " + str(name)+ "-"+  dt + " > " + PATH_TO_RESULT_FILE)
            '''elif code == 2:
                os.system("echo 'KO: No known subject identified-" + dt +  "' > " > PATH_TO_RESULT_FILE)
            else:
                os.system("echo 'KO: No face detected-" + dt  + "' > " + PATH_TO_RESULT_FILE)
            '''
        except Exception as e:
            print(type(e))
            print(e.args)
            print(e)

    def display_faces(self):

        for (top, right, bottom, left), name in zip(self._face_locations, self._face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            if os.sep in name and "." in name:
                name = name.split(os.sep)[-1].split('.')[0]
            # Draw a box around the face
            cv2.rectangle(self._frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(self._frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(self._frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', self._frame)

        # Hit 'q' on the keyboard to quit!


    def Run(self,  display : bool):

        while True:
            t.process_image()
            if display:
                t.display_faces()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self._get_video_capture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    t = Recognition()
    t.Run(display=True)