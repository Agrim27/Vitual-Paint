import cv2

cap = cv2.VideoCapture(0)

# Video Loop
while True:
    # Read the image
    [ret, img] = cap.read()
    ## Do the processing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 100, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    # Show the image
    cv2.imshow('image', img)

    # End the video loop
    if cv2.waitKey(1) == 27:  # 27 - ASCII for escape key
        break

# Close and exit
cap.release()
cv2.destroyAllWindows()
