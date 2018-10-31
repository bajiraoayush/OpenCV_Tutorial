import cv2

img = cv2.imread('1.jpg')
img_grey = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)

img_GB = cv2.GaussianBlur(img, (5, 5), 0)
img_grey_GB = cv2.GaussianBlur(img_grey, (5, 5), 0)

lap_img = cv2.Laplacian(img, cv2.CV_64F)
lap_img_grey = cv2.Laplacian(img, cv2.CV_64F)
lap_img_GB = cv2.Laplacian(img, cv2.CV_64F)
lap_img_grey_GB = cv2.Laplacian(img, cv2.CV_64F)

canny_img = cv2.Canny(img, 100, 150)
canny_img_grey = cv2.Canny(img_grey, 100, 150)
canny_img_GB = cv2.Canny(img_GB, 100, 150)
canny_img_grey_GB = cv2.Canny(img_grey_GB, 100, 150)


cv2.imshow('Original', canny_img)
cv2.imshow('OG Grey', canny_img_grey)
cv2.imshow('OG GB', canny_img_GB)
cv2.imshow('OG GB Grey', canny_img_grey_GB)

cv2.waitKey(0)
cv2.destroyAllWindows()
