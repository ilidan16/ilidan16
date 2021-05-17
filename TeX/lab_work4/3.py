import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('3.csv')

a = np.array([])
for i in range(len(df['X']) - 2):
    a = np.append(a, df['X'][i+2]-df['X'][i])
    
b = df['R'][0]/(2*df['L'][0])
Um = df['Y'][0]*df['volts/div'][0] * np.exp(b*df['X'][0]*df['time/div'][0])
T = a.mean() * df['time/div'][0]
w0 = (2*np.pi)/(T)
w = np.sqrt(abs(w0**2 - b**2))


fig, ax = plt.subplots()


ax.set_title('Контур №3\n L=5,7 мГн;   C=1 мкФ;   R=5,3 Ом',fontsize=14)
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

x = np.linspace(0,9*df['time/div'][0]*1E3,1000)
y = Um * np.exp(-b*x*1E-3) * np.sin(w*x*1E-3)
ax.plot(x,y,
        color='black',
        label = r'$U(t)=U_m\,e^{-\beta t}\,\sin{\omega t}$',
        zorder=1)

box = {'facecolor':'white',    #  цвет области
       'edgecolor': 'black',     #  цвет крайней линии
       'boxstyle': 'round'}    #  стиль области
text = fr'$\beta={round(b)}$'r' $c^{-1}$''\n'f'$U_m={round(Um,2)}$ B''\n'rf'$\omega={round(w)}$'r' $c^{-1}$'
ax.text(3.6, -0.36, text, bbox = box,
        fontsize = 13)


ax.legend(shadow = False,fontsize = 14,edgecolor = 'k')
ax.set_axisbelow(True) # рисует сетку НЕ на точках
ax.grid(linestyle='-', linewidth='0.5', color='gray')

fig.set_figheight(5)
fig.set_figwidth(8)

fig.savefig('pictures/3.pdf', dpi = 600)
plt.show()

