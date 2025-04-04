import cv2
from scipy.signal import convolve2d
import numpy as np

img = cv2.imread('F:/StudyatCLass/Study/class/Xulianhso/Code/ultra1.jpg', 0)

h = 1/9 * np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32)

img_out = convolve2d(img, h, mode='same')
img_out = np.round(img_out)
img_out = np.array(img_out, dtype=np.uint8)

cv2.imshow('old img', img)
cv2.imshow('Highpass Filtering', img_out)

cv2.waitKey(0)
cv2.destroyAllWindows()