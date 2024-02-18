'''
IN THIS CHAPTER WE WILL LEARN ABOUT HOW TO RUN A IMAGE USING PYTHON

IMPORT CV2 PAKAGE
using imread function read the img from the resource path
use imshow function to display the img by passing the window name and img variable
CALL THE WAITKEY function AND PASS VALUE 0 AS ARGUMENT
'''

import cv2

img=cv2.imread("resource/img.png")
cv2.imshow("img",img)
cv2.waitKey(100)

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    sucess,img1=cap.read()
    print(sucess)
    cv2.imshow("video",img1)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break