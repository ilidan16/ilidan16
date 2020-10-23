import math
import numpy as np
import matplotlib.pyplot as plt

a = -math.pi         # начало графика
b = math.pi          # конец
c = 0.01         # шаг
def f(x):
    x = math.sin(x)   # f(x)
    return(x)

x = list(np.r_[a:b:c])                              
y = []
for i in x:            
    y.append(f(i))    
plt.plot(x,y,color='black')
plt.show()     
