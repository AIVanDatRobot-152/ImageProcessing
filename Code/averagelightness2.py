import cv2
import numpy as np
import time

RGB = cv2.imread('fruittt.jpg', 1)


blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]

ro, co, _ = RGB.shape

start = time.time()
grayscale = np.zeros([ro,co ],dtype = np.uint8)
for r in range (ro): 
    for c in range (co):
        averagegrayscale = int(red[r,c]*(1/3) + green[r,c]*(1/3) + blue[r,c]*(1/3))
        grayscale[r,c] = averagegrayscale

end = time.time()
cal_time = end - start 
print (cal_time , 'giây')
cv2.imshow('Display gray scale 2', grayscale)


cv2.waitKey(0)
cv2.destroyAllWindows()