import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./cat.jpeg", 0)
H, W = image.shape

normalized_img = image / 255                # 8bit image를 Normalization
c_param = 2
"""
c_param은 영상의 contrast를 어떻게 조절할지 결정하는 인자.
1을 기준으로 하여, 이보다 크면 영상은 어두워지고, 이보다 작으면 영상은 밝아짐.
"""
corrected_img = np.zeros((H, W))

for i in range(H):
    for j in range(W):
        corrected_img[i, j] = normalized_img[i, j] ** c_param

corrected_img = (corrected_img * 255).astype(np.uint8)
# 다시 255를 곱해 영상을 원래 높이로 복구시킴

plt.hist(image.ravel(), 256, [0, 256])
plt.hist(corrected_img.ravel(), 256, [0, 256])
# plt.show()
cv2.imshow("Original", image)
cv2.imshow("Corrected Image", corrected_img)
cv2.waitKey()
cv2.destroyAllWindows()