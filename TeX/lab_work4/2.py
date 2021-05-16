import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('2.csv')


Um = df['Y'][0] * df['volts/div'][0]
b = df['R'][0]/(2*df['L'][0])


T = 0.74 * df['time/div'][0]
w0 = (2*math.pi)/(T)
w = math.sqrt(abs(w0**2 - b**2))

fig, ax = plt.subplots()

#ax.set_xlim([-10, 10])
#ax.set_ylim([-2, 2])
ax.set_title('title')
ax.set_xlabel('ось X')
ax.set_ylabel('ось Y')


xp = df['X']*df['time/div'][0]
yp = df['Y']*df['volts/div'][0]
ax.scatter(xp, yp,  marker = 'o',
                   c = 'red',
                   s = 20,
                   linewidths = 1,
                   edgecolors = 'black')

x = np.linspace(0,6*df['time/div'][0],1000)
y = Um * math.e**(-b*x)*np.sin(w*x)
ax.plot(x,y,
        color='black',
        label = '')

plt.show()

