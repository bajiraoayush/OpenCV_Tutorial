import cv2
import numpy as np


man = cv2.imread('Man.jpg')
hat = cv2.imread('Hat.jpg')
hat_grey = cv2.cvtColor(hat, cv2.COLOR_BGR2GRAY)

man = man[:, 50:538]        # To add images, they should be of the same size.

added_img = cv2.add(man, hat)   # Adds values of every pixel.
# Example : added_img[0, 0] = man[0, 0] + hat[0, 0]

add_weighted = cv2.addWeighted(man, 1, hat, 0.5, 0)     # Adds value of every pixel according to the next arg.
# Example : added_img[0, 0] = man[0, 0]*1 + hat[0, 0]*0.5

ret, threshold = cv2.threshold(hat_grey, 200, 210, cv2.THRESH_BINARY_INV)
# All values before 50 wil become black and all values after 200 will become white.

no_background = cv2.add(hat, hat, mask=threshold)


# cv2.imshow('Added Image', added_img)
# cv2.imshow('Weighted Add Image', add_weighted)
cv2.imshow('Threshold', threshold)
cv2.imshow('No Background', no_background)
cv2.waitKey(0)
cv2.destroyAllWindows()
