from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

#OpenCV module
import cv2
#os module for reading training data directories and paths
import os
#numpy to convert python lists to numpy arrays as it is needed by OpenCV face recognizers
import numpy as np
from trainingFaces import prepare_training_data


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)


serviceUsername = "6fd37c9b-4719-4fe6-9494-509a4f4e2130-bluemix"
servicePassword = "349ecad031b57c58c0bd4b3991abd44b41d78a49632fb6456a038dcfd83951fc"
serviceURL = "https://6fd37c9b-4719-4fe6-9494-509a4f4e2130-bluemix:349ecad031b57c58c0bd4b3991abd44b41d78a49632fb6456a038dcfd83951fc@6fd37c9b-4719-4fe6-9494-509a4f4e2130-bluemix.cloudant.com"


client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
print ("Successfully connected to Cloudant")


databaseName = "class"
##myDatabaseDemo = client.create_database(databaseName)
myDatabaseDemo = client[databaseName]
if myDatabaseDemo.exists():
    print ("'{0}' successfully created.\n".format(databaseName))


print("Collecting data")
faces,labels=prepare_training_data("C:/Users/Unknown/Desktop/faceoff")
print(labels)

print("Total faces: ", len(faces))
print("Total labels: ", len(labels))

banyAdmeen = ["Unknown","Hazem", "Azazi","Omar","Adel"]
flags=[0,0,0,0,0]
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))

cam = cv2.VideoCapture(1)
cam.set(3, 640)  # set video widht
cam.set(4, 480)  # set video height
# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)

while True:
    ret, img = cam.read()
    img = cv2.flip(img, 1)  # Flip vertically
    cv2.imshow("camera",img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    x=np.sum(gray)
##    print(x)
##    if x<15*1000000:
##        draw_text(img, "brightness is low",0,30)
##        cv2.imshow("camera",img)
##        k = cv2.waitKey(10) & 0xff  # Presss 'ESC' for exiting video
##        if k == 27:
##            break
##        continue
    face_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\lbpcascades\lbpcascade_frontalface.xml')
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(int(minW), int(minH)))
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("camera",img)
        idh, confidence = face_recognizer.predict(gray[y:y + h, x:x + w])
        print ('the id: {0} the confidence {1}'.format(idh,confidence))
        print (banyAdmeen[idh])
        persentage = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(persentage), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)
        if(confidence<40):
            draw_text(img, "{}".format(banyAdmeen[idh]),0,30)
            if flags[idh]==0:
                flags[idh]=1
                
                my_document = myDatabaseDemo[str(idh)]
                my_document['attendance']=my_document['attendance']+1
                print ("saved")
                my_document.save()
                
        cv2.imshow("camera",img)
    k = cv2.waitKey(100) & 0xff  # Presss 'ESC' for exiting video
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
