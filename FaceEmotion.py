from facial_emotion_recognition import EmotionRecognition
import cv2

er=EmotionRecognition(device='cpu') #device='cpu' or device='gpu'

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    frame=er.recognise_emotion(frame,return_type='BGR')
    cv2.imshow('frame',frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()