import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("bean.tif", 0)
H, W = image.shape
corrected_img = np.zeros((H, W))

# 강의노트 9페이지의 그래프를 수식적으로 구현
for i in range(H):
    for j in range(W):
        if image[i, j] < 80:
            corrected_img[i, j] = image[i, j] * 0.25
        elif image[i, j] < 140:
            corrected_img[i, j] = image[i, j] * 3.0 - 220
        else:
            corrected_img[i, j] = min(image[i, j] * 0.5 + 130, 255)
            # else 문의 max는 min으로 바꿔야 함
            
fig = plt.figure()
ax0 = fig.add_subplot(211)
ax0.hist(image.ravel(), 256, [0, 256])
ax1 = fig.add_subplot(212)
ax1.hist(corrected_img.ravel(), 256, [0, 256])

plt.show()

cv2.imshow("Original", image)
cv2.imshow("Contrast Enhancement", corrected_img.astype(np.uint8))
cv2.waitKey()
cv2.destroyAllWindows()