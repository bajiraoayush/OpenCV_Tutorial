import cv2
import numpy as np

img = cv2.imread('1.jpg')
# print(img)        # Prints value of every pixel.

# Making our own image.
new_img = np.array([        # Every element of this list is a row of pixels and every row comes one below the other.
    [       # Every element of this list is a pixel and the whole list is a row of pixels.
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0],
        [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0],
    ],
    [
        [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0],
        [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0],
    ],
    [
        [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255],
        [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255],
    ],
], np.uint8)

print(new_img.shape, '\n') # (Columns, Rows, Colours)
print(new_img[0, 0])        # Prints value of pixel (Column = 0, Row = 0)
print(new_img[1, 4])
print(new_img[2, 9])

# cv2.imshow('Image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
