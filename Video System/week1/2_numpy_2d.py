from tokenize import _all_string_prefixes
import numpy as np

# 2D Array
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
arr_a = np.array(a)
arr_b = np.array(b)

print(type(a))              # <class 'list'>
print(type(b))              # <class 'list'>
print(type(arr_a))          # <class 'numpy.ndarray'>
print(type(arr_b))          # <class 'numpy.ndarray'>

print("arr_a = ", arr_a)
# arr_a =  [[1 2 3]
#           [4 5 6]
#           [7 8 9]]

print("arr_b = ", arr_b)
# arr_b =  [[7 8 9]
#           [4 5 6]
#           [1 2 3]]