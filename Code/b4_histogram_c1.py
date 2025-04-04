import numpy as np
import matplotlib.pyplot as plt 
img = [[3, 6, 6, 8],
       [5, 3, 1, 4],
       [8, 6, 5, 1],
       [4, 8, 2, 3]]

img = np.array(img, dtype=np.uint8)

r = np.unique(img)

nr = np.zeros(len(r), dtype=np.uint8) #1*7: 1 hàng 7 cột
for i in range(len(r)):
    nr[i] = np.sum(img == r[i])

fig = plt.figure(figsize = (10,7))
plt.bar(r,nr)
plt.xlabel("r")
plt.ylabel("nr")
plt.title("bảng histogram cách 1")
plt.show()

print("Các giá trị duy nhất trong img:", r)
print("Kích thước của ma trận img:", r.shape)
