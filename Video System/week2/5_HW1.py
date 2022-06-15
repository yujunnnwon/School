import cv2
import numpy as np

def bgr2gray(img):
    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]      # 입력된 이미지를 b, g, r 채널로 분리
    result = (b * 0.114) + (g * 0.587) + (r * 0.299)

    return result.astype(np.uint8)

bgr_img = cv2.imread("input.jpg")
gray_img = bgr2gray(bgr_img)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey()
cv2.destroyAllWindows()