import cv2
import numpy as np

# cap = cv2.VideoCapture('image/mission.jpg')
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # 3 for width from document
    height = int(cap.get(4))  # 4 for height from document

    image = np.zeros(frame.shape, np.uint8)
    # making smaller frame for 4 videos
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # assume its a four part of a square
    # first starting from 0 to height divide by 2 and starting from 0 width divide by 2
    # so we get the first top left corner and then other s as same

    image[:height // 2, :width //
          2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  # top left
    image[height // 2:, :width // 2] = smaller_frame   # bottom right position
    image[:height // 2, width //
          2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  # Bottom left
    image[height // 2:, width // 2:] = smaller_frame  # top right position

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
