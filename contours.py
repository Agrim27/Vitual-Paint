import cv2
def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(img1, cnt, -1, (0, 255, 0), 3)
            print("Perimeter = ", cv2.arcLength(cnt, True))
            app = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            cor = len(app)
            print(cor)
            x, y, w, h = cv2.boundingRect(app)
            if cor == 3:
                type = "triangle"
            elif cor == 4:
                aspratio = w/float(h)
                if aspratio > 0.95 and aspratio <1.05: type = "square"
                else:type = "rectangle"
            elif cor == 5: type = "pentagon"
            elif cor == 6: type = "hexagon"
            elif cor > 7 : type = "circle"
            else:
                type = "none"
            cv2.putText(img1, type, (x + (w // 2) - 10, y + (h // 2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)


img = cv2.imread('shapes.jpg')
# need a binary image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray, 1)
canny = cv2.Canny(blur, 50, 50)
img1 = img.copy()
getContours(canny)



cv2.imshow('image', img)
cv2.imshow('canny', canny)
cv2.imshow('blur', blur)
cv2.imshow('result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
