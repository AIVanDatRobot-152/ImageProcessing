import cv2
from scipy.signal import convolve2d
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code\speckle_noise_6.png', 0)

h1 = 1/9 * np.ones((3, 3), dtype=np.float32)
h2 = 1/16 * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]], dtype=np.float32)

img_out1 = convolve2d(img, h1, mode='same')
img_out1 = np.round(img_out1)
img_out1 = np.array(img_out1, dtype=np.uint8)

img_out2 = convolve2d(img, h2, mode='same')
img_out2 = np.round(img_out2)
img_out2 = np.array(img_out2, dtype=np.uint8)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(img_out1, cmap='gray')
plt.title('Lowpass Filtering 1')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(img_out2, cmap='gray')
plt.title('Lowpass Filtering 2')
plt.axis('off')

plt.tight_layout()
plt.show()
