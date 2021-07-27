import cv2

############################################

############################################
# Read the image
from PIL.XVThumbImagePlugin import r

img = cv2.imread('lion.jpg')
############################################

############################################
# Do the processing
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 127 < r < 160, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
############################################

############################################
# Show the image
cv2.imshow('image - thresh1', thresh1)
cv2.imshow('image - thresh2', thresh2)
cv2.imshow('image - thresh3', thresh3)
cv2.imshow('image - thresh4', thresh4)
cv2.imshow('image - thresh5', thresh5)
cv2.imshow('image', img)
############################################

############################################
# Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
