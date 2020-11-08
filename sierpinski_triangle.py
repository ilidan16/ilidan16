# Триугольник Серпинского
import turtle as t
import math
import random

t.penup()         # поднять перо черепашки
t.speed(0)        # максимальная скорость черепашки
t.tracer(500,0)   # обновление экрана каждые 500 шагов
t.hideturtle()    # убрать саму черепашку
t.bgcolor("black")# чёрный фон

A = [-300,-170]   # координаты вершин триугольнака
B = [150,320]
C = [300,-170]
O = [0,0]         # начальная точка черепашки

t.goto(O[0],O[1])

for _ in range(7000):
    x = t.xcor()
    y = t.ycor()
    r = random.randint(1,3)
    
    if r == 1:
        t.goto((x+A[0])/2, (y+A[1])/2)
        t.dot(2,"red")
        
    if r == 2:
        t.goto((x+B[0])/2, (y+B[1])/2)
        t.dot(2,"blue")
        
    if r == 3:
        t.goto((x+C[0])/2, (y+C[1])/2)
        t.dot(2,"green")
