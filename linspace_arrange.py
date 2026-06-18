# NumPy arange vs linspace - linspace_arrange.py
# This file compares two NumPy functions for generating sequences of numbers:
#
#   np.arange(start, stop, step):
#     - Generates values from start to stop with a fixed step size.
#     - Accepts float arguments (e.g. step=0.2).
#     - Stop value is NOT included.
#     - Use when you know the step size.
#
#   np.linspace(start, stop, num):
#     - Generates exactly `num` evenly spaced values between start and stop.
#     - Stop value IS included by default.
#     - Use when you know how many points you need.
#     - Commonly used to define smooth x-axis/y-axis values for plotting.
#
# Example:
#   arange(0, 2, 0.2)  → [0.0, 0.2, 0.4, ..., 1.8]   (step-based)
#   linspace(0, 2, 9)  → [0.0, 0.25, 0.5, ..., 2.0]  (count-based)
#
#ITS ACCEPTS FLOAT ARGUMENTS AS WELL


import numpy as np
import pandas as pd
from numpy import pi
a = np.arange(10,20,2)

print(a)

b = np.arange(0, 2, 0.2)
print(b)



#linspace is generally used to create an array of evenly spaced values over a specified range. It is often used when you want to create a specific number of points between two values, rather than specifying the step size as in arange.
c = np.linspace(0,2,9)
print(c)
#linspace is used to define x -axis and y-axis values for plotting functions. It is particularly useful when you want to create smooth curves or graphs by generating a set of points that represent the function's behavior over a specified interval.
