import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\\StudyatCLass\\Study\\class\\Xulianhso\\Code\\lena.tif')

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ro, co = grayscale.shape

binary = np.zeros((ro, co), dtype='uint8')
hard = np.zeros((ro, co), dtype='uint8')
soft = np.zeros((ro, co), dtype='uint8')

T = 120

# Áp dụng các thuật toán thresholding
for i in range(ro):
    for j in range(co):
        # Binary Thresholding
        if grayscale[i, j] <= T:
            binary[i, j] = 0
        else:
            binary[i, j] = 255

        # Hard Thresholding
        if abs(grayscale[i, j]) <= T:
            hard[i, j] = 0
        else:
            hard[i, j] = grayscale[i, j]

        # Soft Thresholding
        if abs(grayscale[i, j]) <= T:
            soft[i, j] = 0
        elif grayscale[i, j] > T:
            soft[i, j] = grayscale[i, j] - T
        elif grayscale[i, j] < -T:
            soft[i, j] = grayscale[i, j] + T

# Hiển thị kết quả
cv2.imshow('Original Grayscale Image', grayscale)
cv2.imshow('Binary Thresholding', binary)
cv2.imshow('Hard Thresholding', hard)
cv2.imshow('Soft Thresholding', soft)

# Đợi người dùng nhấn phím và đóng các cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()
