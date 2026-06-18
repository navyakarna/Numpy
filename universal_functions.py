# NumPy Universal Functions (ufuncs) - universal_functions.py
# Universal functions (ufuncs) are functions that operate element-wise on arrays.
# They are faster than regular Python loops as they are implemented in C.
#
#   np.exp(a)   : computes e^x for every element in the array
#
# Other commonly used ufuncs (reference list):
#   Math      : ceil, floor, round, clip, sqrt, log, exp, prod, cumsum, cumprod
#   Stats     : mean, median, std, var, min, max, average, corrcoef, cov
#   Logic     : all, any, nonzero, where
#   Sorting   : sort, argsort, lexsort, argmax, argmin
#   Linear Algebra : dot, inner, outer, cross, vdot, transpose, trace
#   Misc      : diff, invert, conj, bincount, vectorize, apply_along_axis
import numpy as np

b = np.arange(12).reshape(3,4)
print(b)
print(np.exp(b))

#all, any, apply_along_axis, argmax, argmin, argsort, average, bincount, 
# ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot,
#  floor, inner, invert, lexsort, max, maximum, mean, median, min, minimum,
#  nonzero, outer, prod, re, round, sort, std, sum, trace, transpose, var, 
# vdot, vectorize, where
