import cv2
import numpy as np

def getContours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgCopy,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)  #way to find corner points.
            #print(len(approx))
            objcor = len(approx)
            #creating a bounding box around object.
            x,y,w,h =  cv2.boundingRect(approx)
            if objcor ==3 : objectType = 'tri'
            elif objcor ==4:
                aspRatio=w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:objectType='square'
                else:objectType= 'rect.'
            elif objcor>6 : objectType="circle"
            elif objcor==5 : objectType='pentagon'
            elif objcor==6 :objectType= 'hexagon'
            else:objectType= 'none'



            cv2.rectangle(imgCopy,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgCopy,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,
                        (0,0,0),2)




img = cv2.imread('shapes.jpg')
imgCopy = img.copy()
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(grayImg,(7,7),0.7)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


cv2.imshow('shapes', img)
cv2.imshow('gray Image', grayImg)
cv2.imshow('blurred image', imgBlur)
cv2.imshow('canny Image', imgCanny)
cv2.imshow('contour drawings', imgCopy)
cv2.waitKey(0)
