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
half_x = (xmin + xmax)/2


m = 500
n = 500
itr = 200
border = 2.0
#===================================================
"""
Будем разбивать множество на две части по оси абсцисс,
вычислять эти части "параллельно", а затем склеивать.
"""
left_image = np.zeros((m, int(n/2)))
right_image = np.zeros((m, int(n/2)))

def mandelbrot(xmin,xmax,m,n,part_image, ymin=ymin, ymax=ymax, itr=itr, border=border):
    for i_y, y in enumerate(np.linspace(ymin, ymax, m)):
        for i_x, x in enumerate(np.linspace(xmin, xmax, n)):
            c = x + y * 1j
            z = 0
            for k in range(itr):
                z = z**2 + c
                if abs(z) > border:
                    part_image[i_y,i_x] = k
                    break
#===================================================
# Создаём два потока
t0 = time.time()
if __name__ == '__main__':
    t1 = Thread(target=mandelbrot, args=(xmin,half_x,m,int(n/2),left_image,))
    t2 = Thread(target=mandelbrot, args=(half_x,xmax,m,int(n/2),right_image,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

full_image = np.concatenate((left_image, right_image), axis=1) #склеиваем
print(time.time()-t0)

t0 = time.time()
image = np.zeros((m, n))
mandelbrot(xmin,xmax,m,n,image,)
print(time.time()-t0)

plt.figure(figsize=(8, 8))
plt.xticks([])
plt.yticks([])
plt.imshow(-full_image, cmap='flag')
plt.show()


"""
image_s = np.zeros((m, n))
mandelbrot(xmin,xmax,m,n,image_s, -2, 2, itr=itr, border=border)
plt.figure(figsize=(8, 8))
plt.xticks([])
plt.yticks([])
plt.imshow(-image_s, cmap='flag')
plt.show()
"""
