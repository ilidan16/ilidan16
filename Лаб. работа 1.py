import matplotlib.pyplot as plt
import numpy as np
import math


g = 0.418
a = 4.738
y = lambda x: (1/(math.sqrt(2*math.pi)*g))*np.exp(-(x-a)**2/(2*g**2))
plt.subplots() 
plt.xlabel('Время (С)')
plt.ylabel('Плотность вероятности')
plt.text(4,1,'$\sigma=0.418$')
plt.text(3.9,0.9,'$<t>=4.74(c)$')
x = np.linspace(3.5,5.93,100)
plt.plot(x,y(x),color='red')
a = [3.5,4,4.48,5.08,4.38,3.81,4.75,4.99,4.47,4.94,
     4.72,4.95,5.03,5.93,4.45,5.03,5.09,4.98,4.94,4.79,
     4.99,4.61,4.64,4.92,5.15,5.05,5.06,5.22,5.07,5.09,
     4.83,4.5,4.45,5.41,4.31,4.13,4.55,5.12,4.14,4.58,
     4.48,5.04,4.87,4.47,4.67,4.6,4.67,4.8,5,4.15]
hist = np.histogram(a,bins=7, density=True)[0]
plt.bar([3.67,4.02,4.37,4.71,5.06,5.41,5.76],hist,width=0.1,color='black')
plt.show()

