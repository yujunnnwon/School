import cv2
import numpy as np

img = cv2.imread("hw_1_img.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # img를 grayscale로 변환
cv2.imshow("Original Grayscale Image", gray_img)

# Approximation Gaussian Kernel(3x3) 구현
kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16

gaussian_img = cv2.filter2D(gray_img, -1, kernel)
"""
앞서 Numpy를 통해 구현한 3x3 크기의 Gaussian Kernel을 적용하기 위해, Open CV의 filter2D 함수를 이용하였습니다.
filter2D 함수를 사용할 때 각각의 인자는 다음과 같습니다. cv2.filter2D(@src, @ddepth, @kernel)
@src: kernel을 적용할 이미지
@ddepth: 결과 영상의 깊이를 지정하는 인자로, -1로 지정하면 출력 영상의 깊이는 입력 영상과 같게 설정
@kernel: 적용할 kernel
"""
cv2.imshow("Gaussian Filtered Image", gaussian_img)
cv2.waitKey()
cv2.destroyAllWindows()

"""
아래의 코드는 3주차 실습 강의 노트 Down Sampling 부분에 포함된 코드입니다.
Numpy를 이용하여 만든 가우시안 커널과 Open CV에서 제공하는 GaussianBlur 적용 결과와의 비교를 위해 삽입했습니다.
"""
# H, W, C = img.shape
# DN = 2

# compare_with_cv_func = cv2.GaussianBlur(gray_img, (3, 3), 0)
# sample_img = compare_with_cv_func[0:H:DN, 0:W:DN]
# cv_img = cv2.resize(sample_img, (W, H))
# cv2.imshow("with_LPF", cv_img)

# cv2.waitKey()
# cv2.destroyAllWindows()
