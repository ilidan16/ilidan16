import numpy as np
import matplotlib.pyplot as plt
#===================================================

xmin = -2.5
xmax = 1.5
ymin = -2
ymax = 2
m, n = 1000, 1000
itr = 300
border = 2.0
#===================================================

def mandelbrot(xmin, xmax, ymin, ymax, m, n, itr, border):
    image = np.zeros((m, n))
    x, y = np.mgrid[xmin:xmax:(n*1j), ymin:ymax:(m*1j)]
    c = x + 1j * y
    z = np.zeros_like(c)
    for k in range(itr):
        z = z * z + c
        mask = (np.abs(z) > border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan

    return -image.T
#===================================================

plt.figure(figsize=(8, 8))
image = mandelbrot(xmin, xmax, ymin, ymax, m, n, itr, border)
plt.xticks([])
plt.yticks([])
plt.imshow(image, cmap='flag', interpolation='none')
plt.show()
