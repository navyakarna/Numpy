# Mandelbrot Set
#
# The Mandelbrot set is a fractal defined in the complex plane.
# For each complex number C, we repeatedly apply: z = z² + C (starting from z=0)
# If the value of |z| stays bounded (≤ r) forever → C is IN the set
# If |z| escapes to infinity              → C is NOT in the set
#
# "Escape time" algorithm:
#   - Run the iteration up to `maxit` times for every point on a grid
#   - Record at which iteration each point diverges (escapes beyond radius r)
#   - Points that never diverge get value `maxit` (colored differently)
#   - Plotting these escape times with imshow produces the fractal image
#
# Key NumPy concepts used:
#   np.linspace   → creates evenly spaced x and y coordinates
#   np.meshgrid   → turns 1D x/y arrays into a 2D grid of complex numbers
#   np.zeros_like → initializes z array with same shape/type as C
#   Boolean masks → diverge, div_now used to update only relevant elements
#
# The colormap in imshow maps escape-time values to colors, revealing the fractal boundary.

import numpy as np
import matplotlib.pyplot as plt

def mandelbort(h , w, maxit=20, r=2):
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A,B = np.meshgrid(x,y)
    C = A +B*1j
    z = np.zeros_like(C)

    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i

        z[diverge] = r

    return divtime
plt.clf()
plt.imshow(mandelbort(600,300))
plt.show()





