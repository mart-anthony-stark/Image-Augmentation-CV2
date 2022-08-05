import numpy as np
import cv2
from datetime import datetime
import os

capture = cv2.VideoCapture('assets/prototype.mp4')

while True:
  ret, frame = capture.read()

  image = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
  cv2.imshow('frame', image)

  keyPressed = cv2.waitKey(1)
  if keyPressed == ord('q'):
    break
  elif keyPressed == ord("p"):
    current_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
    filename = "Recording-"+ current_time + ".jpg"
    if not cv2.imwrite('captures/'+filename, image):
      raise Exception("Could not write image")


capture.release()
cv2.destroyAllWindows()