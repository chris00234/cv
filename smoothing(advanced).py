import cv2 as cv

img = cv.imread('Photos/ellie2.jpeg')

cv.imshow('Ellie', img)

# averaging blur
average = cv.blur(img, (3,3)) # (#,#) is kernel size. So there is window on image and e.g) 3 x 3 window calculate the pixel near 8 areas and calculate the average it and apply blur based on that average
cv.imshow('Average Blur', average)

# Gaussian Blur (less blur than average blur method)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gaussian blur", gauss)

# Median blur
median = cv.medianBlur(img, 3) #35 is kernel size
cv.imshow("median", median)

# Bilateral blur (most effective)
bilaterial = cv.bilateralFilter(img, 55, 75, 55) #src, kernel, sigma color, sigma space(how far calculate central)
cv.imshow('Bilaterial', bilaterial)


cv.waitKey(0)