import cv2
import numpy as np

# Đọc ảnh màu
RGB = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif', 1)

# Tách các kênh màu
blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]

# Chuyển đổi ảnh RGB thành ảnh xám (grayscale) theo công thức trung bình
grayscale = red*(0.299) + green*(0.587) + blue*(0.114)
grayscale = grayscale.astype(np.uint8)
negative_image = cv2.merge([255-blue, 255-green, 255-red])
# Tạo ảnh bù (negative) của ảnh xám
negative_grayscale = 255 - grayscale

# Hiển thị ảnh xám và ảnh bù
cv2.imshow('Grayscale Image', grayscale)
cv2.imshow('Negative Grayscale Image', negative_grayscale)
cv2.imshow('Negative Image', negative_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
