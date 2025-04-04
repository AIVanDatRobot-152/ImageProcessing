import cv2
import numpy as np
import time

RGB = cv2.imread('fruit.jpg', 1)


blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]


ro, co, _ =RGB.shape

# r=g=b =np.zeros([ro,co,ch],dtype = np.uint8)

maxband= np.zeros([ro,co ],dtype = np.uint8)
minband= np.zeros([ro,co ],dtype = np.uint8)
start = time.time()
maxband [:,:] = np.maximum (red,green,blue)
minband [:,:] = np.minimum (red,green,blue)
grayscale1 = maxband*0.5 + minband*0.5
grayscale1 = grayscale1.astype(np.uint8)
end = time.time()
cal_time = end - start 
print (cal_time , 'giây')
cv2.imshow('Display gray scale 1', grayscale1)


cv2.waitKey(0)
cv2.destroyAllWindows()
