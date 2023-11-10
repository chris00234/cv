import cv2 as cv
import numpy as np

img = cv.imread('Photos/jenna.jpg')
cv.imshow('Jenna', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F) #compute gradient of the image
lap = np.uint8(np.absolute(lap)) # compute negative to absolute(pos)
cv.imshow('Laplacian', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('Combined sobel', combined_sobel)

canny = cv.Canny(gray, 155, 255)
cv.imshow('Canny', canny)


cv.waitKey(0)