import numpy as np
import cv2

cap = cv2.VideoCapture(r"path")
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (320, 480))

while(True):
    ret, frame = cap.read() 
    cropped = frame[320:640, 0:360]
    out.write(cropped) 
    cv2.imshow('Original', frame)
    cv2.imshow('frame', cropped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
out.release() 
cv2.destroyAllWindows()