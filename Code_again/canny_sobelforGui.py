from scipy.signal import convolve2d
import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

image_path = "F:\StudyatCLass\Study\class\Xulianhso\Code_again\lena.tif"  # Thay bằng đường dẫn đến ảnh của bạn

def canny_algorithm(image_path):
    # Bước 1: Hình ảnh được làm mịn và bằng bộ lọc gaussian
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
    I = cv2.imread(image_path, 0)
    image = convolve2d(I, H, mode='same')

    # Bước 2: Định nghĩa kernel Sobel
    Hx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    Hy = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    Gx = convolve2d(image, Hx, mode='same')
    Gy = convolve2d(image, Hy, mode='same')
    G = np.sqrt(Gx**2 + Gy**2)

    # Tính độ lớn góc pha và điều chỉnh giá trị góc pha
    angle = np.arctan2(Gy, Gx)
    ro, co = image.shape

    for i in range(ro):
        for j in range(co):
            if angle[i, j] < 0:
                angle[i, j] = 360 + angle[i, j]

    # Bước 4: Điều chỉnh các góc trong bước 3
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
    for i in range(1, ro - 1):
        for j in range(1, co - 1):
            if angle2[i, j] == 0:
                BW[i, j] = G[i, j] == max(G[i, j], G[i, j + 1], G[i, j - 1])
            elif angle2[i, j] == 45:
                BW[i, j] = G[i, j] == max(G[i, j], G[i + 1, j - 1], G[i - 1, j + 1])
            elif angle2[i, j] == 90:
                BW[i, j] = G[i, j] == max(G[i, j], G[i + 1, j], G[i - 1, j])
            elif angle2[i, j] == 135:
                BW[i, j] = G[i, j] == max(G[i, j], G[i + 1, j + 1], G[i - 1, j - 1])

    BW = BW * G

    # Bước 6: Giá trị ngưỡng
    T_Low = 0.02 * BW.max()
    T_High = 0.08 * BW.max()
    edge_final = np.zeros([ro, co], dtype='uint8')

    for i in range(ro):
        for j in range(co):
            if BW[i, j] > T_High:
                edge_final[i, j] = 255

    return edge_final

def sobel_algorithm_binary(image_path):
    # Đọc ảnh
    img = cv2.imread(image_path, 0)
    # Tạo kernel Sobel
    hx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], dtype=np.float32)
    hy = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]], dtype=np.float32)
    # Tích chập
    Gx = convolve2d(img, hx, mode='same')
    Gy = convolve2d(img, hy, mode='same')
    # Gradient
    G = np.sqrt(Gx**2 + Gy**2)
    # Chuyển thành 8-bit
    G_scale = np.uint8(G / G.max() * 255)
    # Ảnh nhị phân
    _, binary_img = cv2.threshold(G_scale, 50, 255, cv2.THRESH_BINARY)
    return binary_img

def compare_algorithms(image_path):
    canny_edges = canny_algorithm(image_path)
    sobel_binary = sobel_algorithm_binary(image_path)
    # Lấy hiệu giữa ảnh Canny và Sobel Binary
    difference = cv2.subtract(canny_edges, sobel_binary)

    # Hiển thị kết quả
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(canny_edges, cmap='gray')
    axs[0].set_title('Canny Edges')
    axs[0].axis('off')

    axs[1].imshow(sobel_binary, cmap='gray')
    axs[1].set_title('Sobel Binary')
    axs[1].axis('off')

    axs[2].imshow(difference, cmap='gray')
    axs[2].set_title('Canny - Sobel Difference')
    axs[2].axis('off')

    plt.tight_layout()
    plt.show()

compare_algorithms(image_path)
