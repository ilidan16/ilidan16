import matplotlib.pyplot as plt
import numpy as np
import math
    
fig, ax = plt.subplots()

#ax.set_xlim([-10, 10])
#ax.set_ylim([-2, 2])
ax.set_title('Вольт-амперная характеристика')
ax.set_xlabel('Напряжение $U_{\parallel}$, В')
ax.set_ylabel('Сила тока $I$, мА')


y1 = np.arange(5,45,5)
x1 = [0.22,0.46,0.75,0.98,1.22,1.49,1.77,2.07]

x2 = np.linspace(0,2.2,1000)
y2 = 1.10543 + 19.1023*x2

ax.scatter(x1, y1,
        color = 'k',
        s = 15)

ax.plot(x2,y2,
        color='red',
        label = '$I(U_{\parallel})=19.1U_{\parallel}+1.1$')

ax.legend(shadow = False,fontsize = 15,edgecolor = 'k')

ax.set_axisbelow(True) # рисует сетку НЕ на точках
ax.grid(linestyle='-', linewidth='0.5', color='gray')

"""
fig.set_figheight(5)
fig.set_figwidth(8)
"""

fig.savefig('pictures/BAX.pdf', dpi = 600)
plt.show()

