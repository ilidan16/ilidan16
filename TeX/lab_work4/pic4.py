import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import math

df = pd.read_csv('4.csv')

fig, ax = plt.subplots()


ax.set_title('Контур №4',fontsize=14)
ax.set_ylabel('Напряжение $U$, В',fontsize=13)

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

xp = df['X']*df['time/div'][0]*1E3
yp = df['Y']*df['volts/div'][0]
plt.scatter(xp, yp,  marker = 'o',
                   c = 'red',
                   s = 20,
                   linewidths = 1.1,
                   edgecolors = 'black',
                   zorder=2)
plt.vlines(xp, 0, yp, linestyle="dashed", color='grey',zorder=1)

text = 'Время $t$,  мс'
ax.text(1.25, -0.36, text,
        fontsize = 13)


ax.set_xticks(np.arange(0,3,0.25), minor=True)
fig.set_figheight(5)
fig.set_figwidth(8)

fig.savefig('pictures/pic4.pdf', dpi = 600)
plt.show()
