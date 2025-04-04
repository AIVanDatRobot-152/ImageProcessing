import numpy as np

img = np.array([[249, 108, 110, 113],
                [10, 98, 108, 114],
                [85, 100, 96, 104],
                [85, 87, 95, 98]], dtype=np.uint8)

ro,co = img.shape

new_img = np.zeros([ro,co], dtype='uint8')

i = np.unique(img)
L = i[1]
M = i[len(i)-2]
Imax = 255
Imin = 0
factor = (Imax-Imin-2)/(M - L)
for i in range(ro):
    for j in range(co):
        if img[i,j] < L:
            new_img[i,j] = Imin
        elif img[i,j] > M:
            new_img[i,j] =Imax
        else:
            new_img[i, j] = np.round(factor * (img[i, j] - L)+1)

print(new_img)