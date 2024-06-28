import cv2
import os
import Functions as fc

path = 'ImgsProject'
imgs = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    imgs.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

encodeListKnow = fc.findEncodings(imgs)
cap = cv2.VideoCapture(0)
fc.faceRecognition(cap, encodeListKnow, newFace)







