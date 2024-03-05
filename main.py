import cv2
from simple_facerec import SimpleFacerec
import keyboard

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (35, 170, 242), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (35, 170, 242), 4)

    cv2.imshow("Face Recognition", frame)
    if keyboard.is_pressed('q'):
        break
    key = cv2.waitKey(1)
    if key == 'q':
        break
cap.release()
cv2.destroyAllWindows()

import cv2
from simple_facerec import SimpleFacerec
