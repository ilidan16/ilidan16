import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = np.linspace(-10, 10, 200)
y = 0.01*(x + 9)*(x + 6)*(x - 6)*(x - 9)*x

fig, ax = plt.subplots()

ax.plot(x, y, color = 'r', linewidth = 3)

#  Устанавливаем интервал основных и
#  вспомогательных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(10))


#  Добавляем линии основной сетки:
ax.grid(which='major',
        color = 'k')

#  Включаем видимость вспомогательных делений:
ax.minorticks_on()
#  Теперь можем отдельно задавать внешний вид
#  вспомогательной сетки:
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figwidth(12)
fig.set_figheight(8)

plt.show()                     
