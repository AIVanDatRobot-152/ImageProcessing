import numpy as np
import cv2
from scipy.signal import convolve2d

# Kernel Sobel
hx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]], dtype=np.float32)
hy = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]], dtype=np.float32)

# Đọc ảnh xám
image = cv2.imread(r"F:\StudyatCLass\Study\class\Xulianhso\Code_again\lena.tif", 0)

# Tính toán đạo hàm Sobel theo trục X và Y
gx = convolve2d(image, hx, mode='same')
gy = convolve2d(image, hy, mode='same')

# Tính toán độ lớn gradient
g = np.sqrt((gx**2) + (gy**2))

# Chuẩn hóa độ lớn gradient về khoảng giá trị 0-255
G8 = np.uint8(g / g.max() * 255)

# Ngưỡng để tạo ảnh nhị phân
threshold_value = 10  # Điều chỉnh giá trị ngưỡng theo yêu cầu
_, binary_image = cv2.threshold(G8, threshold_value, 255, cv2.THRESH_BINARY)

# Hiển thị ảnh
cv2.imshow("Original Image", image)
cv2.imshow("Sobel Edge Detection", G8)
cv2.imshow("Binary Edge Detection", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
