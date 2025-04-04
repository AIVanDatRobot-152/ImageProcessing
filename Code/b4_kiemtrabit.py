import numpy as np

# Tạo mảng NumPy từ danh sách
img = np.array([[3, 6, 6, 8],
                [5, 3, 1, 4],
                [8, 6, 5, 1],
                [4, 8, 2, 3]], dtype=np.uint8)

# Số byte mỗi phần tử trong mảng chiếm
bytes_per_element = img.itemsize
# Chuyển đổi sang bit
bits_per_element = bytes_per_element * 8
# Tổng số bit của mảng
total_bits = img.size * bits_per_element

print("Kiểu dữ liệu của mảng:", img.dtype)
print("Số bit mỗi phần tử:", bits_per_element)
print("Tổng số bit của mảng:", total_bits)
