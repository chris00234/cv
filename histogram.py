import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/jenna.jpg')
cv.imshow('Jenna', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 500, 255, -1)
masked = cv.bitwise_and(blank, blank, mask = mask)
cv.imshow('mask', masked)

#Grayscale histogram
#                        image, channel, mask, 
gray_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('num of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


#color histogram

plt.title('Colorscale Histogram')
plt.xlabel('Bins')
plt.ylabel('num of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color = col)
    #print(f'i = {i}, col = {col}')
    plt.xlim([0,256])
    
plt.show()


cv.waitKey(0)