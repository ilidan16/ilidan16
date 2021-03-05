import time
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

from multiprocessing import Process
#===================================================
# https://mandel.gart.nz/
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

m = 10
n = 10
itr = 200
border = 2.0
#===================================================
image1 = np.zeros((m, int(n/2)))
image2 = np.zeros((m, int(n/2)))
def mandelbrot(xmin,xmax,m,n,image_i, ymin=ymin, ymax=ymax, itr=itr, border=border):
    image = image1
    for i_y, y in enumerate(np.linspace(ymin, ymax, n)):
        for i_x, x in enumerate(np.linspace(xmin, xmax, m)):
            c = x + y * 1j
            z = 0
            for k in range(itr):
                z = z**2 + c
                if abs(z) > border:
                    image[i_x,i_y] = k
                    break
                print(image1)
#===================================================
half_x = (xmin + xmax)/2

t0 = time.time()
if __name__ == '__main__':
    p1 = Process(target=mandelbrot, args=(xmin, half_x, m, int(n/2), image1))
    p2 = Process(target=mandelbrot, args=(half_x, xmax, m, int(n/2), image2))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
print(time.time() - t0)

#print(image1)
#print(image2)
image = np.concatenate((image1,image2), axis=1)
#print(image)



