import cv2
import numpy as np
import face_recognition

from datetime import datetime

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendence(name):
    with open('DataBase.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtStr = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtStr}')


def newUser(cap, encodeListKnow, newFace, encodeCurFrame):
    while newFace:
        Name = input('Name: ')
        now = datetime.now()
        dtStr = now.strftime('%H:%M:%S')

        i = 0
        while i <= len(EncList):
            encodeNewFace = False
            if encodeNewFace:
                encodeNewFace = face_recognition.compare_faces(EncList[i], encodeCurFrame)
            i += 1

        if not encodeNewFace:
            now = datetime.now()
            dtStr = now.strftime('%H:%M:%S')
            n.writelines(f'\n{name},{dtStr},{encodeCurFrame}')

            newFace = False
        else:
            newFace = False
            faceRecognition(cap, encodeListKnow, newFace)


def faceRecognition(cap, encodeListKnow, newFace):
    while True:
        succes, img = cap.read()
        imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnow, encodeFace)

            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 =  y1*4,x2*4,y2*4,x1*4

                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle((img,(x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED))
                cv2.putText(img, name, (x1 +6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

                markAttendence(name)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)
