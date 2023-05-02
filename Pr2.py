import cv2
import time
cap = cv2.VideoCapture('cam_video.mp4')
#Create an object to select the object on the frame
object_detector = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21, 21), 0)

    ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy =cv2.findContours(thresh,
                                          cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        c = max(contours, key= cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0, 255, 9), 2)
        # Print the coordinates of the object to the console
        print("Object coordinates: ({}, {})".format(x, y))


    cv2.imshow('Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #time.sleep(0.1)


cap.release()
cv2.destroyAllWindows()
