#Import Libraries
import cv2
import imutils
    


v  = cv2.VideoCapture('mot.mp4')
#v = cv2.VideoCapture(0)


ret, frame = v.read()
frame = imutils.resize(frame,width=600)
cv2.imshow('Frame',frame)
bb = cv2.selectROI('Frame',frame)
tracker.init(frame,bb)


while True:
    ret, frame = v.read()
    if not ret:
        break
    frame = imutils.resize(frame,width=600)
    (success,box) = tracker.update(frame)
    if success:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
    
v.release()
cv2.destroyAllWindows()



        

