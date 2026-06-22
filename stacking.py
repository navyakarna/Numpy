# NumPy Array Stacking
#
# Stacking combines multiple arrays into one along a given axis.
#
# np.vstack((a, b))      → vertical stack: joins arrays along rows (axis 0)
#                           arrays must have the same number of columns
#                           e.g. (4,2) + (7,2) → (11,2)
#
# np.hstack((a, b))      → horizontal stack: joins arrays along columns (axis 1)
#                           arrays must have the same number of rows
#                           e.g. (4,2) + (4,3) → (4,5)
#
# np.newaxis             → inserts a new axis, increasing the array's dimensions by 1
#                           a[:, np.newaxis] turns shape (n,) into (n,1)
#                           useful when you need to align dimensions before stacking

import numpy as np
import numpy.random as rg

a = np.floor(10 * rg.random((4,2))) 
# print(a)

b = np.floor(10 * rg.random((7,2))) 
# print(b)


print(np.vstack((a,b)))
print(np.hstack((a,b)))

print(np.hstack((a[:, np.newaxis],b)))

