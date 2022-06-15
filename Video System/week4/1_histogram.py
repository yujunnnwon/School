import cv2
import matplotlib.pyplot as plt

image = cv2.imread("cat.jpg", 0)

plt.hist(image.ravel(), 256, [0, 255])
# image.ravel(): 다차원 배열을 1차원 배열로 변환
# 256: x-axis element의 개수(bin)
# [0, 256]: x-axis element의 값의 범위
plt.show()