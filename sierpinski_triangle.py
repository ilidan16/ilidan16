# Триугольник Серпинского
import turtle as t
import math
import random

t.penup()
t.speed(0)
t.tracer(1000,0)
t.hideturtle()
t.bgcolor("black")

A = [-300,-170]
B = [150,320]
C = [300,-170]
O = [0,0]

t.goto(O[0],O[1])

for i in range(10000):
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

