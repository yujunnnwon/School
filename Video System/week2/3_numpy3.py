import numpy as np

""" Broadcasting """
x = np.array([[1, 2], [3, 4]])
print(x + 10)

x = np.array([[1, 2], [3, 4]])
y = np.array([[10], [20]])
print(x + y)

""" .matmul: 행렬곱 """
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a * b)
print(a @ b)
print(np.matmul(a, b))

"""
<통계 관련>
sum(): 합계
    x.sum(axis=0): 행별 합계
    x.sum(axis=1): 열별 합계
mean(): 평균
min(), max(): 최소값, 최대값
var(), std(): 분산, 표준편차
"""