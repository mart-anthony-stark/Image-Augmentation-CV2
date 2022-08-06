import numpy as np
import cv2
from datetime import datetime
import os
import ctypes  # An included library with Python install.   

def capture_video():
  videopath = 'assets/prototype.mp4'
  capture = cv2.VideoCapture(videopath)

  while True:
    ret, frame = capture.read()
    # width = int(capture.get(3))
    # height = int(capture.get(4))

    image = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image = np.zeros(image.shape, np.uint8)

    height = image.shape[0]
    width = image.shape[1]

    smaller_frame = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame


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

