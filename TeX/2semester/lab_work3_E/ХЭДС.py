import matplotlib.pyplot as plt
import numpy as np
import math
    
fig, ax = plt.subplots()

#ax.set_xlim([-10, 10])
#ax.set_ylim([-2, 2])
ax.set_title('ХЭДС при $I=15$ мА', fontsize = 14)
ax.set_xlabel('Магнитная индукция $B$, Тл', fontsize = 13)
ax.set_ylabel('ХЭДС $U_{\perp}$, В', fontsize = 13)

x1 = [0.007,0.014,0.032,0.056,0.080,0.103,0.123,0.148,0.176,0.207,0.222]
y1 = [30.0,30.8,32.7,35.4,38.2,40.7,43.0,45.6,48.5,51.7,53.3]

x2 = np.linspace(-0.01,0.25,50)
y2 = 29.3561+108.719*x2


ax.plot(x2,y2,
        color='black',
        label = '$U_{\perp}(B)=108.72B+29.36$')

ax.errorbar(x1, y1,
            yerr=1,
            marker='o',
            markeredgecolor='black',
            markerfacecolor='red',
            markersize=5,
            capsize=3,
            elinewidth=0.9,
            capthick=0.9,
            ecolor='black',
            linestyle='None')

ax.legend(shadow = False,fontsize = 14,edgecolor = 'k') # легенда

ax.set_axisbelow(True) # рисует сетку НЕ на точках
ax.grid(linestyle='-', linewidth='0.5', color='grey') # сетка


# размеры окна
fig.set_figheight(5)
fig.set_figwidth(8)


fig.savefig('pictures/Hall.pdf',dpi = 600)#сохранение файла
plt.show()

