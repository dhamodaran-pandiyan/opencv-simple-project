import cv2

path2 = "Resources/image.jpg"
img = cv2.imread(path2)
print(img.shape)
cv2.imshow("img", img)

#image resize
width, height = 400, 400
img_resize = cv2.resize(img, (width, height))
print(img_resize.shape)
cv2.imshow("img resized", img_resize)

#img crop
img_crop = img[0:200, 0:750]
cv2.imshow("img cropped", img_crop)

#img crop + resize
img_crop_resize = cv2.resize(img_crop, (img.shape[1], img.shape[0]))
cv2.imshow("img cropped_resized", img_crop_resize)

cv2.waitKey(0)