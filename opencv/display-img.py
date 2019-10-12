from cv2 import cv2
import matplotlib.pyplot as plt

img=cv2.imread('download.jpeg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.imread('download.jpeg',cv2.IMREAD_GRAYSCALE)
# plt.ion()
cv2.imshow('image BGR',img)
cv2.imshow('image RGB',img1)
# plt.show()
cv2.imshow('gray',gray)
# plt.show()
cv2.waitKey(5000)
cv2.destroyAllWindows()