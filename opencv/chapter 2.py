import cv2
import numpy as np
kernal=np.ones((5,5),np.uint8)

img=cv2.imread("resource/img.png")
cv2.imshow("widow",img)
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey",imggrey)
imgcanny=cv2.Canny(img,500,510)
cv2.imshow("edge view",imgcanny)
imgdi=cv2.dilate(imgcanny,kernal,iterations=1)
cv2.imshow("dialatien",imgdi)
imgerode=cv2.erode(imgdi,kernal,iterations=1)
cv2.imshow("eroded image",imgerode)
cv2.waitKey(0)