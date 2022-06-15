import cv2
import numpy as np

def three_thresholding(value):
    if value < 64:
        return 64
    elif value < 128:
        return 128
    elif value < 192:
        return 192
    else:
        return 255

image = cv2.imread("input.jpg", 0)

H, W = image.shape
result = np.zeros((width, height))

for i in range(H):
    for j in range(W):
        temp = image[i, j]
        return_value = three_thresholding(temp)
        result[i, j] = return_value

cv2.imshow("Original", image)
cv2.imshow("Result", result.astype(np.uint8))
cv2.waitKey()
cv2.destroyAllWindows()
