import cv2 as cv
import numpy as np

#dtype = 'uint8' == datatype is image
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

# 1. paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# blank[:] = 0, 0, 255
# cv.imshow('Red', blank)

# # to choose the section
# blank[0:200, 200:300] = 255, 0, 0
# cv.imshow('Blue_partial', blank)

# 2. Draw a rectangle
#             img, origin,   whereto,   color,    thickness = -1, 1, 2, ...
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = cv.FILLED)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
#          img,                where the circle at,   radius(pixels),  color,   thickness
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness= 3)
cv.imshow('circle', blank)
# 4. Draw a line

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness= 3)
cv.imshow('line', blank)

#5. Write a text on img

cv.putText(blank, 'hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (213, 123, 222), 2)
cv.imshow('Text', blank)


# img = cv.imread('Photos/ellie1.jpeg')
# cv.imshow('ellie', img)

cv.waitKey(0)
