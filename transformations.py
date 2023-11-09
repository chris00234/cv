import cv2 as cv
import numpy as np

img = cv.imread('Photos/ellie1.jpeg')

cv.imshow('ellie', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, 100)
cv.imshow('Translate', translated)

#Rotation
def rotate(img, angle, rotPoint = None):
    height, width = img.shape[:2]
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, scale = 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)
    

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

rotated_again = rotate(rotated, 45)

cv.imshow('rotated again', rotated_again)

# Resizing 
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow('resized', resized)

#flipping
#flipcode = 1, 0, or -1
vertical_flip = cv.flip(img, 0)
cv.imshow('Vertical Flip', vertical_flip)

horizontal_fip = cv.flip(img, 1)
cv.imshow('Horizontal Flip', horizontal_fip)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)