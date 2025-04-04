import cv2
import numpy as np
RGB = cv2.imread("F:\StudyatCLass\Study\class\Xulianhso\Code_again\peppers.png",1)
blue = RGB[:,:,0]
green = RGB[:,:,1]
red = RGB[:,:,2]

# cv2.imshow("RGB blue", blue)
# cv2.imshow('RGB green', green)
# cv2.imshow('RGB red',red)

ro,co,ch = RGB.shape 

r = g = b = np.zeros([ro,co,ch], dtype = np.uint8)

temp = np.zeros([ro,co], dtype = np.uint8)

r[:,:,0], r[:,:,1], r[:,:,2] = temp, temp, red
cv2.imshow('RGB red',r) 
r[:,:,0], r[:,:,1], r[:,:,2] = temp, green, temp 
cv2.imshow('RGB green', g)
r[:,:,0], r[:,:,1], r[:,:,2] = blue, temp, temp
cv2.imshow("RGB blue", b) 

cv2.waitKey(0)
cv2.destroyAllWindows