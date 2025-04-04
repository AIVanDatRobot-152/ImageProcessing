from scipy.signal import convolve2d
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code_again\lena.tif', 0)

def edge_detection(img, method='sobel'):
    """Hàm thực hiện phát hiện cạnh Sobel hoặc Prewitt."""
    if method == 'sobel':
        hx = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]], dtype=np.float32)
        hy = np.array([[-1, -2, -1],
                       [0,  0,  0],
                       [1,  2,  1]], dtype=np.float32)
        threshold_value = 10
    elif method == 'prewitt':
        hx = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=np.float32)
        hy = np.array([[-1, -1, -1],
                       [0,  0,  0],
                       [1,  1,  1]], dtype=np.float32)
        threshold_value = 13
    else:
        raise ValueError("Invalid method. Choose 'sobel' or 'prewitt'.")

    # Tính toán Gx và Gy bằng tích chập
    Gx = convolve2d(img, hx, mode='same')
    Gy = convolve2d(img, hy, mode='same')

    # Tính biên độ gradient
    G = np.sqrt(Gx**2 + Gy**2)

    # Chuẩn hóa G về 8-bit
    G_scale = np.uint8(G / G.max() * 255)

    # Tạo ảnh nhị phân dựa trên ngưỡng
    _, binary_img = cv2.threshold(G_scale, threshold_value, 255, cv2.THRESH_BINARY)

    return binary_img

# Thực hiện phát hiện cạnh bằng Sobel
binary_sobel = edge_detection(img, method='sobel')

# Thực hiện phát hiện cạnh bằng Prewitt
binary_prewitt = edge_detection(img, method='prewitt')

# Thực hiện phép trừ hai ảnh nhị phân
binary_difference = cv2.absdiff(binary_sobel, binary_prewitt)

# Hiển thị kết quả
fig, axs = plt.subplots(1, 4, figsize=(15, 5))
fig.suptitle('Comparison of Sobel and Prewitt Edge Detection', fontsize=16)

# Hiển thị ảnh gốc
axs[0].imshow(img, cmap='gray')
axs[0].set_title('Original Image')
axs[0].axis('off')

# Hiển thị ảnh nhị phân Sobel
axs[1].imshow(binary_sobel, cmap='gray')
axs[1].set_title('Binary Sobel')
axs[1].axis('off')

# Hiển thị ảnh nhị phân Prewitt
axs[2].imshow(binary_prewitt, cmap='gray')
axs[2].set_title('Binary Prewitt')
axs[2].axis('off')

# Hiển thị ảnh sau khi trừ
axs[3].imshow(binary_difference, cmap='gray')
axs[3].set_title('Difference (Sobel - Prewitt)')
axs[3].axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.show()
