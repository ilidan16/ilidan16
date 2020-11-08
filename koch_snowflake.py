# Снежинка Коха
import turtle

turtle.speed(0)
turtle.setup(width=1440, height=900)
turtle.penup()
turtle.goto(-300,-170)
turtle.pendown()

LENGTH = 600 # длина стороны прав. треугольника
n = 6  #количество итераций 
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






    
    

