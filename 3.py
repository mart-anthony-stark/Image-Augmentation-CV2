import numpy as np
import cv2

capture = cv2.VideoCapture('assets/prototype.mp4')

while True:
  ret, frame = capture.read()

  image = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
  cv2.imshow('frame', image)

  keyPressed = cv2.waitKey(1)
  if keyPressed == ord('q'):
    break
  elif keyPressed == ord("p"):
    

capture.release()
cv2.destroyAllWindows()