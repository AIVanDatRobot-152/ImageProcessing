import cv2
import numpy as np


RGB = cv2.imread('fruit.jpg', 1)


blue = RGB[:, :, 0]
green = RGB[:, :, 1]
red = RGB[:, :, 2]


ro, co, ch =RGB.shape

r=g=b =np.zeros([ro,co,ch],dtype = np.uint8)

temp= np.zeros([ro,co ],dtype = np.uint8)
r[:,:,0], r[:,:,1], r[:,:,2] = blue, temp, red
cv2.imshow('Display red image', r)
g[:,:,0], g[:,:,1], g[:,:,2] = temp, green, red
cv2.imshow('Display green image', g)
b[:,:,0], b[:,:,1], b[:,:,2] = blue, green, temp
cv2.imshow('Display blue image', b)

cv2.waitKey(0)
cv2.destroyAllWindows()
