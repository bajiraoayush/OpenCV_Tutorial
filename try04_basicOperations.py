import cv2
import numpy as np

img = cv2.imread('1.jpg')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print('This is original image.\n', img, '\nEnd of original image.\n\n')        # Prints value of every pixel.

print('This is grey scaled image.\n', img_grey, '\nEnd of grey scaled image.\n\n')
# Every pixel has a single value i.e. every number is a pixel.


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
# The above image is very small. Give more pixels for a bigger picture.


print('Dimensions of image.\n',
      '(Rows, Cols, Channel)\n', new_img.shape, '\n')  # (Columns, Rows, Colours)
print('Value at 0,0 \t', new_img[0, 0])        # Prints value of pixel (Column = 0, Row = 0)
print('Value at 1,4 \t', new_img[1, 4])
print('Value at 2,5 \t', new_img[2, 9])


# Changing a single pixel in an image.
new_img[2, 2] = [0, 0, 0]       # Take a bigger image and change more pixels to see the change.


rows, cols, _ = img.shape

# Cropping an image.
cropped_img = img[rows//4:3*rows//4, cols//4:3*cols//4]


cv2.imshow('Cropped Image', cropped_img)
cv2.imshow('Image', img)
cv2.imshow('New Image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
