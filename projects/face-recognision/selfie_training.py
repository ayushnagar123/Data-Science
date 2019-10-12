import numpy as np
from cv2 import cv2

cap = cv2.VideoCapture(0)   # capture the device
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

skip=0
face_data = []
dataset_path =  './data/'
filename = input('Enter the name of the person:- ')
while(True):
    ret,frame = cap.read()  # return bool and captured frame
    # frame1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    if(ret==False):
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame,1.3,5)

    if(len(faces)==0):
        continue

    faces = sorted(faces,key=lambda f:f[2]*f[3])

    # pick largest face
    for face in faces[-1:]:
        (x,y,w,h) = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)    

        # extract (crop out required face): region of interest
        offset = 10
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section,(100,100))
        skip+=1
        if(skip%10==0):
            # store every 10th face
            face_data.append(face_section)
            print(len(face_data))

    cv2.imshow('video frame',frame)
    cv2.imshow('face section',face_section)

    key_pressed = cv2.waitKey(1) & 0xFF
    if(key_pressed==ord('q')):
        break

# face list to numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

#save this data into the file

np.save(dataset_path+filename+'.npy',face_data)
print('data successfully saved '+dataset_path+filename+'.npy')

cap.release()
cv2.destroyAllWindows()

