import numpy as np
import matplotlib.pyplot as plt 
img = [[0, 1, 1],
       [2, 0, 1],
       [0, 1, 1]]

img = np.array(img, dtype=np.uint8)

r = np.unique(img)

nr = np.zeros(len(r), dtype=np.uint8)
pr = np.zeros(len(r), dtype=np.uint8) #1*7: 1 hàng 7 cột
for i in range(len(r)):
    pr[i] = np.sum(img == r[i])

fig = plt.figure(figsize = (10,7))
plt.bar(r,pr/9, color ='black')
plt.xlabel("r")
plt.ylabel("p(r)")
plt.title("bảng histogram cách 2")
fractions = [f"{int(v)}/{img.size}" for v in pr]
plt.gca().set_yticks(pr / img.size)
plt.gca().set_yticklabels(fractions)
plt.show()

print("Các giá trị duy nhất trong img:", r)
print("Kích thước của ma trận img:", r.shape)
