import cv2 as cv

img = cv.imread('Photos/ellie1.jpeg')
cv.imshow('ellie', img)


#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('ellie-gray', gray)

cv.waitKey(0)