import cv2
import numpy

def bgr2gray(bgr_img):
    # 영상의 각 채널을 분리
    b, g, r = bgr_img[:, :, 0], bgr_img[:, :, 1], bgr_img[:, :, 2]      # 영상의 각 채널을 분리
    result = (0.114 * b) + (0.587 * g) + (0.299 * r)                    # RGB -> Grayscale

    # cv2로 불러온 이미지는 numpy array의 형태
    return result.astype(numpy.uint8)       # astype()을 사용하여 result의 data type을 uint8로 변환

img = cv2.imread("winner.jpeg")
Gray_img = bgr2gray(img)
cv2.imshow('rgb to gray', Gray_img)
cv2.waitKey()
cv2.destroyAllWindows()