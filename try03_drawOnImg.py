import cv2
import numpy as np


img = cv2.imread("1.jpg")       # Reading image.

shape = img.shape    # Gets the dimensions of the image.
print('Shape =', shape)


cv2.line(img, (50, 50), (430, 802), (255, 0, 0), thickness=2)
# Draws a line on 1st arg, from 1st point (2nd arg) to 2nd point # (3rd arg) in the color of 4rd arg.


cv2.circle(img, (640, 426), 25, (0, 0, 255), -1)
# Draws a circle on 1st arg at pixel 2nd arg of radius 3rd arg of color 4th arg.
# 5th arg is optional, negative integers will fill the circle.


cv2.rectangle(img, (20, 20), (140, 140), (0, 255, 255), -1)
# Draws a rectangle on 1st arg, from pixel in 2nd arg to pixel in 3rd arg, in 4th arg color.
# 5th arg is optional, negative integers will fill the rectangle.


cv2.ellipse(img, (470, 270), (100, 50), 0, 120, 240, (0, 120, 120), -1)
# Draws an ellipse on 1st arg, with centre as pixel in 2nd arg, angle of ellipse wrt X-axis is 3rd arg.
# Starting angle of ellipse is 4th arg and ending angle is 5th arg (Partial part of ellipse can also be shown).
# 6th arg is color.
# 7th arg is optional, negative integers will fill the ellipse.


points = np.array([[[550, 200], [650, 200], [550, 300], [650, 300]]], np.int32)
# Next code explains this line properly.
cv2.polylines(img, [points], True, (50, 100, 150), thickness=5)
# Draws a polygon on 1st arg, 2nd arg defines the corners in order.
# 3rd arg decides whether the polygon should be closed or not, 4th arg is the colour.


font = cv2.FONT_HERSHEY_COMPLEX_SMALL
# Selecting a font.
cv2.putText(img, 'Ground', (450, 50), font, 2, (200, 200, 200))
# Writes text on image (1st arg), the text is 2nd arg, 3rd arg is the starting pixel of the text.
# 4th arg is the font, 5th arg is font-size, 6th arg is colour of text.

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
