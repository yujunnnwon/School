import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("bean.tif", 0)
equ = cv2.equalizeHist(image)           # cv2의 함수를 이용하여 image를 Histogram Equalization

fig = plt.figure()
ax0 = fig.add_subplot(211)
ax0.hist(image.ravel(), 256, [0, 256])
ax1 = fig.add_subplot(212)
ax1.hist(equ.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("Original", image)
cv2.imshow("After Histogram Equalization", equ.astype(np.uint8))
cv2.waitKey()
cv2.destroyAllWindows()