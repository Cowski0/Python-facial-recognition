import face_recognition
import cv2
import numpy as np
from os import system, name
print('type "again" in box to continue (bug)')
def clear():
    if name == 'nt':
        _=system('cls')

def photomain():
    unknown = 'Known.jpg'
    unknown_in = input('\nInput Image Or, Would you like a "Known Image" (Y/N): ')
    if unknown_in == 'Y':
        unknown = 'Known.jpg'
    elif unknown_in == "N":
        unknown = 'Unknown.jpg'
    else:
        unknown = unknown_in
    known_image1 = face_recognition.load_image_file("Known.jpg")
    known_image2 = face_recognition.load_image_file("Known2.jpg")
    unknown_image = face_recognition.load_image_file(unknown)
    qwe = ('Known,\nKnown2')
    try:
        known_face1 = face_recognition.face_encodings(known_image1)[0]
        known_face2 = face_recognition.face_encodings(known_image2)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    known_faces = [
        known_face1,
        known_face2
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    if results[0] == True:
        print('Known person! nothing will happen.')
    else:
        print('Detected face is not a known person!')
def videomain():
    video_capture = cv2.VideoCapture(0)
    Known_image = face_recognition.load_image_file("Known.jpg")
    Known_face_encoding = face_recognition.face_encodings(Known_image)[0]
    known_face_encodings = [
        Known_face_encoding
    ]
    known_face_names = [
        "Known"
    ]
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                print('face detected')
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown!"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)
        process_this_frame = not process_this_frame
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        cv2.imshow('Live Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('0'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
while True:
    ewq = input('\n\nPress <CTRL+C> To Exit... Or Type "again" To Restart: ')
    if ewq == 'again':
        clear()
        qwer = input('Would you like to use webcam or use an image?\n1: Webcam\n2: Photo\nEnter Here: ')
        if qwer == '1':
            videomain()
        elif qwer == '2':
            photomain()
