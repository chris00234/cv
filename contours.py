import cv2 as cv
import numpy as np

img = cv.imread('Photos/apple.webp')
cv.imshow('apple', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# canny is preferred over tresh
blur = cv.GaussianBlur(gray, (1,1), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('canny edges', canny)

#if the pixel below 125 set to 0 (black) if above 255, set to 1 (white)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)


#RETR_LIST, RETR_EXTERNAL, RETR_TREE, ...
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours drawn', blank)


cv.waitKey(0)