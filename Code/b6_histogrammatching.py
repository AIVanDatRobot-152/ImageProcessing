import numpy as np
import matplotlib.pyplot as plt

img = np.array([[13, 14, 2, 14],
                [10, 2, 5, 9],
                [15, 15, 3, 15],
                [15, 8, 13, 1]], dtype=np.uint8)

img2 = np.array([[11, 13, 0, 13],
                [7, 0, 2, 5],
                [15, 15, 1, 15],
                [15, 4, 11, 0]], dtype=np.uint8)

gray_level = np.array(list(range(16)))

ro,co = img.shape
n= ro*co

Au= np.zeros(len(gray_level),dtype=np.float32)
pAu= np.zeros(len(gray_level),dtype=np.float32)
Bu= np.zeros(len(gray_level),dtype=np.float32)
pBu= np.zeros(len(gray_level),dtype=np.float32)

for i in range(len(gray_level)):
    Au[i] = np.sum(img == gray_level[i])
    pAu[i] = Au[i]/n
    Bu[i] = np.sum(img2 == gray_level[i])
    pBu[i] = Bu[i]/n

preA = 0
preB = 0
cum_an= np.zeros(len(gray_level),dtype=np.float32)
cum_bn= np.zeros(len(gray_level),dtype=np.float32)
for i in range(len(gray_level)):
    cum_an[i] = preA + pAu[i]
    preA = cum_an[i]
    cum_bn[i] = preB + pBu[i]
    preB = cum_bn[i]
C = np.zeros([ro,co], dtype='uint8')
c_gray =np.zeros(len(gray_level),dtype=np.float32)
cum_cn =np.zeros(len(gray_level),dtype=np.float32)
for i in range(len(cum_bn)):
    temp = np.argwhere(cum_an>=cum_bn[i]).min()
    c_gray[i] = temp 
for i in range(ro):
     for j in range(co):
            C[i, j] = c_gray[img2[i,j]]
Cu= np.zeros(len(gray_level),dtype=np.float32)
pCu= np.zeros(len(gray_level),dtype=np.float32)
for i in range(len(gray_level)):
    Cu[i] = np.sum(C == gray_level[i])
    pCu[i] = Cu[i]/n
preC = 0
cum_cn= np.zeros(len(gray_level),dtype=np.float32)
for i in range(len(gray_level)):
    cum_cn[i] = preC + pCu[i]
    preC = cum_cn[i]
print('Phân phối tích lũy của ảnh C', cum_cn)
print(C)
print(c_gray)
plt.plot(gray_level,cum_an,'o', color='b', label='Hình A')
plt.plot(gray_level,cum_cn,'x', color='r', label='Hình C')
plt.xlabel('Mức xám')
plt.ylabel('Phân phối tích lũy')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Histogram of Original Image')
plt.plot(gray_level,cum_an,'o', color='b', label='Hình A')
plt.xlabel('Mức xám')
plt.ylabel('Phân phối tích lũy')
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Histogram of New Image')
plt.plot(gray_level,cum_cn,'x', color='r', label='Hình C')
plt.xlabel('Mức xám')
plt.ylabel('Phân phối tích lũy')
plt.legend()

plt.tight_layout()
plt.show()
