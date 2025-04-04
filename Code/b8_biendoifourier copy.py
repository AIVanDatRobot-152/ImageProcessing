import numpy as np

g1 = np.array([1, 1, 2, 1], dtype=np.complex_)
N = len(g1)  # Độ dài tín hiệu
G = np.zeros(N, dtype=complex)  # Mảng lưu kết quả

# Tính DFT sử dụng hai vòng for
for k in range(N):  # Duyệt qua tất cả các tần số k
    for n in range(N):  # Duyệt qua tất cả các giá trị thời gian n
        G[k] += g1[n] * np.exp(-2j * np.pi * k * n / N)  # Áp dụng công thức DFT

# In kết quả
print("Biến đổi Fourier rời rạc (thủ công):", G)
