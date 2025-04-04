import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

def gaussian_filter(kernel_size, sigma, mu):
    x, y = np.meshgrid(np.linspace(-2, 2, kernel_size), np.linspace(-2, 2, kernel_size))
    dst = np.sqrt(x**2 + y**2)
    
    normal = 1 / (2.0 * np.pi * sigma**2)
    gauss = np.exp(-((dst - mu)**2 / (2.0 * sigma**2))) * normal
    return gauss

# Gaussian filter parameters
kernel_size = 9
sigma = 7
mu = 0
H = gaussian_filter(kernel_size, sigma, mu)

# Read the input image
I = cv2.imread(r'F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif', 0)
image =  convolve2d(I,H, mode ='same')

HX = np.array([[-1, 0, 1],
               [-1, 0, 1],
               [-1, 0, 1]], dtype=np.float32)
HY = np.array([[-1, -1, -1],
               [0, 0, 0],
               [1, 1, 1]], dtype=np.float32)

GX = convolve2d(image, HX, mode='same')
GY = convolve2d(image, HY, mode='same')

G = np.sqrt((GX**2) + (GY**2))

angle = np.arctan(GY,GX)
ro,co = image.shape

for i in range(ro):
    for j in range(co):
        if angle[i,j] <0:
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
# BW= BW*G
# print(BW.dtype)

# cv2.imshow('BW',BW)
# cv2.waitKey(0)
# cv2.destroyAllWindows

fig, axs = plt.subplots(1,6)
axs[0].imshow(image, cmap = 'gray')
axs[0].set_xticks(())
axs[0].set_yticks(())
axs[0].set_title('Original IMG')
axs[1].imshow(I, cmap = 'gray')
axs[1].set_xticks(())
axs[1].set_yticks(())
axs[1].set_title('làm mịn')
axs[2].imshow(angle, cmap = 'gray')
axs[2].set_xticks(())
axs[2].set_yticks(())
axs[2].set_title('Angle')
axs[3].imshow(angle2, cmap ='gray')
axs[3].set_xticks(())
axs[3].set_yticks(())
axs[3].set_title('Angle2')
axs[4].imshow(BW, cmap = 'gray')
axs[4].set_xticks(())
axs[4].set_yticks(())
axs[4].set_title('BW')
axs[5].imshow(G, cmap = 'gray')
axs[5].set_xticks(())
axs[5].set_yticks(())
axs[5].set_title('G')


plt.show()
