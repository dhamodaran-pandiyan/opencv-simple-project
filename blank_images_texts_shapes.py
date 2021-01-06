import cv2
import numpy as np

#blank image
img = np.zeros((512,512,3), np.uint8)

print(img)
# blank blue image
# img[:] = 255, 0, 0

# part of blue 
# img[10:200, 100:200] = 255, 0, 0

#draw a line with x, y points
cv2.line(img, (0,0), (100,100),(0,255,0),2 )

#diagonal line
cv2.line(img, (0,0), (img.shape[1],img.shape[0]),(0,255,0),2 )

#rectangle
# cv2.rectangle(img, (350,100),(450,200),(0,255,0),2)
cv2.rectangle(img, (350,100),(450,200),(0,255,0),cv2.FILLED)

#circle
# cv2.circle(img, (150,400),50,(0,255,0),2)
cv2.circle(img, (150,400),50,(0,255,0),cv2.FILLED)

#text
cv2.putText(img, "Text here", (75,50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 2)

cv2.imshow("blank_image",img)

cv2.waitKey(0)