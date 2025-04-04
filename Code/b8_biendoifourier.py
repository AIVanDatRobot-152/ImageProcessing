from numpy.fft import fft, ifft
import numpy as np 
import cv2

g1 = np.array([1,1,2,1], dtype= np.complex_)
g2 = np.array([1,2,3,4], dtype= np.complex_)

G1 = fft(g1)
# G11 = cv2.dft(g1, flags = cv2.DFT_COMPLEX_OUTPUT)
G2 = fft(g2)
# G22 = cv2.dft(g2, flags = cv2.DFT_COMPLEX_OUTPUT)
G = G1*G2

g = ifft(G)

print('biến đổi mảng sang số phức g1',g1)
print('biến đổi mảng sang số phức g2',g2)
print('biến đổi fourier rời rạc của g1',G1)
print('biến đổi fourier rời rạc của g1',G2)
# print(G11)
# print(G22)
print('tich chap vong tron cua g1 va g2',G)
print('biến đổi fourier rời rạc ngược của G',g)