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
h = gaussian_filter(kernel_size, sigma, mu)

# Read the input image
f = cv2.imread(r'F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif', 0)
if f is None:
    raise FileNotFoundError("Image not found. Please check the file path.")

# Apply Gaussian filter
filter_f = convolve2d(f, h, mode='same')

# Apply Laplacian filter
kernel = np.array([[0, 1, 0],
                   [1, -4, 1],
                   [0, 1, 0]], dtype=np.float32)
log_f = convolve2d(filter_f, kernel, mode='same')

# Zero-crossing detection
def zero_crossing_detection(log_image, threshold=0):
    img_h, img_w = log_image.shape
    zero_crossing = np.zeros_like(log_image, dtype=np.uint8)

    for i in range(1, img_h - 1):
        for j in range(1, img_w - 1):
            patch = log_image[i-1:i+2, j-1:j+2]
            min_val = np.min(patch)
            max_val = np.max(patch)

            if min_val < 0 and max_val > 0 and (max_val - min_val) > threshold:
                zero_crossing[i, j] = 255

    return zero_crossing

zero_crossing_f = zero_crossing_detection(log_f, 0.55)

# Plot results
fig, axs = plt.subplots(1, 3, figsize=(18, 9))
axs[0].imshow(f, cmap='gray')
axs[0].set_xticks(())
axs[0].set_yticks(())
axs[0].set_title('Original Image')

axs[1].imshow(log_f, cmap='gray')
axs[1].set_xticks(())
axs[1].set_yticks(())
axs[1].set_title('Laplacian of Gaussian')

axs[2].imshow(zero_crossing_f, cmap='gray')
axs[2].set_xticks(())
axs[2].set_yticks(())
axs[2].set_title('Zero Crossing Detection')

plt.tight_layout()
plt.show()
