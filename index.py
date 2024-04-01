import cv2

img = cv2.imread("dodge.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
blur_img = cv2.GaussianBlur(gray_image, (21, 21), 0)
upside_img = 255 - blur_img
layout = cv2.divide(gray_image, 255 - upside_img, scale=255)
cv2.imwrite("layout.jpg", layout)