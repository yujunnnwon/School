import cv2

# Down Sampling
img = cv2.imread("fig0.PNG")
H, W, C = img.shape                     # H, W, C를 각각 할당
cv2.imshow("original", img)

DN = 4                                  # Down Sampling을 시도할 때의 간격

# Case 1: Down Sampling without LPF
dw_img = img[0:H:DN, 0:W:DN]            # img의 H와 W를 각각 DN 간격으로 축소
dw_img = cv2.resize(dw_img, (W, H))     # Open CV의 resize를 이용하여 지정된 크기로 변환
cv2.imshow("without_LPF", dw_img)

# Case 2: Down Sampling with Gaussian Filter
dw = cv2.GaussianBlur(img, (5, 5), 2.0)
"""
cv2.GaussianBlur(img, kernel_shape, sigma): Open CV에서 제공하는 Gaussian Blur 함수
@kernel_shape: (width, height)
@sigma: standard deviation
"""
dw_1 = dw[0:H:DN, 0:W:DN]
dw_img = cv2.resize(dw_1, (W, H))       
cv2.imshow("with_LPF", dw_img)
cv2.waitKey()
cv2.destroyAllWindows()