import numpy as np
from scipy.signal import convolve2d 
import math

hx = np.array([[-1, 0, 1],
               [-2,  0,  2],
               [-1,  0,  1]], dtype=np.float32)
hy = np.array([[-1, -2, -1],
               [0,  0,  0],
               [1,  2,  1]], dtype=np.float32)
I = np.array([[100,  100,  200,  200],
               [100,  100,  200,  200],
               [100,  100,  200,  200],
               [100,  100,  200,  200]], dtype=np.float32)


gx = convolve2d(I,hx,mode='same')
gy = convolve2d(I,hy,mode='same')
g = np.sqrt((gx**2)+(gy**2))
theta = np.arctan(np.divide(gx,gy))
print(gx)
print(gy)
print(g)
print(theta)