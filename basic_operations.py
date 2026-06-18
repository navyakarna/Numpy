# NumPy Basic Operations - basic_opeartion.py
# This file covers fundamental operations on NumPy arrays:
#
#   Arithmetic        : a-b, a**2 (element-wise subtraction and power)
#   Math functions    : np.sin(a) — applied element-wise across the array
#   Comparison        : a < 3 — returns a boolean array (True/False per element)
#
#   Matrix operations :
#     A * B           → element-wise multiplication (NOT matrix multiply)
#     A @ B           → matrix multiplication (dot product)
#     A.dot(B)        → same as A @ B
#
#   Random arrays     : np.random.default_rng() — reproducible random values
#   Aggregations      : a.sum(), a.min(), a.max() — reduce entire array to one value
#
#   Axis-based sum    :
#     b.sum(axis=0)   → sum down each column (result has shape = num cols)
#     b.sum(axis=1)   → sum across each row  (result has shape = num rows)



import numpy as np
a = np.array([1,3,4])
b = np.arange(3)

print(b)
print(a)

c = (a-b)
print(c)


d = (a**2)
print(d)

e = 10 * np.sin(a)
print(e)

f = a < 3
print(f)

A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])

c = A * B
print(c)

d = A @ B
print(d)

e = A.dot(B)
print(e)


rg = np.random.default_rng(1)
a = np.ones((2,3), dtype=np.int_)

a *= 3
print(a)

b = rg.random((2,3))
print(b)

b += a
print(b)

a = rg.random((2,3))
print(a)

print(a.sum())

print(a.min())

print(a.max())


b = np.arange(12).reshape(3,4)
print(b)

print(b.sum(axis=0))

print(b.sum(axis=1))
