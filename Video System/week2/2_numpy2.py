import numpy as np

# linspace(): 수의 범위를 균일하게 나눈 array 생성
a = np.linspace(0, 10, 5)
print(a)                    # [ 0.   2.5  5.   7.5 10. ]

# eye(n): n by n identical matrix 생성
b = np.eye(3)
print(b)

# zeros((n, m)): n by m zero matrix 생성
array_0 = np.zeros((3, 5))            
print(array_0)

# ones((n, m)): n by m one matrix 생성
array_1 = np.ones((3, 5))
print(array_1)

# full(shape, fill_value): fill_value로 채워진 array 생성
array_num = np.full((3, 3), fill_value=5)
print(array_num)