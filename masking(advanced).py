import cv2 as cv
import numpy as np


img = cv.imread('Photos/jenna.jpg')
cv.imshow('Jenna', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 300, img.shape[0]//2), 500, 255, -1)
cv.imshow('Mask', circle)

masked = cv.bitwise_and(img, img, mask = circle)
cv.imshow('Masked', masked)

rectangle = cv.rectangle(blank.copy(), (0,0), (img.shape[1]//2, img.shape[0]//2), 255, -1)
cv.imshow('rectangle', rectangle)
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('weird_shape', weird_shape)

masked2 = cv.bitwise_and(img, img, mask = weird_shape)
cv.imshow('Masked Image', masked2)




cv.waitKey(0)