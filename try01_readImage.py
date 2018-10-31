import cv2      # Library used for Image Processing.

img = cv2.imread("1.jpg")       # Takes an image as argument and reads it.
grey_img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)        # Reads image and converts it to shades od grey.

cv2.imshow('Grey Img', grey_img)        # Displays the image (2nd arg) with the 1st arg as name of the window.
cv2.imwrite('Grey_1.jpg', grey_img)     # Makes another image file in the given path (1st arg) of the image (2nd arg).
cv2.imshow('Image', img)
cv2.waitKey(0)      # Waits for 'arg' milliseconds before closing display window.
# Returns the ascii value of any key pressed when window was open.

cv2.destroyAllWindows() # Closes all display windows opened by OpenCV.
