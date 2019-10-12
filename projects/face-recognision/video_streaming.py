from cv2 import cv2

cap = cv2.VideoCapture(0)   # capture the device

while(True):
    ret,frame = cap.read()  # return bool and captured frame
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if(ret==False):
        continue
    
    cv2.imshow('video frame',frame)
    cv2.imshow('gray frame',gray_frame)

    key_pressed = cv2.waitKey(1) & 0xFF # will wait for 1 ms for next itteration
    if(key_pressed==ord('q')):  # ord tells ascii value of a character
        break

cap.release()
cv2.destroyAllWindows()

