import cv2
import numpy as np

# cap = cv2.VideoCapture('image/blue_test.jpeg')
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # 3 for width from document
    height = int(cap.get(4))  # 4 for height from document

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert BGR into HSV
    # light blue value in HSV find it from color picker
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])  # Dark blue value in HSV

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
