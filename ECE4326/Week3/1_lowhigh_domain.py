import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import cv2

img = cv2.imread("lowhigh_domain.jpg")
high_domain = img[350:450, 1300:1400, 1]    # 영상의 채널 분리 중 G 채널
low_domain = img[100:200, 1100:1200, 1]
# [:,:,0]: B / [:,:,1]: G / [:,:,2]: R

x = range(100)                              # x와 y의 범위를 0에서 99로 설정
y = range(100)
x, y = np.meshgrid(x, y)                    # np.meshgrid(x, y): x와 y를 축으로 갖는 격자 그리드 생성

fig = plt.figure()                          # plt.figure(): 한 화면에 여러 개의 그래프를 그리기 위한 함수
"""
fig.add_subplot()을 통해 그래프 추가 가능
fig.add_subplot(121): 1행 2열의 subplot을 생성하고, 그 중 1번째 plot에 해당하는 그래프
                      즉, 좌-우의 2개의 그래프를 생성하고, 그 중에서 좌측의 그래프를 의미
"""
ax0 = fig.add_subplot(121, projection="3d") # 좌측의 그래프에 3d로 projection
ax1 = fig.add_subplot(122, projection="3d") # 우측의 그래프에 3d로 projection
"""
plot_surface(x,y,z)
표면 플롯을 제작하기 위한 함수. x,y,z는 모두 2차원 배열.
cmap은 그래프의 색을 결정하는 argument. ex) viridis, plasma, inferno, magma, cividis
"""
ax0.plot_surface(x, y, high_domain, cmap=cm.plasma)    # high_domain을 z축으로 설정
ax1.plot_surface(x, y, low_domain, cmap=cm.plasma)     # low_domain을 z축으로 설정
plt.show()