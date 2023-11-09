import cv2 as cv

#Images, Videos, live videos
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    #shape[0] = height, shape[1] = width
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


#only work on live video eg. cam
def changeRes(width, height):
    capture.set(3, width) # 3 is width
    capture.set(4, height) # 4 is height



#---------------read Image----------------------------------
img = cv.imread('Photos/ellie1.jpeg')
resized_img = rescaleFrame(img)

cv.imshow('Ellie', img)
cv.imshow('Ellie_img_resized', resized_img)


cv.waitKey(0) #wait anykey to run bottom code


#---------------read Video----------------------------------
capture = cv.VideoCapture('Videos/eliie_video1.MOV')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()