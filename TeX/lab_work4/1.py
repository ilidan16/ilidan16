import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('1.csv')

a = np.array([])
for i in range(len(df['X']) - 1):
    a = np.append(a, df['X'][i+1]-df['X'][i])
    
b = df['R'][0]/(2*df['L'][0])
Um = df['Y'][0]*df['volts/div'][0] * np.exp(b*df['X'][0]*df['time/div'][0])

T = a.mean() * df['time/div'][0]
w0 = (2*np.pi)/(T)
w = np.sqrt(abs(w0**2 - b**2))

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
                   edgecolors = 'black',
                   zorder=2)

x = np.linspace(0,6*df['time/div'][0],1000)
y = Um * np.exp(-b*x) * np.sin(w*x)
ax.plot(x,y,
        color='black',
        label = '',
        zorder=1)

plt.show()

