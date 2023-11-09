import cv2 as cv
import matplotlib.pyplot as plt

########################################################################
#   OPENCV reads an image as bgr format blue, green, red               #
#   But matplotlib reads an image as rgb format                        #
########################################################################

img = cv.imread('Photos/jenna.jpg')

cv.imshow('Hawaii', img)

plt.imshow(img)
plt.show()

#BGR to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (l*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('LAB',lab)


#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV ---> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB ---> BGR', lab_bgr)


cv.waitKey(0)