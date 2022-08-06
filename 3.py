import numpy as np
import cv2
from datetime import datetime
import os
import ctypes  # An included library with Python install.   


def capture_video():
  capture = cv2.VideoCapture('assets/prototype.mp4')

  while True:
    ret, frame = capture.read()

    image = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('frame', image)

    keyPressed = cv2.waitKey(1)
    if keyPressed == ord('q'): # Quit program
      break
    elif keyPressed == ord("p"): # PrintScreen
      # Check whether the specified path exists or not
      path = "captures"
      isExist = os.path.exists(path)

      if not isExist:
        # Create a new directory because it does not exist 
        os.makedirs(path)
        
      current_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
      filename = "Recording-"+ current_time + ".jpg"
      if not cv2.imwrite('captures/'+filename, image):
        raise Exception("Could not write image")


  capture.release()
  cv2.destroyAllWindows()


choice = ctypes.windll.user32.MessageBoxW(0, "q - Quit \np - PrintScreen", "Video Capture", 1)

if choice == 1:
  capture_video()

