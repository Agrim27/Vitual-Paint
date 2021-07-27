import cv2
import numpy as np

# Read the image
img = cv2.imread('color_image.jpg')
print("original image matrix = ", img.shape)

# Do the processing
############################################
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("hsv image matrix = ", hsv.shape)

(width, height, channel) = hsv.shape
canvas = np.zeros((width, height), np.uint8)

canvas = hsv[:, :, 0]
canvas1 = hsv[:, :, 1]
canvas2 = hsv[:, :, 2]
############################################
# Show the image
cv2.imshow('image', img)
cv2.imshow('hue', canvas)
cv2.imshow('saturation', canvas1)
cv2.imshow('value', canvas2)
# Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
