import cv2
import numpy as np
import matplotlib.pyplot as plt

original_img = cv2.imread("bean.tif", 0)

hist, bins = np.histogram(original_img.ravel(), 256, [0, 256])
H, W = original_img.shape
"""
Numpy의 histogram 메소드를 이용하여 original_img를 1차원으로 만든 후, 8bit 히스토그램으로 변환.
hist: original_img의 히스토그램을 저장한 변수
bins: 히스토그램의 범위에 해당되는 값을 저장한 변수
"""
cdf = np.cumsum(hist)                   # Numpy의 cumsum()을 이용하여 histogram의 CDF 구함
cdf = (cdf - cdf.min()) * 255 / ((H * W) - cdf.min())
cdf = cdf.astype(np.uint8)              # Numpy array를 uint8의 영상으로 변환
"""
H*W 영상을 equalization -> Histogram의 CDF가 8bit인 영상으로 변환
Histogram Equalization 공식 이용
h(v) = round((cdf(v)-cdf.min) * (L-1) / (M*N) - cdf.min)
출처: https://en.wikipedia.org/wiki/Histogram_equalization
"""
equalized_img = cdf[original_img]       # Histogram Equalization 된 영상을 반환

fig = plt.figure()
ax0 = fig.add_subplot(311)
ax0.set_title("Original")
ax0.hist(original_img.ravel(), 256, [0, 256])
ax1 = fig.add_subplot(313)
ax1.set_title("Equalized Histogram")
ax1.hist(equalized_img.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

cv2.imshow("Original Image", original_img)
cv2.imshow("Equalized Image", equalized_img)
cv2.waitKey()
cv2.destroyAllWindows()