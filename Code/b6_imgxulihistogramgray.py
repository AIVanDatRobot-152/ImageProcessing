import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif')

blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]

grayscale = red*(0.299) + green*(0.587) + blue*(0.114)
grayscale = grayscale.astype(np.uint8)

L=256
u=np.array(list(range(L)), dtype= 'uint8')

nu= np.zeros(len(u),dtype=np.float32)
pu= np.zeros(len(u),dtype=np.float32)

ro,co = grayscale.shape
n= ro*co

for i in range(len(u)):
    nu[i] = np.sum(grayscale == u[i])
    pu[i] = nu[i]/n

pre = 0
cu= np.zeros(len(u),dtype=np.float32)
v = np.zeros(len(u),dtype=np.float32)

for i in range(len(pu)):
    cu[i] = pre + pu[i]
    v[i] = cu[i]*(L-1)
    pre = cu[i]

v_round = np.round(v)
v_round = np.array (v_round, dtype='uint8')

new_img = np.zeros([ro,co], dtype='uint8')

for i in range(ro):
    for j in range(co):
            new_img[i, j] = v_round[grayscale[i,j]]

cv2.imshow('Original Image', grayscale)
cv2.imshow('Contrast Stretched Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.figure(1)
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()
# plt.figure(2)
# plt.hist(new_img.ravel(), 256, [0, 256])
# plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Histogram of Original Image')
plt.hist(img.ravel(), 256, [0, 256])
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Histogram of New Image')
plt.hist(new_img.ravel(), 256, [0, 256])
plt.legend()

plt.tight_layout()
plt.show()

print("Ảnh gốc:")
print(img)
print("Ảnh sau khi kéo dãn tương phản:")
print(new_img)