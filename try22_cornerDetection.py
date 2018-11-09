import cv2
import numpy as np

img = cv2.imread("Shapes.jpg")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert to greyscale to put in function.

corners = cv2.goodFeaturesToTrack(img_grey, 100, 0.20, 5)
# Function takes greyscale image as 1st arg, maximum number of corners to be found as 2nd arg.
# 3rd arg is quality (b/w 0 and 1), 4th arg is minimum pixels b/w 2 corners.

corners = np.int0(corners)

for corner in corners:
    a, b = corner.ravel()
    cv2.circle(img, (a, b), 6, (0, 0, 0), -1)

cv2.imshow('Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
