# NumPy Array Shape Manipulation
#
# Arrays have a .shape attribute (e.g. (3,4) = 3 rows, 4 cols).
# Shape manipulation restructures data without changing its values.
#
# .ravel()         → flattens any array to 1D; returns a view when possible
# .reshape(r, c)   → reorganizes into new shape; total elements must stay the same
#                    use -1 for one dim to let NumPy calculate it: reshape(-1, 1)
# .T               → transposes (flips rows/cols); always returns a view
#
# All three preserve the underlying data — they only change how it's indexed.
# Use .copy() if you need an independent copy.

import numpy as np
import numpy.random as rg

a = np.array(10* rg.random((3,4)))

print(a)
print(a.shape) #tell shape

print(a.ravel()) #ravel is used to flatten the array into a 1D array. It returns a view of the original array whenever possible. If the original array is not contiguous in memory, it will return a copy. The shape of the original array is not changed.

print(a.reshape(2,6)) #reshape

print(a.T) #transform
