#OpenCV module
import cv2
#os module for reading training data directories and paths
import os
#numpy to convert python lists to numpy arrays as it is needed by OpenCV face recognizers
import numpy as np

def detect_face(img):
    # convert the test image to gray scale as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # load OpenCV face detector, I am using LBP which is fast
    # there is also a more accurate but slow: Haar classifier

    face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\lbpcascades\lbpcascade_frontalface.xml')
    #print(face_cascade.load('/home/hazem/opencv-3.2.0/data/lbpcascades/lbpcascade_frontalface.xml')) #to check the directory
    # let's detect multiscale images(some images may be closer to camera than others)
    # result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    # if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None

    # under the assumption that there will be only one face,
    # extract the face area
    (x, y, w, h) = faces[0]

    # return only the face part of the image
    return gray[y:y + w, x:x + h], faces[0]


##cam = cv2.VideoCapture(1)
##cam.set(3, 640)  # set video widht
##cam.set(4, 480)  # set video height
#### Define min window size to be recognized as a face
##minW = 0.1 * cam.get(3)
##minH = 0.1 * cam.get(4)
##
##while True:
##    ret, img = cam.read()
##    img = cv2.flip(img, 1)  # Flip vertically
##    face,position=detect_face(img)
##    
##    if position is not None:
##        cv2.rectangle(img, (position[0], position[1]), (position[0]+position[3], position[1]+position[2]), (0,0,255), 2)
##    if face is not None:
##        cv2.imshow('camera', face)
##    cv2.imshow('camera1', img)
##    k = cv2.waitKey(10) & 0xff  # Presss 'ESC' for exiting video
##    if k == 27:
##        break
##cam.release()
##cv2.destroyAllWindows()
        
