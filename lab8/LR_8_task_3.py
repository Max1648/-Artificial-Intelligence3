import cv2
import numpy as np
img = cv2.imread("Maks12.jpg")
print(img.shape)
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)
imgCropped = img[75:400, 30:350]
cv2.imshow("Image", img)
# cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)