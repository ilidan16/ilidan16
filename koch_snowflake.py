# Снежинка Коха
import turtle

turtle.speed(0)
turtle.tracer(10,0)
turtle.hideturtle()
turtle.penup()
turtle.goto(-300,-170)
turtle.pendown()
turtle.bgcolor("black")
turtle.color("blue")

LENGTH = 600 # длина стороны прав. треугольника
n = 5  #количество итераций 
#===========================================
# Кривая Коха
def koch_curve(LENGTH, n):
    if n == 0:
        turtle.forward(LENGTH)
    else:
        koch_curve(LENGTH / 3, n - 1)
        turtle.left(60)
        koch_curve(LENGTH / 3, n - 1)
        turtle.left(240)
        koch_curve(LENGTH / 3, n - 1)
        turtle.left(60)
        koch_curve(LENGTH / 3, n - 1)
        
#===========================================
turtle.left(60)
koch_curve(LENGTH, n)
turtle.left(240)
koch_curve(LENGTH, n)
turtle.left(240)
koch_curve(LENGTH, n)






    
    

