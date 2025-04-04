import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.array([[117, 170, 130, 54, 84, 209, 164, 148], 
                [135, 151, 137, 96, 56, 157, 255, 189], 
                [136, 152, 174, 146, 64, 84, 146, 90], 
                [123, 139, 182, 133, 51, 71, 56, 74], 
                [119, 137, 172, 146, 116, 65, 70, 75], 
                [90, 123, 166, 184, 203, 101, 49, 64], 
                [85, 102, 162, 194, 164, 80, 38, 56], 
                [73, 84, 155, 185, 147, 163, 87, 57]], dtype='uint8')

ro, co = img.shape
binary = np.zeros([ro, co], dtype='uint8')
hard = np.zeros([ro, co], dtype='uint8')
soft = np.zeros([ro, co], dtype='uint8')
T = 120

for i in range(ro):
    for j in range(co):
        # Binary Thresholding
        if img[i, j] <= T:
            binary[i, j] = 0
        else:
            binary[i, j] = 1

        # Hard Thresholding
        if abs(img[i, j]) <= T:
            hard[i, j] = 0
        else:
            hard[i, j] = img[i, j]
        # Soft Thresholding
        if abs(img[i, j]) <= T:
            soft[i, j] = 0
        elif img[i, j] > T:
            soft[i, j] = img[i, j] - T
        elif img[i, j] < -T:
            soft[i, j] = img[i, j] + T
print("Binary Thresholding Result:\n", binary)
print("Hard Thresholding Result:\n", hard)
print("Soft Thresholding Result:\n", soft)