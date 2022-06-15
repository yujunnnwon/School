import cv2

img = cv2.imread("input.jpg")                       # 이미지 불러오기
cv2.imshow("original image", img)                   # 원본 이미지 출력

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # grayscale로 변환
cv2.imshow('grayscale image', gray_img)             # grayscale 이미지 출력
cv2.waitKey()
cv2.destroyAllWindows()                             # cv2로 불러온 이미지는 numpy array 형태(<class 'numpy.ndarray'>)

# 영상의 B, G, R 채널 분리
b, g, r = cv2.split(img)                            # cv2.split()을 이용한 채널 분리
b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]  # 리스트 슬라이싱을 이용한 분리