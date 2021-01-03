import cv2

# to read image
# img = cv2.imread("Resources/hello_img.png")
# cv2.imshow("Window title", img)
# cv2.waitKey(0)


#TO READ LOCAL VIDEO
# frameWidth = 482
# frameHeight = 360
# cap = cv2.VideoCapture("Resources/video.mp4")
# while(True):
#     success, img = cap.read()
#     cv2.imshow("img", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): 
#         break


frameWidth = 482
frameHeight = 360
cap = cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)
while(True):
    success, img = cap.read()
    img = cv2.resize(img, (frameHeight, frameWidth))
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap = cv2.VideoCapture(0)