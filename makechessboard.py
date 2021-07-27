import numpy as np
import cv2

fullpattern = np.zeros((400, 400), np.uint8)
fullpattern[200:400, 0:200] = 255
fullpattern[0:200, 200:400] = 255
cv2.imshow('canvas', fullpattern)
cv2.waitKey(0)
cv2.destroyAllWindows()
