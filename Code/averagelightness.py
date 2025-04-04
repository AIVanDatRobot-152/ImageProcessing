import cv2
import numpy as np
import time

img = cv2.imread('F:/StudyatCLass/Study/class/Xử lí ảnh số/Code/fruit.jpg', 1)


blue = img[ :,:, 0]
green = img[:,:, 1]
red = img[:,:, 2]

ro, co, _ = img.shape

start = time.time()

grayscale = red*(1/3) + green*(1/3) + blue*(1/3)
grayscale = grayscale.astype(np.uint8)

end = time.time()
cal_time = end - start 
print (cal_time , 'giây')
cv2.imshow('Display gray scale 2', grayscale)


cv2.waitKey(0)
cv2.destroyAllWindows()