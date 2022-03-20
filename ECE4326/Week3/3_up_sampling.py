# NN(Nearest Neiborhood) Interpolation
# Original 신호 중 가장 인접한 신호를 이용하여 보간하는 방법
import cv2
import numpy as np

img = cv2.imread("fig0.PNG")
H, W, C = img.shape

# Up Sampling
UP = 2

# Before Interpolation
NN = cv2.resize(img, dsize=(W*UP, H*UP), interpolation=cv2.INTER_NEAREST)   # interpolation을 NN으로 설정

UPSAM = np.zeros((H*UP, W*UP, C))                                           # (H*UP, W*UP, C)의 3차원 matrix 생성
"""UPSAM(zero matrix)의 픽셀에 img의 픽셀을 mapping"""
for i in range(H):
    for j in range(W):
        UPSAM[2*i, 2*j, :] = img[i, j, :]

UPSAM = UPSAM.astype(np.uint8)                                              # UPSAM의 matrix를 형변환
cv2.imshow("Before_interpolation", UPSAM)

# After Interpolation
for i in range(H):
    for j in range(W):
        UPSAM[2*i+1, 2*j+1, :] = img[i, j, :]
        UPSAM[2*i, 2*j+1, :] = img[i, j, :]
        UPSAM[2*i+1, 2*j, :] = img[i, j, :]

UPSAM = UPSAM.astype(np.uint8)
cv2.imshow("After_interpolation", UPSAM)
cv2.waitKey()
cv2.destroyAllWindows()
