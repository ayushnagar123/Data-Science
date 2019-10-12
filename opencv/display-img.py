from cv2 import cv2
import matplotlib.pyplot as plt

img=cv2.imread('download.jpeg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# plt.ion()
cv2.imshow('image',img)
# plt.show()
# cv2.imshow('gray',gray)
# plt.show()
cv2.waitKey(1000)
cv2.destroyAllWindows()