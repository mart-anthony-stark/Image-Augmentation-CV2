import cv2

# Basic image manipulation and loading
img = cv2.imread("assets/profile.png", cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Mart",img)
cv2.waitKey(0)