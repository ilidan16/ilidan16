import time
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

from threading import Thread
#===================================================
# Поиск красивых мест: https://mandel.gart.nz/
"""
x = -1.748187465
y = 0.001251896
zoom = 711920010
d = 1600/zoom
xmin = x-d/2
xmax = x+d/2
ymin = y-d/2
ymax = y+d/2
"""

xmin = -2.5
xmax = 1.5
ymin = -2
ymax = 2

m = 500
n = 500
itr = 200
border = 2.0
#===================================================
image = np.zeros((m, n))
image1 = np.zeros((m, int(n/2)))
image2 = np.zeros((m, int(n/2)))
def mandelbrot(xmin,xmax,m,n,image_i, ymin=ymin, ymax=ymax, itr=itr, border=border):
    image = image_i
    for i_y, y in enumerate(np.linspace(ymin, ymax, n)):
        for i_x, x in enumerate(np.linspace(xmin, xmax, m)):
            c = x + y * 1j
            z = 0
            for k in range(itr):
                z = z**2 + c
                if abs(z) > border:
                    image[i_x,i_y] = k
                    break
#===================================================
half_x = (xmin + xmax)/2

t0 = time.time()
if __name__ == '__main__':
    t1 = Thread(target=mandelbrot, args=(xmin, half_x, m, int(n/2), image1,))
    t2 = Thread(target=mandelbrot, args=(half_x, xmax, m, int(n/2), image2,))
    
    t1.start()
    t2.start()

    t1.join(1)
    t2.join(1)
print(time.time() - t0)


t0 = time.time()
mandelbrot(xmin,xmax,m,n,image, ymin=ymin, ymax=ymax, itr=itr, border=border)
print(time.time() - t0)
