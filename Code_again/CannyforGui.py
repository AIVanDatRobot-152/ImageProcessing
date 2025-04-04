from scipy.signal import convolve2d
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
# Bước 1: Hình ảnh được làm mịn và bằng bộ lọc gaussian và tính tích chập I * H
def gaussian_filter(kernel_size, sigma, mu):
    x, y = np.meshgrid(np.linspace(-2, 2, kernel_size),
                       np.linspace(-2, 2, kernel_size))
    dst = np.sqrt(x**2 + y**2)
    normal = 1 / (2.0 * np.pi * sigma**2)
    gauss = np.exp(-((dst - mu)**2 / (2.0 * sigma **2))) * normal
    return gauss
kernel_size = 5
sigma = 9
mu = 1
H = gaussian_filter(kernel_size, sigma, mu)
I = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code_again\doggo.jpg',0)
image = convolve2d(I, H, mode = 'same')

# Bước 2: Định nghĩa kernel sobel
Hx = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
Hy = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
Gx = convolve2d(image, Hx, mode = 'same')
Gy = convolve2d(image, Hy, mode = 'same')
G = np.sqrt(Gx**2 + Gy**2)
# Tính độ lớn góc pha và điều chỉnh giá trị góc pha
angle = np.arctan2(Gy,Gx)
ro, co = image.shape

for i in range(ro):
    for j in range(co):
        if angle[i,j] < 0:
            angle[i,j] = 360 + angle[i,j]
# Bước 4: Điều chỉnh các góc trong bước 3 đến 0, 45, 90 và 135 gần nhất
angle2 = np.zeros([ro, co], dtype=np.uint8)

for i in range(ro):
    for j in range(co):
        if (angle[i, j] >= 0 and angle[i, j] < 22.5) or (
            angle[i, j] >= 157.5 and angle[i, j] < 202.5) or (
            angle[i, j] >= 337.5 and angle[i, j] < 360):
            angle2[i, j] = 0
        elif (angle[i, j] >= 22.5 and angle[i, j] < 67.5) or (
            angle[i, j] >= 202.5 and angle[i, j] < 247.5):
            angle2[i, j] = 45
        elif (angle[i, j] >= 67.5 and angle[i, j] < 112.5) or (
            angle[i, j] >= 247.5 and angle[i, j] < 292.5):
            angle2[i, j] = 90
        elif (angle[i, j] >= 112.5 and angle[i, j] < 157.5) or (
            angle[i, j] >= 292.5 and angle[i, j] < 337.5):
            angle2[i, j] = 135
# Bước 5: Phương pháp triệt tiêu không cực đại
BW = np.zeros([ro, co])
for i in range(1,ro-1):
    for j in range(1, co-1):
        if angle2[i, j] == 0:
            BW[i,j] = G[i,j] == max(G[i,j], G[i,j+1], G[i,j-1]) 
        elif angle2[i, j] == 45:
            BW[i,j] = G[i,j] == max(G[i,j], G[i+1,j-1], G[i-1,j+1]) 
        elif angle2[i, j] == 90:
            BW[i,j] = G[i,j] == max(G[i,j], G[i+1,j], G[i-1,j]) 
        elif angle2[i, j] == 135:
            BW[i,j] = G[i,j] == max(G[i,j], G[i+1,j+1], G[i-1,j-1]) 
BW= BW*G
# Bước 6: Giá trị ngưỡng
T_Low = 0.02
T_High = 0.08
T_Low = T_Low * max(max(x) for x in BW)
T_High = T_High * max(max(x) for x in BW)
edge_final = np.zeros([co,ro], dtype = 'uint8')

edge_final = np.zeros_like(BW, dtype=np.uint8)

for i in range(ro):
    for j in range(co):
        if (BW[i,j] < T_Low):
            edge_final[i,j] = 0
        elif (BW[i,j] > T_High):
            edge_final[i,j] = 1
edge_final = edge_final*255

# Hiển thị kết quả
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(I, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(BW, cmap='gray')
plt.title('Non-Maximum Suppression')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(edge_final, cmap='gray')
plt.title('Final Canny Edges')
plt.axis('off')

plt.suptitle('Canny Edge Detection Steps', fontsize=16)

plt.tight_layout()
plt.show()
