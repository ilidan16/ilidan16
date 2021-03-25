# Папоротник Барнсли
import turtle as tl
import random

tl.tracer(1000,0)
tl.penup()
tl.hideturtle()
tl.bgcolor("black")


zoom = 1.5
x = 0
y = 0
tl.goto(x,y)

for _ in range(20000):
    tl.goto(zoom*65 * x, zoom*37 * y - 252)
    tl.dot(2,"green")
    r = random.randint(1,100)
    x_current = x
    y_current = y
    
    if r == 1: # данное преобразование выполняется
        x = 0  # с вероятностью 1%
        y = 0.16*y_current
        
    if r > 1 and r <= 86: # с вероятностью 85%
        x = 0.85*x_current + 0.04*y_current
        y = -0.04*x_current + 0.85*y_current + 1.6
        
    if r > 86 and r <= 93:# с вероятностью 7%
        x = 0.2*x_current - 0.26*y_current
        y = 0.23*x_current + 0.22*y_current + 1.6
        
    if r > 93 and r <= 100:# с вероятностью 7%
        x = -0.15*x_current + 0.28*y_current
        y = 0.26*x_current + 0.24*y_current + 0.44
    

