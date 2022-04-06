import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("img64.jpeg", 0)
plt.imshow(image, cmap="gray")
plt.show()

M, N = image.shape

# 1. Zero-padding ------------------------------------------------------------
P, Q = 2*M, 2*N
padded_image = np.zeros((P, Q))
padded_image[:M, :N] = image
plt.imshow(padded_image, cmap="gray")
plt.show()
# ----------------------------------------------------------------------------

# 2. Centering ---------------------------------------------------------------
padded_image_new = np.zeros((P, Q))
for x in range(P):
    for y in range(Q):
        padded_image_new[x, y] = padded_image[x, y] * ((-1)**(x+y))
# ----------------------------------------------------------------------------

# 3. DFT ---------------------------------------------------------------------
def DFT(padded_image):
    M, N = padded_image.shape
    tmp_img = np.zeros((M, N), dtype=complex)   # 하나의 축에 대한 DFT의 결과를 담기 위한 임시 Numpy array
    dft2d = np.zeros((M, N), dtype=complex)     # 최종 결과를 담을 Numpy array
    
    m = np.arange(M)                            # padded_image의 M을 ascending order로 만듦 (1xM matrix)
    n = np.arange(N)
    x = m.reshape((M, 1))                       # 1xM matrix를 Mx1 matrix로 변환
    y = n.reshape((N, 1))
    for row in range(M):
        M1 = np.exp(-2j * np.pi * y * n / N)                        # Numpy array의 x-axis에 대한 DFT
        tmp_img[row] = np.dot(M1, padded_image[row])                # tmp_img의 row 성분에 입력
    for col in range(N):
        M2 = np.exp(-2j * np.pi * x * m / M)                        # y-axis에 대한 DFT
        dft2d[:, col] = np.dot(M2, tmp_img[:, col])                 # tmp_img의 col 성분에 M2를 입력
    
    return dft2d                                                    # 최종 결과를 dft2d로 반환

dft2d = DFT(padded_image_new)
plt.imshow(dft2d.real, cmap="gray")
plt.show()
# ----------------------------------------------------------------------------

# 4. Filtering ---------------------------------------------------------------
def ideal_LPF(image):
    M, N = image.shape
    H = np.zeros((M, N))
    D = np.zeros((M, N))
    U0 = int(M / 2)
    V0 = int(N / 2)

    D0 = 10                 # cut-off frequency
    
    for u in range(M):
        for v in range(N):
            u2 = np.power(u, 2)
            v2 = np.power(v, 2)
            D[u, v] = np.sqrt(u2 + v2)
    
    for u in range(M):
        for v in range(N):
            if D[np.abs(u - U0), np.abs(v - V0)] <= D0:
                H[u, v] = 1
            else:
                H[u, v] = 0
    return H

# ideal LPF의 연산을 수행하여 H(u, v)를 만듦
lpf = ideal_LPF(dft2d)
plt.imshow(lpf, cmap="gray")
plt.show()

# G(u,v) = F(u,v)H(u,v) 연산
G = np.multiply(dft2d, lpf)
plt.imshow(G.real, cmap="gray")
plt.show()
# ----------------------------------------------------------------------------

# 5. Inverse DFT -------------------------------------------------------------
# DFT와 IDFT의 차이는 exponential 계수의 +와 -의 차이이기 때문에 DFT의 코드에서 exponential의 -2를 2로 수정하여 구현
def IDFT(dft_image):    
    M, N = dft_image.shape
    tmp_img = np.zeros((M, N), dtype=complex)
    idft2d = np.zeros((M, N), dtype=complex)

    m = np.arange(M)
    n = np.arange(N)
    x = m.reshape((M, 1))
    y = n.reshape((N, 1))

    for row in range(M):
        M1 = np.exp(2j * np.pi * y * n / N)
        tmp_img[row] = np.dot(M1, dft_image[row])
    for col in range(N):
        M2 = np.exp(2j * np.pi * x * m / M)
        idft2d[:, col] = np.dot(M2, tmp_img[:, col])
    
    return idft2d

# IDFT
idft2d = IDFT(G)

# De-centering
for x in range(P):
    for y in range(Q):
        idft2d[x, y] = idft2d[x, y] * ((-1) ** (x + y))

# Remove zero-padding part
plt.imshow(idft2d[:int(P/2), :int(Q/2)].real, cmap="gray")
plt.show()
# ----------------------------------------------------------------------------