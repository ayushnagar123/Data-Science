from cv2 import cv2

cap = cv2.VideoCapture(0)   # capture the device
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
    ret,frame = cap.read()  # return bool and captured
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    glasses = cv2.imread('glasses.png')
    if(ret==False):
        continue
    
    eyes= eye_cascade.detectMultiScale(gray_frame,1.3,5)

    cv2.imshow('gray frame',gray_frame)

    for eye in eyes:
        (x,y,w,h) = eye
        # combine = cv2.addWeighted(eye,0.4,glasses,0.1,0)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # cv2.imwrite(frame, combine)

    cv2.imshow('video frame',frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if(key_pressed==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()

