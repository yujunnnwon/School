import numpy as np

# 1D Array
a = [1, 2, 3, 4, 5]
b = np.array(a)

print(type(a))          # <class 'list'>
print(type(b))          # <class 'numpy.ndarray'>
print("a = ", a)        # a = [1, 2, 3, 4, 5]
print("b = ", b)        # b = [1 2 3 4 5]

# 1D Array의 연산: 동일한 Dimension의 성분별 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

print("a+b = ", a+b)
print("a-b = ", a-b)
print("a*b = ", a*b)
print("a/b = ", a/b)