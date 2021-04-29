import matplotlib.pyplot as plt
import numpy as np
import math
    
fig, ax = plt.subplots()

#ax.set_xlim([-10, 10])
#ax.set_ylim([-2, 2])
ax.set_title('title')
ax.set_xlabel('ось X')
ax.set_ylabel('ось Y')

x = []
y = []

ax.scatter(x, y,  
        color = 'k',
        s = 15,
        label = '')

ax.plot(x,y,
        color='red',
        label = '')

ax.legend(shadow = False,fontsize = 15,edgecolor = 'k') # легенда

ax.set_axisbelow(True) # рисует сетку НЕ на точках
ax.grid(linestyle='-', linewidth='0.5', color='gray') # сетка

"""
# размеры окна
fig.set_figheight(5)
fig.set_figwidth(8)
"""

fig.savefig('name.pdf', dpi = 600)#сохранение файла
plt.show()

