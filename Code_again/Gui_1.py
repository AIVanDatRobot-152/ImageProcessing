import numpy as np
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

# Sobel Operator
def compute_sobel(image):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    gx = cv2.filter2D(image, -1, sobel_x)
    gy = cv2.filter2D(image, -1, sobel_y)
    gradient_magnitude = np.sqrt(gx.astype(float) ** 2 + gy.astype(float) ** 2)
    gradient_magnitude = (gradient_magnitude / gradient_magnitude.max() * 255).astype(np.uint8)
    _, binary_image = cv2.threshold(gradient_magnitude, 50, 255, cv2.THRESH_BINARY)
    return gx, gy, gradient_magnitude, binary_image

# Prewitt Operator
def compute_prewitt(image):
    prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    gx = cv2.filter2D(image, -1, prewitt_x)
    gy = cv2.filter2D(image, -1, prewitt_y)
    gradient_magnitude = np.sqrt(gx.astype(float) ** 2 + gy.astype(float) ** 2)
    gradient_magnitude = (gradient_magnitude / gradient_magnitude.max() * 255).astype(np.uint8)
    _, binary_image = cv2.threshold(gradient_magnitude, 50, 255, cv2.THRESH_BINARY)
    return gx, gy, gradient_magnitude, binary_image

# Canny Edge Detection
def compute_canny(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)
    edges = cv2.Canny(blurred_image, 50, 150)
    return edges

# Resize Image
def resize_image(image, target_size=(500, 600)):
    h, w = image.shape
    scale = min(target_size[0] / h, target_size[1] / w)
    new_h, new_w = int(h * scale), int(w * scale)
    return cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

# Load Image
def load_image():
    global original_image, gx, gy, gradient_image, binary_image, edges, method

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tif")])
    if not file_path:
        return

    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    resized_image = resize_image(image)

    if method.get() == "Sobel":
        gx, gy, gradient_image, binary_image = compute_sobel(resized_image)
    elif method.get() == "Prewitt":
        gx, gy, gradient_image, binary_image = compute_prewitt(resized_image)
    elif method.get() == "Canny":
        edges = compute_canny(resized_image)
        gx, gy, gradient_image, binary_image = None, None, edges, edges

    original_image = resized_image
    show_image(original_image)

# Display Image
def show_image(image):
    image = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(image=image)
    display_label.config(image=img_tk)
    display_label.image = img_tk

# Main GUI
root = tk.Tk()
root.title("Edge Detection (Sobel, Prewitt, Canny)")
root.geometry("800x650")

# Options Frame
button_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
button_frame.pack(side=tk.LEFT, fill=tk.Y)

method = tk.StringVar(value="Sobel")
method_menu = ttk.Combobox(button_frame, textvariable=method, values=["Sobel", "Prewitt", "Canny"], state="readonly")
method_menu.pack(pady=10)

tk.Button(button_frame, text="Load Image", command=load_image, width=20).pack(pady=10)
tk.Button(button_frame, text="Original Image", command=lambda: show_image(original_image), width=20).pack(pady=10)
tk.Button(button_frame, text="Gx", command=lambda: show_image(np.uint8(np.abs(gx))) if gx is not None else None, width=20).pack(pady=10)
tk.Button(button_frame, text="Gy", command=lambda: show_image(np.uint8(np.abs(gy))) if gy is not None else None, width=20).pack(pady=10)
tk.Button(button_frame, text="Gradient Magnitude", command=lambda: show_image(gradient_image), width=20).pack(pady=10)
tk.Button(button_frame, text="Binary Image", command=lambda: show_image(binary_image), width=20).pack(pady=10)

image_frame = tk.Frame(root, bg="white", padx=10, pady=10)
image_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

display_label = tk.Label(image_frame, bg="white")
display_label.pack(expand=True)

root.mainloop()
