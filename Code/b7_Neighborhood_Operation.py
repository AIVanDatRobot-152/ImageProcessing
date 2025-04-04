import numpy as np
v1 = np.array([1/3, 1/3, 1/3], dtype = np.float32)
v2 = np.array([10, 11, 12, 5, 4, 3, 1], dtype = np.float32)
full = np.convolve(v1,v2,mode='full')
valid = np.convolve(v1,v2,mode='valid')
same = np.convolve(v1,v2,mode='same')
print(full)
print(valid)
print(same)