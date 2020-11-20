import matplotlib.pyplot as plt
import numpy as np
import math
import turtle

MODEL_DT = 0.01
g = 9.81

#-------------------------------------------------------
class Body:
    def __init__(self, alpha, L):
        self.alpha = alpha * math.pi/180 # перевод градусов в радианы
        self.L = L
        self.s = self.alpha * self.L
        self.V = 0
        self.trajectory = []
        self.trajectory_x = []
        self.trajectory_y = []
        
        
    def advance(self):
        self.trajectory.append(self.s)
        
        self.s += self.V * MODEL_DT
        self.alpha = self.s/self.L
        self.a = -g * np.sin(self.alpha)
        self.V += self.a * MODEL_DT

        
#-------------------------------------------------------
class Ball(Body):
    def __init__(self, alpha, L, b):
        super().__init__(alpha, L)
        self.b = b # коэффициент сопротевления
    
    def advance(self):
        self.trajectory.append(self.s)
        
        self.s += self.V * MODEL_DT
        self.alpha = self.s/self.L
        self.a = -g * np.sin(self.alpha) - self.V * self.b # F(сопр.)=-b*V
        self.V += self.a * MODEL_DT
#--------------------------------------------------------
ball = Ball(90,1,0.2)

T = 10
for t in np.r_[0:T:MODEL_DT]:
    ball.advance()

#-------------------------------------------------------
# Это перевод из "s"-системы в обычну декартовую систему координат
for i in ball.trajectory:
    ball.trajectory_x.append(np.sin(i/ball.L))
    ball.trajectory_y.append(ball.L - np.cos(i/ball.L))

#-------------------------------------------------------
    # Анимация маятника с помощью библиотеки turtle
turtle.tracer(0,0) # выключить обновление экрана после каждого шага
turtle.speed(0)    # максимальная скорость
turtle.hideturtle()# удалить саму черепашку
turtle.penup()
turtle.width(2)

for i in range(len(np.r_[0:T:MODEL_DT])):
    x = 300 * ball.trajectory_x[i]
    y = 300 * ball.trajectory_y[i]
    turtle.goto(x,y)
    turtle.dot(12)
    turtle.pendown()
    turtle.goto(0,300)
    turtle.goto(10,300)
    turtle.goto(-10,300)
    turtle.penup()
    turtle.update() 
    turtle.clear()

    
