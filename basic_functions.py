import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)


path = "Resources/hello_img.png"
path2 = "Resources/image.jpg"
img = cv2.imread(path2)

#gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#image blur
img_blur = cv2.GaussianBlur(img_gray,(9,9),0) #increase (9,9) increase blur effect

#edge detector
img_canny = cv2.Canny(img_blur, 100, 100) #decrease values to increase edges

#image dilation
img_dil = cv2.dilate(img_canny , kernel, iterations=1) #increase iter to increase dilation

#image erode
img_eroded = cv2.erode(img_dil, kernel, iterations=1)

#Output
cv2.imshow("image",img)
cv2.imshow("grayimage",img_gray)
cv2.imshow("imageblur",img_blur)
cv2.imshow("imagecanny",img_canny)
cv2.imshow("imagedilate",img_dil)
cv2.imshow("imageerode",img_eroded)
cv2.waitKey(0)