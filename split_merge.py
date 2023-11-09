import cv2 as cv
import numpy as np

img = cv.imread('Photos/Hawaii.jpg')
cv.imshow('Hawaii', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged image', merged)

# To see actual color
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)