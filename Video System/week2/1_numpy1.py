import numpy as np

# .shape: 데이터의 크기 확인
array_2d = np.array([[1, 2], [3, 4]])
print(array_2d.shape)                   # (2, 2)

array_3d = np.array([[[1, 2], [3, 4]],
                     [[5, 6], [7, 8]]])
print(array_3d.shape)                   # (2, 2, 2)

# .dtype: 타입 설정
array = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float16)
print(array)                            # [[1. 2. 3.]
                                        #  [4. 5. 6.]]
print(array.dtype)                      # float16
"""
(sign: 부호, exponent: 지수, mantissa: 가수)
float16: sign bit, 5 bits exponent, 10 bits mantissa
float32: sign bit, 8 bits exponent, 23 bits mantissa
float64: sign bit, 11 bits exponent, 52 bits mantissa
"""

# .size: 총 element의 개수
print(array.size)                       # 6