import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('1.csv')

a = np.array([])
for i in range(len(df['X']) - 2):
    a = np.append(a, df['X'][i+2]-df['X'][i])
    
b = df['R'][0]/(2*df['L'][0])
Um = df['Y'][0]*df['volts/div'][0] * np.exp(b*df['X'][0]*df['time/div'][0])

T = a.mean() * df['time/div'][0]
w0 = (2*np.pi)/(T)
w = np.sqrt(abs(w0**2 - b**2))

fig, ax = plt.subplots()


ax.set_title('Параметры контура:\n L=5,7 мГн;   C=97,9 нФ;   R=16,65 Ом',fontsize=14)
ax.set_xlabel('Время $t$, мс.', fontsize=13)
ax.set_ylabel('Напряжение $U$, В',fontsize=13)


xp = df['X']*df['time/div'][0]*1E3
yp = df['Y']*df['volts/div'][0]
ax.scatter(xp, yp,  marker = 'o',
                   c = 'red',
                   s = 20,
                   linewidths = 1.1,
                   edgecolors = 'black',
                   zorder=2)

x = np.linspace(0,6*df['time/div'][0]*1E3,1000)
y = Um * np.exp(-b*x*1E-3) * np.sin(w*x*1E-3 - 0.2*0.1E-3*w)
ax.plot(x,y,
        color='black',
        label = r'$U(t)=U_m\,e^{-\beta t}\,\sin{\omega t}$',
        zorder=1)

ax.legend(shadow = False,fontsize = 15,edgecolor = 'k')
ax.set_axisbelow(True) # рисует сетку НЕ на точках
ax.grid(linestyle='-', linewidth='0.5', color='gray')

fig.set_figheight(5)
fig.set_figwidth(8)

fig.savefig('pictures/1.pdf', dpi = 600)
plt.show()

