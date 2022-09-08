import numpy as np
import cv2

def bgr_to_hsv(bgr_mtx):
  # green = np.uint8([[[0,255,0 ]]])
  return cv2.cvtColor(bgr_mtx, cv2.COLOR_BGR2HSV)

print(bgr_to_hsv(np.uint8([[[34,98,98 ]]])))
print(bgr_to_hsv(np.uint8([[[0,255,255 ]]])))