import numpy as np
import cv2
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

hx = np.array([[-1, 0, 1],
               [-1, 0, 1],
               [-1, 0, 1]], dtype=np.float32)
hy = np.array([[-1, -1, -1],
               [0, 0, 0],
               [1, 1, 1]], dtype=np.float32)

image = cv2.imread("F:\StudyatCLass\Study\class\Xulianhso\Code\lena.tif",0)

gx = convolve2d(image, hx, mode='same')
gy = convolve2d(image, hy, mode='same')

g = np.sqrt((gx**2) + (gy**2))

G8 = np.uint8(g/ g.max()*255 )

threshold_value = 10
_, binary_image = cv2.threshold(G8, threshold_value, 255, cv2.THRESH_BINARY)


# cv2.imshow('Gradient X (gx)', np.uint8((gx / gx.max()) * 127 + 127))
# cv2.imshow('Gradient Y (gy)', np.uint8((gy / gy.max()) * 127 + 127))
# cv2.imshow('G', G8)
# cv2.imshow('Binary', binary_image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

fig, axs = plt.subplots(1,5)
axs[0].imshow(image, cmap = 'gray')
axs[0].set_xticks(())
axs[0].set_yticks(())
axs[0].set_title('Original IMG')
axs[1].imshow(gx, cmap = 'gray')
axs[1].set_xticks(())
axs[1].set_yticks(())
axs[1].set_title('Gx')
axs[2].imshow(gy, cmap ='gray')
axs[2].set_xticks(())
axs[2].set_yticks(())
axs[2].set_title('Gy')
axs[3].imshow(G8, cmap = 'gray')
axs[3].set_xticks(())
axs[3].set_yticks(())
axs[3].set_title('G')
axs[4].imshow(binary_image, cmap = 'gray')
axs[4].set_xticks(())
axs[4].set_yticks(())
axs[4].set_title('Binary IMG')
plt.show()