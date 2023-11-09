import cv2 as cv

img = cv.imread('Photos/ellie1.jpeg')
cv.imshow('ellie', img)


#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('ellie-gray', gray)

#blur
#                           blur power
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#Edge Cascade
Canny = cv.Canny(img, 125, 175) # can decrese edges with blur
cv.imshow('Canny edges', Canny)

#Dilating the image
dilated = cv.dilate(Canny, (7,7), iterations = 5)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations = 3)
cv.imshow('eroded', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Cropping
cropped = img[100:, 100:800]
cv.imshow('cropped', cropped)

cv.waitKey(0)