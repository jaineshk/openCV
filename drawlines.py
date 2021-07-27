import cv2
import numpy as np

# cap = cv2.VideoCapture('image/mission.jpg')
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # 3 for width from document
    height = int(cap.get(4))  # 4 for height from document

    img = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 5)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 20)
    img = cv2.rectangle(img, (250, 50), (500, 300), (56, 23, 160), 10)
    img = cv2.circle(img, (50, 50), 50, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, "tatti", (10, height - 100),
                      font, 1, (0, 0, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
