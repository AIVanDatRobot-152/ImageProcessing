import matplotlib.pyplot as plt
import numpy as np
import cv2

# Tạo subplot 1x2
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Đọc ảnh
img = cv2.imread(r'F:\StudyatCLass\Study\class\Xulianhso\Code\speckle_noise_6.png', cv2.IMREAD_GRAYSCALE)
axs[0].imshow(img, cmap='gray')  # Hiển thị ảnh gốc
axs[0].set_xticks(())
axs[0].set_yticks(())
axs[0].set_title('Hình ảnh gốc')

# Biến đổi Fourier
fourier = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
fourier_shift = np.fft.fftshift(fourier)
mag = cv2.magnitude(fourier_shift[:, :, 0], fourier_shift[:, :, 1])

# Lấy log và chuẩn hóa
mag = np.log(mag + 1)
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

# Hiển thị độ lớn của biến đổi Fourier
axs[1].imshow(mag, cmap='gray')
axs[1].set_xlabel('u')
axs[1].set_ylabel('v')
axs[1].set_xticks(())
axs[1].set_yticks(())
axs[1].set_title('Độ lớn của biến đổi Fourier')

# Hiển thị đồ thị
plt.tight_layout()
plt.show()
