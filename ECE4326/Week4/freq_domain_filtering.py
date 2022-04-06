import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("img64.jpeg", 0)
plt.imshow(image, cmap="gray")
plt.show()

M, N = image.shape

# 1. Zero-padding ------------------------------------------------------------
P, Q = 2*M, 2*N
padded_image = np.zeros((P, Q))                 # (2M,2N)의 크기로 영행렬 생성
padded_image[:M, :N] = image                    # 좌측 상단의 영행렬에 M, N을 붙여넣음
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
    dft2d = np.zeros((M, N), dtype=complex)

    for k in range(M):
        for l in range(N):
            sum_ = 0.0
            for m in range(M):
                for n in range(N):
                    e = np.exp(-2j * np.pi * ((k*m)/M + (l*n)/N))
                    sum_ += padded_image[m, n] * e
            dft2d[k, l] = sum_
    return dft2d

dft2d = DFT(padded_image_new)
print("Complete the DFT with centering")
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

# 함수를 통해 정의한 LPF 연산을 진행하는 부분
lpf = ideal_LPF(dft2d)
plt.imshow(lpf, cmap="gray")
plt.show()

# G(u,v) = F(u,v)H(u,v)를 연산
G = np.multiply(dft2d, lpf)
plt.imshow(G.real, cmap="gray")
plt.show()
# ----------------------------------------------------------------------------

# 5. Inverse DFT -------------------------------------------------------------
def IDFT(dft_image):
    M, N = dft_image.shape
    idft2d = np.zeros((M, N), dtype=complex)

    for k in range(M):
        for l in range(N):
            sum_ = 0.0
            for m in range(M):
                for n in range(N):
                    e = np.exp(2j * np.pi * ((k*m)/M + (l*n)/N))
                    sum_ += dft_image[m, n] * e
            idft2d[k, l] = sum_
    
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


# # +) Magnitude & Phase
# mag = np.abs(dft2d)
# phase = dft2d / mag

# mag2d = IDFT(mag)

# for x in range(P):
#     for y in range(Q):
#         mag2d[x, y] = mag2d[x, y] * ((-1) ** (x+y))

# print("Complete the DFT with centering")
# plt.imshow(mag2d.real, cmap="gray")
# plt.show()

# phase2d = IDFT(phase)

# for x in range(P):
#     for y in range(Q):
#         phase2d[x, y] = phase2d[x, y] * ((-1) ** (x+y))

# print("Complete the DFT with centering")
# plt.imshow(phase2d.real, cmap="gray")
# plt.show()