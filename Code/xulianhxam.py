import cv2
import numpy as np

# Đọc ảnh
RGB = cv2.imread('Code/chill.jpg', 1)

# Tách các kênh màu
blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]

# Hiển thị hình ảnh
cv2.imshow('Display red image', red)
cv2.imshow('Display green image', green)
cv2.imshow('Display blue image', blue)

cv2.waitKey(0)
cv2.destroyAllWindows()
