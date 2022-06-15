import cv2

# open cv 버전 확인
# print(cv2.__version__)

image = cv2.imread("moon.png")
cv2.imshow("Original", image)
cv2.waitKey()                   # 바로 창이 종료되지 않도록 키 입력 대기
cv2.destroyAllWindows()         # 모든 창 종료