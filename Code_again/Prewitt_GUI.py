import numpy as np
import cv2
from scipy.signal import convolve2d
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Hàm tính toán Prewitt
def compute_prewitt(image):
    hx = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]], dtype=np.float32)
    hy = np.array([[-1, -1, -1],
                   [0, 0, 0],
                   [1, 1, 1]], dtype=np.float32)

    gx = convolve2d(image, hx, mode='same')
    gy = convolve2d(image, hy, mode='same')
    g = np.sqrt(gx**2 + gy**2)
    g8 = np.uint8(g / g.max() * 255)

    threshold_value = 10
    _, binary_image = cv2.threshold(g8, threshold_value, 255, cv2.THRESH_BINARY)
    return gx, gy, g8, binary_image

# Hàm thu nhỏ ảnh về kích thước 500x600
def resize_image(image, target_size=(500, 600)):
    h, w = image.shape
    scale_h = target_size[0] / h
    scale_w = target_size[1] / w
    scale = min(scale_h, scale_w)
    new_h, new_w = int(h * scale), int(w * scale)
    resized_image = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    return resized_image

# Hàm tải ảnh từ máy tính
def load_image():
    global original_image, gx, gy, gradient_image, binary_image

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tif")])
    if not file_path:
        return

    # Đọc và chuyển đổi ảnh về grayscale
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized_image = resize_image(image)

    # Tính toán các chế độ ảnh
    gx, gy, gradient_image, binary_image = compute_prewitt(resized_image)
    original_image = resized_image

    # Hiển thị ảnh gốc
    show_image(original_image)

# Hàm hiển thị ảnh
def show_image(image):
    image = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(image=image)
    display_label.config(image=img_tk)
    display_label.image = img_tk

# Giao diện chính
root = tk.Tk()
root.title("Prewitt Edge Detection")
root.geometry("800x650")  # Kích thước khung chính

# Khung chứa các nút
button_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

# Thêm các nút
load_button = tk.Button(button_frame, text="Load Image", command=load_image, width=20)
load_button.pack(pady=10)

original_button = tk.Button(button_frame, text="Original Image", command=lambda: show_image(original_image), width=20)
original_button.pack(pady=10)

gx_button = tk.Button(button_frame, text="Gx", command=lambda: show_image(np.uint8(np.abs(gx))), width=20)
gx_button.pack(pady=10)

gy_button = tk.Button(button_frame, text="Gy", command=lambda: show_image(np.uint8(np.abs(gy))), width=20)
gy_button.pack(pady=10)

gradient_button = tk.Button(button_frame, text="Gradient Magnitude", command=lambda: show_image(gradient_image), width=20)
gradient_button.pack(pady=10)

binary_button = tk.Button(button_frame, text="Binary Image", command=lambda: show_image(binary_image), width=20)
binary_button.pack(pady=10)

# Khung hiển thị ảnh
image_frame = tk.Frame(root, bg="white", padx=10, pady=10)
image_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

display_label = tk.Label(image_frame, bg="white")
display_label.pack(expand=True)

# Chạy giao diện
root.mainloop()
