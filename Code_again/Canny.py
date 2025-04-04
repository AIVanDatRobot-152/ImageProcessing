import numpy as np
import cv2
from matplotlib import pyplot as plt

# 1. Đọc ảnh và chuyển sang grayscale
image_path = "F:\StudyatCLass\Study\class\Xulianhso\Code_again\doggo.jpg"  # Thay bằng đường dẫn đến ảnh của bạn
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Không thể tải ảnh. Vui lòng kiểm tra đường dẫn.")
    exit()

# 2. Làm mượt ảnh bằng Gaussian filter
def gaussian_filter(image, kernel_size=5, sigma=1.4):
    ax = np.arange(-kernel_size // 2 + 1., kernel_size // 2 + 1.)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2. * sigma**2))
    kernel = kernel / np.sum(kernel)
    return cv2.filter2D(image, -1, kernel)

smoothed_image = gaussian_filter(image)

# 3. Tính gradient cường độ và hướng cạnh
def sobel_filter(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    gradient_x = cv2.filter2D(image, -1, sobel_x)
    gradient_y = cv2.filter2D(image, -1, sobel_y)
    
    magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
    direction = np.arctan2(gradient_y, gradient_x) * 180. / np.pi
    direction = (direction + 180) % 180  # Normalize to [0, 180]
    return magnitude, direction

magnitude, direction = sobel_filter(smoothed_image)

# 4. Non-Maximum Suppression
def non_maximum_suppression(magnitude, direction):
    rows, cols = magnitude.shape
    nms = np.zeros((rows, cols), dtype=np.float32)
    direction = direction / 45.  # Quantize to 0, 1, 2, 3
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            q, r = 255, 255
            
            if (0 <= direction[i, j] < 1) or (3 <= direction[i, j] < 4):
                q = magnitude[i, j + 1]
                r = magnitude[i, j - 1]
            elif (1 <= direction[i, j] < 2):
                q = magnitude[i - 1, j + 1]
                r = magnitude[i + 1, j - 1]
            elif (2 <= direction[i, j] < 3):
                q = magnitude[i - 1, j]
                r = magnitude[i + 1, j]
            
            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                nms[i, j] = magnitude[i, j]
    return nms

nms = non_maximum_suppression(magnitude, direction)

# 5. Double Threshold
def double_threshold(image, low_threshold, high_threshold):
    strong = 255
    weak = 50
    
    strong_edges = (image >= high_threshold).astype(np.uint8)
    weak_edges = ((image >= low_threshold) & (image < high_threshold)).astype(np.uint8)
    
    result = strong * strong_edges + weak * weak_edges
    return result, strong, weak

low_threshold = 50
high_threshold = 150
thresholded_image, strong, weak = double_threshold(nms, low_threshold, high_threshold)

# 6. Edge Tracking by Hysteresis
def edge_tracking(image, strong, weak):
    rows, cols = image.shape
    result = np.copy(image)
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if result[i, j] == weak:
                if ((result[i + 1, j - 1:j + 2] == strong).any() or
                    (result[i - 1, j - 1:j + 2] == strong).any() or
                    (result[i, [j - 1, j + 1]] == strong).any()):
                    result[i, j] = strong
                else:
                    result[i, j] = 0
    return result

final_edges = edge_tracking(thresholded_image, strong, weak)

# Hiển thị kết quả
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title("Ảnh gốc")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Edges sau NMS")
plt.imshow(nms, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Final Edges")
plt.imshow(final_edges, cmap="gray")
plt.axis("off")

plt.show()
