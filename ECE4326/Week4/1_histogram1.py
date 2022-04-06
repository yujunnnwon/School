import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./cat.jpeg", 0)

plt.hist(image.ravel(), 256, [0, 255])
"""
image.ravel(): 다차원 배열을 1차원 배열로 변환
256: x-axis element의 개수(bin)
[0, 256]: x-axis element의 값의 범위
"""
plt.show()

"""
최초 코드는 동작하지 않았음.
cat.jpg의 이미지의 형식이 jpeg라는 것을 확인한 후, 확장자 명을 바꾼 후 실행하였을 때 정상적으로 동작함.
"""