import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\\StudyatCLass\\Study\\class\\Xulianhso\\Code\\lena.tif', cv2.IMREAD_GRAYSCALE)

ro, co = img.shape

binary = np.zeros([ro, co], dtype='uint8')
hard = np.zeros([ro, co], dtype='uint8')
soft = np.zeros([ro, co], dtype='uint8')

T = 120

for i in range(ro):
    for j in range(co):
        if img[i, j] <= T:
            binary[i, j] = 0
        else:
            binary[i, j] = 255
        if abs(img[i, j]) <= T:
            hard[i, j] = 0
        else:
            hard[i, j] = img[i, j]

        if abs(img[i, j]) <= T:
            soft[i, j] = 0
        elif img[i, j] > T:
            soft[i, j] = img[i, j] - T
        elif img[i, j] < -T:
            soft[i, j] = img[i, j] + T

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Binary Thresholding')
plt.imshow(binary, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Hard Thresholding')
plt.imshow(hard, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Soft Thresholding')
plt.imshow(soft, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
