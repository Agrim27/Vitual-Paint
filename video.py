import cv2


# Initialize camera
cap = cv2.VideoCapture(0)

############################################

############################################
# Video Loop
while True:

    # Read the image
    ret, frame = cap.read()
    # Show the image
    cv2.imshow('image', frame)

    # End the video loop
    if cv2.waitKey(1) == 27:  # 27 - ASCII for escape key
        break
############################################

############################################
# Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
