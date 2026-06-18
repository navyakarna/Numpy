# NumPy Array Dimensions & Properties - array_dim.py
# This file explores key properties of NumPy arrays:
#   - np.arange() + reshape() : create a 1D range and reshape it into a 2D array (3x5)
#   - a.shape   : returns the dimensions of the array as a tuple (rows, cols)
#   - a.ndim    : returns the number of dimensions (e.g. 2 for a 2D array)
#   - a.dtype   : returns the data type of the array elements (e.g. int64)
#   - a.size    : returns the total number of elements in the array
#   - type(a)   : returns the Python type, which is <class 'numpy.ndarray'>
# Also creates a simple 1D array and checks its type.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.arange(15).reshape(3,5)

print(a)

np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])


print(a.shape)

print(a.ndim)

print(a.dtype.name)

print(a.size)

print(type(a))

b = np.array([6,7,8])
print(b)

print(type(b))

