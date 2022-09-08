import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  width = int(cap.get(3))
  height = int(cap.get(4))

  # convert bgr to hsv
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # lower_blue = np.array([110,50,50])
  # upper_blue = np.array([130,255,255])
  lower_green = np.array([60-10,138,129])
  upper_green = np.array([60+10,255,255])

  mask = cv2.inRange(hsv, lower_green, upper_green)
  result = cv2.bitwise_and(frame, frame, mask=mask)

  cv2.imshow('frame', result)
  cv2.imshow('mask', mask)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

# ? find HSV values to track
# def find_hsv(rgb_arr):
#   # green = np.uint8([[[0,255,0 ]]])
#   return cv2.cvtColor(rgb_arr, cv2.COLOR_BGR2HSV)

