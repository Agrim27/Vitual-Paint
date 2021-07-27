import cv2
import numpy as np


def empty(a):
    pass


path = '/home/shank53/PycharmProjects/SummerProject/lion.jpg'
cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('hue min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('hue max', 'TrackBars', 30, 179, empty)
cv2.createTrackbar('sat min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('sat max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('val min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('val max', 'TrackBars', 255, 255, empty)

w = 700
h = 500

while True:
    img = cv2.imread(path)
    imgResize = cv2.resize(img, (w // 2, h // 2))
    imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
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
    imgResult = cv2.bitwise_and(imgResize, imgResize, mask=mask)
    cv2.imshow('resized image', imgResize)
    cv2.imshow('HSV image', imgHSV)
    cv2.imshow('mask', mask)
    cv2.imshow('result', imgResult)
    cv2.waitKey(1)

