import numpy as np
import cv2

img = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code\chill.jpg')

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

grayscale = red*(0.299) + green*(0.587) + blue*(0.114)
grayscale = grayscale.astype(np.uint8)

ro, co = grayscale.shape

new_img = np.zeros([ro, co], dtype='uint8')

i = np.unique(grayscale)
L = i[1]
M = i[len(i)-2]

Imax = 255
Imin = 0

factor = (Imax - Imin) / (M - L)

for i in range(ro):
    for j in range(co):
        if grayscale[i, j] < L:
            new_img[i, j] = Imin
        elif grayscale[i, j] > M:
            new_img[i, j] = Imax
        else:
            new_img[i, j] = np.round(factor * (grayscale[i, j] - L)).astype(np.uint8)

cv2.imshow('Original Image', grayscale)
cv2.imshow('Contrast Stretched Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Ảnh gốc:")
print(grayscale)
print("Ảnh sau khi kéo dãn tương phản:")
print(new_img)
