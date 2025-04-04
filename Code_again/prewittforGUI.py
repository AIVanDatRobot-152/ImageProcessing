import numpy as np
import cv2
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Bộ lọc Prewitt
hx = np.array([[-1, 0, 1],
               [-1, 0, 1],
               [-1, 0, 1]], dtype=np.float32)
hy = np.array([[-1, -1, -1],
               [0, 0, 0],
               [1, 1, 1]], dtype=np.float32)

# Đọc ảnh đầu vào
image = cv2.imread("F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif", 0)

# Áp dụng bộ lọc Prewitt
gx = convolve2d(image, hx, mode='same')
gy = convolve2d(image, hy, mode='same')

# Tính toán gradient
g = np.sqrt((gx**2) + (gy**2))

# Chuyển đổi ảnh về 8-bit
G8 = np.uint8(g / g.max() * 255)

# Áp dụng ngưỡng
threshold_value = 10
_, binary_image = cv2.threshold(G8, threshold_value, 255, cv2.THRESH_BINARY)

# Hiển thị ảnh nhị phân
cv2.imshow("Thresholded Image", binary_image)

# Vẽ histogram của ảnh nhị phân
plt.figure("Histogram")
plt.hist(image.ravel(), bins=256, range=[0, 256], color='blue', alpha=0.7)
plt.title("Histogram of Binary Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.grid(True)

# Hiển thị biểu đồ và đợi người dùng đóng cửa sổ
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
