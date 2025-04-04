import cv2
import numpy as np
import time

# Đọc ảnh màu
gray = cv2.imread('F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif', 1)

# Tách các kênh màu
gamma = [0.5,1,1.5,2,2.5,3]

for g in gamma:
    img_gamma = gray/255
    img_gamma = img_gamma**g
    img_gamma = np.array(img_gamma*255, dtype = 'uint8')
    cv2.imshow('Display gamma correction-'+ str(g),img_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()
