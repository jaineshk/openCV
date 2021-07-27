# learn OpenCV
import cv2
import random
img = cv2.imread('image/mission.jpg', -1)

tag = img[100:200, 25:125]
img[50:150, 150:250] = tag


cv2.imshow('image', img)
cv2.waitKey(0)
# cv2.destoryAllWindows()
