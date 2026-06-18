# NumPy Array Creation - array_properties.py
# This file explores various ways to create NumPy arrays:
#   - np.array()  : create arrays from lists (1D, 2D, with dtype like complex)
#   - np.zeros()  : create arrays filled with 0s
#   - np.ones()   : create arrays filled with 1s
#   - np.empty()  : create uninitialized arrays (random garbage values)
#   - np.arange() : create arrays with evenly spaced values (like Python range)
# Also demonstrates element-wise multiplication between arrays.
import numpy as np
# a = np.array([2,3,4])

# # print(a)

# b = np.array([[1,2,3],[4,5,6]])

# # print(b)

# a = np.array([1,2,3], dtype=complex)
# # print(a)

# print(a*b)

# c =np.zeros((3,4))
# print(c)

# d = np.ones((2,3,3))
# print(d)

# e = np.empty((2,3))
# print(e)

f = np.arange(10,20,2)
print(f)
