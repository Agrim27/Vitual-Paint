import cv2

# Read the image
img = cv2.imread('lion.jpg')

# Do the processing
height, width, channels = img.shape
res = cv2.resize(img, [width // 2, height // 2], interpolation=cv2.INTER_CUBIC)

# Show the image
cv2.imshow('image', res)

# Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
