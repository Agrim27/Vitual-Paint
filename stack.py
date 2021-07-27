import numpy as np
import cv2

img = cv2.imread('lion.jpg')

imgHor = np.hstack((img, img))  # two images can only be stacked if they have same no of channels
imgVer = np.vstack((img, img))  # eg not work for rgb and gray
cv2.imshow('Horizontal', imgHor)
cv2.imshow('Vertical', imgVer)
cv2.waitKey(0)
cv2.destroyAllWindows()
