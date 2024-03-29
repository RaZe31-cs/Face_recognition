import time

import face_recognition
import pickle
import cv2
import os

from arduino import switch

cascPathface = os.getcwd().replace('\\', '/') + '/haarcascade_frontalface_alt2.xml'

faceCascade = cv2.CascadeClassifier(cascPathface)

data = pickle.loads(open('face_enc', "rb").read())

print("Streaming started")
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,
                                         scaleFactor=1.3,
                                         minNeighbors=9,
                                         minSize=(60, 60),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],
                                                 encoding)
        name = "Неопознанный человек"
        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
        if name != "Неопознанный человек":
            print('Вход разрешен')
            switch('e')
            time.sleep(1)
        else:
            print('Вход воспрещен')
            switch('d')
            time.sleep(1)

        names.append(name)
        # for ((x, y, w, h), name) in zip(faces, names):
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #     cv2.putText(frame, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
        #                 0.75, (0, 255, 0), 2)
    # cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
