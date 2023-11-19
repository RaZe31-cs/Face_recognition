import pprint
import sqlite3

from imutils import paths
import face_recognition
import pickle
import cv2
import os

con = sqlite3.Connection('face_enc.sqlite')
cur = con.cursor()
names = cur.execute('SELECT info FROM Users').fetchall()
imagePaths = []
for i in names:
    imagePaths.append((os.listdir(os.getcwd() + '\\Images\\' + i[0]), i[0]))
# в директории Images хранятся папки со всеми изображениями
# imagePaths = list(paths.list_images('Images'))
knownEncodings = []
knownNames = []
# # перебираем все папки с изображениями
for (i, imagePath) in enumerate(imagePaths):
    for j in imagePath[0]:
        # извлекаем имя человека из названия папки
        # name = imagePath.split(os.path.sep)[-1]
        name = imagePath[-1]
        # загружаем изображение и конвертируем его из BGR (OpenCV ordering)
        # в dlib ordering (RGB)
        print(j, name)
        image = cv2.imread(f'Images\\{name}\\' + j)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # используем библиотеку Face_recognition для обнаружения лиц
        boxes = face_recognition.face_locations(rgb, model='hog')
        # вычисляем эмбеддинги для каждого лица
        encodings = face_recognition.face_encodings(rgb, boxes)
        # цикл по кодировкам
        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
# сохраним эмбеддинги вместе с их именами в формате словаря
data = {"encodings": knownEncodings, "names": knownNames}
# для сохранения данных в файл используем метод pickle
f = open("face_enc", "wb")
f.write(pickle.dumps(data))
f.close()
con.close()
