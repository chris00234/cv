import cv2 as cv

img = cv.imread('Photos/jenna.jpg')
cv.imshow('jenna', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #greater than 150 than set it to 255, otherwise set it to 0
cv.imshow('Simple threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) #less than 150 than set it to 255, otherwise set it to 0
cv.imshow('Simple threshold Inverse', thresh_inv)

# Adaptive Thresholding 
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 3)

cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)