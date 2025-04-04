import numpy as np
import matplotlib.pyplot as plt 

# Ma trận ảnh đầu vào
img = np.array([[249, 108, 110, 138],
                [10, 98, 108, 114],
                [85, 100, 96, 104],
                [85, 87, 95, 98]], dtype=np.uint8)

# Lấy số dòng và số cột
ro, co = img.shape

# Tạo ảnh mới với kích thước tương tự, kiểu dữ liệu uint8
new_img = np.zeros([ro, co], dtype=np.uint8)

# Tìm giá trị min và max trong ảnh
i = np.unique(img)
L = i[1]  # Giá trị nhỏ nhất (không phải giá trị 0)
M = i[-2]  # Giá trị lớn nhất (không phải giá trị 255)
Imax = 255  # Giá trị sáng tối đa
Imin = 0    # Giá trị sáng tối thiểu

# Tính toán hệ số ánh xạ
factor = (Imax - Imin) / (M - L)

# Áp dụng ánh xạ cho từng pixel
for i in range(ro):
    for j in range(co):
        if img[i, j] < L:
            new_img[i, j] = Imin
        elif img[i, j] > M:
            new_img[i, j] = Imax
        else:
            new_img[i, j] = np.round(factor * (img[i, j] - L)).astype(np.uint8)

# Hiển thị ảnh gốc và ảnh sau khi ánh xạ
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Ảnh Gốc")
plt.subplot(1, 2, 2)
plt.imshow(new_img, cmap='gray')
plt.title("Ảnh Sau Ánh Xạ")
plt.show()
