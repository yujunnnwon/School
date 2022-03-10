import cv2

# 흑백 이미지에 대해 픽셀값을 특정 조건으로 변환하는 함수
def change_value(value):
    if value < 64:
        return 64
    elif value < 128:
        return 128
    elif value < 192:
        return 192
    else:
        return 255 

img = cv2.imread("winner.jpeg", cv2.IMREAD_GRAYSCALE)   # "winner.jpeg"를 grayscale로 읽음
width, height = img.shape                               # img의 width와 height의 값을 구하여 저장

for x in range(width):                      # x축은 width를 범위로 설정
    for y in range(height):                 # y축은 height를 범위로 설정
        tmp = img[x, y]                     # img의 좌표를 tmp에 저장
        return_value = change_value(tmp)    # tmp를 change_value()를 통해 픽셀값 변환
        img[x, y] = return_value            # 변환된 픽셀값을 다시 img의 좌표로 할당

cv2.imshow("output", img)
cv2.imwrite("output.jpeg", img)             # 변환된 흑백 이미지를 저장
cv2.waitKey()
cv2.destroyAllWindows()