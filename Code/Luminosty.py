import cv2
import numpy as np
import time

RGB = cv2.imread('fruit.jpg', 1)


blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]

ro, co, _ = RGB.shape

start = time.time()
grayscale1 = np.zeros([ro,co ],dtype = np.uint8)
grayscale2 = np.zeros([ro,co ],dtype = np.uint8)
for r in range (ro): 
    for c in range (co):
        averagegrayscale1 = int(red[r,c]*(1/3) + green[r,c]*(1/3) + blue[r,c]*(1/3)) #Average
        grayscale1[r,c] = averagegrayscale1
        averagegrayscale2 = int(red[r,c]*(0.299) + green[r,c]*(0.587) + blue[r,c]*(0.114)) #Luminosty
        grayscale2[r,c] = averagegrayscale2

end = time.time()
cal_time = end - start 
print (cal_time , 'giây')
cv2.imshow('Display gray scale 1', grayscale1)
cv2.imshow('Display gray scale 2', grayscale2)


cv2.waitKey(0)
cv2.destroyAllWindows()