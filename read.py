import cv2 as cv

#---------------read Image----------------------------------
#img = cv.imread('Photos/ellie1.jpeg')
#cv.imshow('Ellie', img)

#cv.waitKey(0) #If any keyboard key interrupted, close it
#-----------------------------------------------------------

#---------------read Video----------------------------------
capture = cv.VideoCapture('Videos/eliie_video1.MOV')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()