import numpy as np
import cv2
import matplotlib.pyplot as plt

# Đọc ảnh màu
img = cv2.imread('F:\\StudyatCLass\\Study\\class\\Xulianhso\\Code\\lena.tif')

# Hàm xử lý kéo dãn tương phản cho một kênh màu
def balace_histogram(channel):
    L = 256
    u = np.array(list(range(L)), dtype='uint8')

    # Tính histogram và xác suất
    nu = np.zeros(len(u), dtype=np.float32)
    pu = np.zeros(len(u), dtype=np.float32)

    ro, co = channel.shape
    n = ro * co

    for i in range(len(u)):
        nu[i] = np.sum(channel == u[i])
        pu[i] = nu[i] / n

    # Tính CDF và ánh xạ giá trị
    pre = 0
    cu = np.zeros(len(u), dtype=np.float32)
    v = np.zeros(len(u), dtype=np.float32)

    for i in range(len(pu)):
        cu[i] = pre + pu[i]
        v[i] = cu[i] * (L - 1)
        pre = cu[i]

    v_round = np.round(v).astype(np.uint8)

    # Tạo kênh màu mới sau khi ánh xạ
    stretched_channel = np.zeros_like(channel, dtype='uint8')
    for i in range(ro):
        for j in range(co):
            stretched_channel[i, j] = v_round[channel[i, j]]

    return stretched_channel

# Áp dụng kéo dãn tương phản cho từng kênh màu
blue_stretched = balace_histogram(img[:, :, 0])
green_stretched = balace_histogram(img[:, :, 1])
red_stretched = balace_histogram(img[:, :, 2])

# Gộp lại thành ảnh màu mới
new_img = cv2.merge([blue_stretched, green_stretched, red_stretched])

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', img)
cv2.imshow('Contrast Stretched Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Vẽ histogram của ảnh gốc và ảnh đã xử lý
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Histogram of Original Image')
colors = ('blue', 'green', 'red')
for i, color in enumerate(colors):
    plt.hist(img[:, :, i].ravel(), 256, [0, 256], color=color, alpha=0.6, label=f'{color} channel')
plt.legend()

plt.subplot(1, 2, 2)
plt.title('Histogram of Contrast Stretched Image')
for i, color in enumerate(colors):
    plt.hist(new_img[:, :, i].ravel(), 256, [0, 256], color=color, alpha=0.6, label=f'{color} channel')
plt.legend()

plt.tight_layout()
plt.show()

# print("Ảnh gốc:")
# print(img)
# print("Ảnh sau khi kéo dãn tương phản:")
# print(new_img)
