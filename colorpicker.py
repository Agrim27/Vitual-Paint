import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def empty(a):
    pass


cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('hue min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('hue max', 'TrackBars', 30, 179, empty)
cv2.createTrackbar('sat min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('sat max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('val min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('val max', 'TrackBars', 255, 255, empty)


while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('hue min', 'TrackBars')
    h_max = cv2.getTrackbarPos('hue max', 'TrackBars')
    sat_min = cv2.getTrackbarPos('sat min', 'TrackBars')
    sat_max = cv2.getTrackbarPos('sat max', 'TrackBars')
    val_min = cv2.getTrackbarPos('val min', 'TrackBars')
    val_max = cv2.getTrackbarPos('val max', 'TrackBars')
    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('video', img)
    cv2.imshow('mask', mask)
    cv2.imshow('result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
