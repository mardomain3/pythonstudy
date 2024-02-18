#HERE I AM GOING TO A WRITE A VIDEO
import cv2
import numpy as np


cap=cv2.VideoCapture("resource/vid.mp4")
forcc=cv2.VideoWriter_fourcc(*'MJPG')
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
hight=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps=cap.get(cv2.CAP_PROP_FPS)
out=cv2.VideoWriter("resource/VIDEO.AVI",forcc,fps,(int(width),int(hight)))
while True:
    sucess,frame=cap.read()
    img1=cv2.flip(frame,1)
    #final=np.hstack([frame,img1])
    cv2.imshow("window",img1)
    out.write(img1)
    if cv2.waitKey(2)==27:
        break
out.release()
cap.release()
cv2.destroyAllWindows()