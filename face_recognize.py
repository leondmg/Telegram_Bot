import cv2
import numpy as np
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
imagePath = 'C:\Projects\Telegram_bot_2.0/AgADAgADMqkxGz2csEhJF8shU73xrOdMqw4ABGEbGTCc4zwI770FAAEC.jpg'

# iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['Unknow', 'Dmitriy', 'Diana', 'Sergey', 'Z', 'W']

# Initialize and start realtime video capture
#cam = cv2.VideoCapture(0)

img = cv2.imread(imagePath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(15, 15),
)

for (x, y, w, h) in faces:

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

    # Check if confidence is less them 100 ==> "0" is perfect match
    if (confidence < 100):
        id = names[id]
        confidence = "  {0}%".format(round(100 - confidence))
    else:
        id = "unknown"
        confidence = "  {0}%".format(round(100 - confidence))

    #cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
    #cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    print(img, str(id))
cv2.imshow('camera', img)

# Do a bit of cleanup
#print("\n [INFO] Exiting Program and cleanup stuff")
#cam.release()
#cv2.destroyAllWindows()