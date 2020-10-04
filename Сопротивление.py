#           Лабораторная работа №1
#гистограмма и график нормального распределения
#результатов измеререния сопротивления резисторов
import matplotlib.pyplot as plt
import numpy as np
import math
g = 0.682
a = 388.388
y = lambda x: (1/(math.sqrt(2*math.pi)*g))*np.exp(-(x-a)**2/(2*g**2))
plt.xlabel('Сопротивление (Ом)')
plt.ylabel('Плотность вероятности, с$^{-1}$')
plt.text(386.5,0.55,'$\sigma=0.682$ (Ом)')
plt.text(386.37,0.5,'$<R>=388.4 (Ом)$')
x = np.linspace(386.5,390.2,100)
plt.plot(x,y(x),color='red')
a = []
a.append(388)
a.append(388)
a.append(388.1)
a.append(388.9)
a.append(387.3)
a.append(390.2)
a.append(387.8)
a.append(389.5)
a.append(389.6)
a.append(388.8)
a.append(388.1)
a.append(388.8)
a.append(389.4)
a.append(389.4)
a.append(389)
a.append(387.9)
a.append(388.6)
a.append(387.7)
a.append(387.5)
a.append(388.3)
a.append(388.3)
a.append(388.6)
a.append(388.2)
a.append(387.5)
a.append(389.4)
a.append(387.5)
a.append(389.1)
a.append(388.6)
a.append(389.3)
a.append(388.1)
a.append(388.4)
a.append(387.3)
a.append(387.8)
a.append(388.5)
a.append(387.6)
a.append(388.3)
a.append(388.2)
a.append(387.9)
a.append(388.5)
a.append(389)
a.append(388.4)
a.append(387.9)
a.append(388.9)
a.append(388.7)
a.append(387.6)
a.append(387.2)
a.append(387.9)
a.append(388)
a.append(388.6)
a.append(389.2)
hist = np.histogram(a,bins=7,density=True)[0]
plt.bar([387.41,387.84,388.27,388.7,389.13,389.56,390],hist,width=0.148,color='black')
plt.show()
