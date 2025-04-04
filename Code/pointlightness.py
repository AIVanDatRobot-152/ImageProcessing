import cv2
import numpy as np
import time

RGB = cv2.imread('fruit.jpg', 1)


blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]

ro, co, _ = RGB.shape


maxband1= np.zeros([ro,co ],dtype = np.uint8)
minband1= np.zeros([ro,co ],dtype = np.uint8)
grayscale2 = np.zeros([ro,co ],dtype = np.uint8)
start = time.time()
for r in range (ro): 
    for c in range (co):
        maxgray = np.max(np.array([red[r,c], green[r,c], blue[r,c]]))
        maxband1[r,c] = maxgray
        mingray = np.min(np.array([red[r,c], green[r,c], blue[r,c]]))
        minband1[r,c] = mingray
        gray = int ( maxgray*0.5 + mingray*0.5)
        grayscale2[r,c] = gray  
end = time.time()
cal_time = end - start 
print (cal_time , 'giây')
cv2.imshow('Display gray scale 2', grayscale2)


cv2.waitKey(0)
cv2.destroyAllWindows()
