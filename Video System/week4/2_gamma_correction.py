"""
<Gamma Correction>
영상 밝기를 point-wise trasform을 통해 조절하는 기법
히스토그램이 편향되었을 때 유용하고, 히스토그램이 고르게 분포한다면 악영향
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("cat.jpg", 0)

H, W = image.shape
result = np.zeros((H, W))

normalized_img = image / 255        # Normalization
c_param = 2                         # 영상의 contrast 조절 인자
                                    # c_param > 1: darkening
for i in range(H):
    for j in range(W):
        result[i, j] = normalized_img[i, j] ** c_param

corrected_img = (result * 255).astype(np.uint8)

fig = plt.figure()
ax0 = fig.add_subplot(3, 1, 1)
ax0.set_title("Before")
ax0.hist(image.ravel(), 256, [0, 256])
ax1 = fig.add_subplot(3, 1, 3)
ax1.set_title("After")
ax1.hist(corrected_img.ravel(), 256, [0, 256])
plt.show()

cv2.imshow("Original", image)
cv2.imshow("Corrected Image", corrected_img)
cv2.waitKey()
cv2.destroyAllWindows()