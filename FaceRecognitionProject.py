import cv2
import os
import Functions as fc

path = 'Imgs'
imgs = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imgs.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

encodeListKnown = fc.findEncodings(imgs)
cap = cv2.VideoCapture(0)

fc.faceRecognition(cap, encodeListKnown, classNames)







