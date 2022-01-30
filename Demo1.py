import cv2
import time
import numpy as np
fourCC=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('output.avi',fourCC,20.0,(640,480))
cap=cv2.VideoCapture(0)
time.sleep(2)
bg=0
for i in range(60):
    ret,bg=cap.read()
bg=np.flip(bg,axis=1)
while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_black=np.array([30,300,0])
    upper_black=np.array([104,153,70])
    mask1=cv2.inRange(hsv,lower_black,upper_black)

    lower_black=np.array([30,300,0])
    upper_black=np.array([104,153,70])
    mask2=cv2.inRange(hsv,lower_black,upper_black)
    mask1=mask1+mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    re1=cv2.bitwise_and(img,img,mask=mask2)
    re2=cv2.bitwise_and(bg,bg,mask=mask1)
    final_output=cv2.addWeighted(re1,1,re2,1,0)
    output_file.write(final_output)
    cv2.imshow("magic",final_output)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()