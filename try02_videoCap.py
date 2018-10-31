import cv2

vid = cv2.VideoCapture(0)       # Arg can be name of file or integer number of camera device.
# vid = cv2.VideoCapture('Name_of_Video')

while True:
    ret, frame = vid.read()     # Returns a value (read documentation of OpenCv) and frames of video.
    frame2 = cv2.flip(frame, 1)     # Flips every frame horizontally (mirror image).
    frame3 = cv2.flip(frame, 0)     # Flips frame vertically (water image).
    grey_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # Converts frames to shades of grey.

    cv2.imshow('Gray_Me', grey_scale)
    cv2.imshow('Horizontal', frame2)
    cv2.imshow('Vertical', frame3)
    cv2.imshow('Original', frame)
    key = cv2.waitKey(1)          # Args are in millisecond.
    if key == 27:   # Press 'Esc' to close windows.
        break

vid.release()       # Closes video file or capturing device.
cv2.destroyAllWindows()
