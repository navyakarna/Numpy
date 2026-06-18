# NumPy Array Reshaping - reshapping.py
# This file demonstrates how to reshape 1D arrays into multi-dimensional arrays:
#
#   np.arange(n)           : creates a 1D array of n elements [0, 1, 2, ..., n-1]
#   array.reshape(r, c)    : reshapes into a 2D array with r rows and c columns
#   array.reshape(d, r, c) : reshapes into a 3D array with d blocks, r rows, c cols
#
# Rules for reshape:
#   - Total elements must remain the same (e.g. 12 elements → reshape(3,4) = 3x4 = 12)
#   - arange(24).reshape(2,3,4) → 2 blocks of 3x4 = 24 elements total
#
# Dimensions at a glance:
#   arange(4)              → 1D: [0, 1, 2, 3]
#   arange(12).reshape(3,4)  → 2D: 3 rows, 4 cols
#   arange(24).reshape(2,3,4)→ 3D: 2 layers, 3 rows, 4 cols
import numpy as np

#use arrange to simply craete an evenly spaced array of numbers. It is similar to the built-in range function but returns an array instead of a list. It is often used to create arrays for indexing, slicing, or generating sequences of numbers for various purposes.
a = np.arange(4)
print(a)

b = np.arange(12).reshape(3,4)
print(b)

c = np.arange(24).reshape(2,3,4)
print(c)




