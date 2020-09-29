import matplotlib.pyplot as plt
import numpy as np
import math

g = 0.058 
a = 388.388
y = lambda x: (1/(math.sqrt(2*math.pi)*g))*np.exp(-(x-a)**2/(2*g**2))
plt.xlabel('Время (с)')
plt.ylabel('Плотность вероятности')
plt.text(4,1,'$\sigma=0.418$')
plt.text(3.9,0.9,'$<t>=4.74 (с)$')
x = np.linspace(3.5,5.93,100)
#plt.plot(x,y(x),color='red')
a = [388,389,389.3,387.7,388.8,
388,388.4,388.1,387.5,389.4,
388.1,387.9,388.4,388.3,389.4,
388.9,388.9,387.3,388.3,389,
387.3,388.7,387.8,388.6,387.9,
390.2,387.6,388.5,388.2,388.6,
387.8,387.2,387.6,387.5,
389.5,387.9,388.3,389.4,
389.6,388,388.2,387.5,
388.8,388.6,387.9,389.1,
388.1,389.2,388.5,388.6,]
hist = np.histogram(a,bins=7, density=True)[0]
plt.bar([3.67,4.02,4.37,4.71,5.06,5.41,5.76],hist,width=0.1,color='black')
#plt.show()

summ = 0
for i in range(50):
    summ = summ + (a[i]- a)**2
print(a[1])
