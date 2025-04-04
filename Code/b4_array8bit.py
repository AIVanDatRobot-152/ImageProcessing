import numpy as np

img = [[3, 6, 6, 8],
       [5, 3, 1, 4],
       [8, 6, 5, 1],
       [4, 8, 2, 3]]

rand_array = np.random.randint(0,3,(2,2))
zeros = np.sum(rand_array == 0)
ones = np.sum(rand_array == 1)
twos = np.sum(rand_array == 2)

img = np.array(img, dtype=np.uint8)

r = np.unique(img)

print("Các giá trị duy nhất trong img:", r)
print("Kích thước của ma trận img:", r.shape)
print(rand_array)
print(zeros)
print(ones)
print(twos)