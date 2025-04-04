import numpy as np

img = np.array([[13, 14, 2, 14],
                [10, 2, 5, 9],
                [15, 15, 3, 15],
                [15, 8, 13, 1]], dtype=np.uint8)

L=16
u=np.array(list(range(L)), dtype= 'uint8')

nu= np.zeros(len(u),dtype=np.float32)
pu= np.zeros(len(u),dtype=np.float32)

ro,co = img.shape
n= ro*co

for i in range(len(u)):
    nu[i] = np.sum(img == u[i])
    pu[i] = nu[i]/n

pre = 0
cu= np.zeros(len(u),dtype=np.float32)
v = np.zeros(len(u),dtype=np.float32)

for i in range(len(pu)):
    cu[i] = pre + pu[i]
    v[i] = cu[i]*(L-1)
    pre = cu[i]

v_round = np.round(v)
v_round = np.array (v_round, dtype='uint8')

new_img = np.zeros([ro,co], dtype='uint8')

for i in range(ro):
    for j in range(co):
            new_img[i, j] = v_round[img[i,j]]

print(new_img)
print('u:',u)
print('nu:',nu)
print('pu:',pu)
print('cu:',cu)
# print('v:',v)