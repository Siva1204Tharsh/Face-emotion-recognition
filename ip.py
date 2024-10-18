import urllib.request  # IP Address baesd working
import cv2
import numpy as np
import imutils


url='http://192.168.8.115:8080/shot.jpg'

while True:
    imgPath=urllib.request.urlopen(url) # url frame wenduram
    imgNp=np.array(bytearray(imgPath.read()), dtype=np.uint8)
    frame=cv2.imdecode(imgNp, -1)

    frame=imutils.resize(frame,width=450)
    cv2.imshow("Frame",frame)
    if ord('q')==cv2.waitKey(1):
        exit(0)
