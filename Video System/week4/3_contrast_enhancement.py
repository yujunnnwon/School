"""
<Contrast Enhancement>
영상의 픽셀 값들의 범위가 작은 경우, contrast가 낮다고 한다.
contrast가 낮으면, 물체 간의 구별이 어렵다.
이를 개선하기 위한 것이 Contrast Enhancement
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("bean.tif", 0)

H, W = image.shape
corrected_img = np.zeros((H, W))

for i in range(H):
    for j in range(W):
        if image[i, j] < 80:
            corrected_img[i, j] = image[i, j] * 0.25
        elif image[i, j] < 140:
            corrected_img[i, j] = image[i, j] * 3.0 - 220
        else:
            corrected_img[i, j] = min(image[i, j] * 0.5 + 130, 255)
            
fig = plt.figure()
ax0 = fig.add_subplot(3, 1, 1)
ax0.set_title("Before")
ax0.hist(image.ravel(), 256, [0, 256])
ax1 = fig.add_subplot(3, 1, 3)
ax1.set_title("After")
ax1.hist(corrected_img.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("Original", image)
cv2.imshow("Contrast Enhancement", corrected_img.astype(np.uint8))
cv2.waitKey()
cv2.destroyAllWindows()