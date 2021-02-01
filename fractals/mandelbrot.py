import numpy as np
import matplotlib.pyplot as plt

import numpy as np

xmin, xmax, ymin, ymax = -2.5, 1.5, -2, 2
m, n = 600, 600
itr = 100
border = 2.0

image = np.zeros((m, n))


for iw, w in enumerate(np.linspace(xmin, xmax, n)):
    for ie, e in enumerate(np.linspace(ymin, ymax, m)):
        c = w + 1j * e

        z = 0
        for k in range(itr):
            z = z*z + c

            if abs(z) > border:
                image[iw, ie] = k
                break

plt.xticks([])
plt.yticks([])

plt.imshow(-image.T, cmap='flag')
plt.show()
