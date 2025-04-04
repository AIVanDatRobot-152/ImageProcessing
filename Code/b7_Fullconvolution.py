import numpy as np
from scipy.signal import convolve2d 

v1 = np.array([[-1, -2, -1],
               [0,  0,  0],
               [1,  2,  1]], dtype=np.float32)

v2 = np.array([[1,  -1,  3,  2],
               [2,   1,  2,  4],
               [1,  -1,  2, -2],
               [3,   1,  2,  2]], dtype=np.float32)


full = convolve2d(v2,v1,mode='full')
valid = convolve2d(v2,v1,mode='valid')
same = convolve2d(v2,v1,mode='same')
print(full)
print(valid)
print(same)


