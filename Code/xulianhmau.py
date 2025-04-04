import cv2
import numpy as np

# Đọc ảnh với đường dẫn hợp lệ
RGB = cv2.imread(r'F:\StudyatCLass\Study\class\Xử lí ảnh số\Code\lena.tif', 1)

# Kiểm tra xem ảnh đã được đọc đúng chưa
if RGB is None:
    print("Lỗi: Không thể đọc được ảnh. Kiểm tra lại đường dẫn và file ảnh.")
    exit()  # Dừng chương trình nếu không thể đọc ảnh

# Tách các kênh màu
blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]

# Tạo ảnh màu từ các kênh riêng lẻ
blue_image = cv2.merge([blue, np.zeros_like(blue), np.zeros_like(blue)])
green_image = cv2.merge([np.zeros_like(green), green, np.zeros_like(green)])
red_image = cv2.merge([np.zeros_like(red), np.zeros_like(red), red])

# Hiển thị hình ảnh
cv2.imshow('Display red image', red_image)
cv2.imshow('Display green image', green_image)
cv2.imshow('Display blue image', blue_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
