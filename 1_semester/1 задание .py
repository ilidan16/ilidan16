
import math
import numpy as np #установка библиотек math, numpy, matplotlib
import matplotlib.pyplot as mpp

# Эта программа рисует фигуры Лиссажу

if __name__=='__main__':
    x = []                                #Создание массива x, в котором
    for i in np.r_[0:10:0.01]:            #лежат значения косинуса с
        x.append(np.cos(3*math.pi*i+2.35))#определённой угловой скоростью и начальной фазой
    y = []
    for i in np.r_[0:10:0.01]:            #Аналогичное создание массива y, 
        y.append(np.cos(2*math.pi*i))     #только с другой угловой скоростью и нач. фазой
    mpp.plot(x,y,color='black')           #Создание графика чёрного цвета
    mpp.show()                            #Показать график
