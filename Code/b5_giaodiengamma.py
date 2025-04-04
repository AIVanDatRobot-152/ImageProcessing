import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Hàm áp dụng hiệu chỉnh gamma và cập nhật ảnh
def apply_gamma():
    g = float(gamma_slider.get())
    img_gamma = gray / 255.0
    img_gamma = img_gamma ** g
    img_gamma = np.array(img_gamma * 255, dtype='uint8')
    
    # Hiển thị ảnh đã hiệu chỉnh trên giao diện
    img_pil = Image.fromarray(cv2.cvtColor(img_gamma, cv2.COLOR_BGR2RGB))
    img_tk = ImageTk.PhotoImage(img_pil)
    label_img.config(image=img_tk)
    label_img.image = img_tk
    label_gamma_value.config(text=f"Gamma: {g:.1f}")

# Đọc ảnh gốc
gray = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code\chillguy.jpg', 1)

# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("Gamma Correction Interface")

# Hiển thị ảnh gốc ban đầu
img_pil = Image.fromarray(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))
img_tk = ImageTk.PhotoImage(img_pil)

# Tạo label để hiển thị ảnh
label_img = tk.Label(root, image=img_tk)
label_img.pack(pady=10)

# Slider điều chỉnh gamma
gamma_slider = ttk.Scale(root, from_=0.5, to=10.0, value=0.5, orient="horizontal", command=lambda e: apply_gamma())
gamma_slider.pack(pady=5)

# Hiển thị giá trị gamma hiện tại
label_gamma_value = tk.Label(root, text="Gamma: 1.0")
label_gamma_value.pack()

# Nút thoát
btn_quit = tk.Button(root, text="Thoát", command=root.destroy)
btn_quit.pack(pady=10)

root.mainloop()
