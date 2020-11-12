# Снежинка Коха
import turtle

turtle.setup(1440,900)
turtle.speed(0)
turtle.tracer(50,0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.color("blue")

LENGTH = 200 # длина стороны прав. многоугольника
k = 5  #количество итераций в кривой Коха
n = 6  # количесвто сторон прав. n-угольника
inside = True # True - рисовать кривую Коха внутри многоугольника
              # False - рисовать снаружи
x = 0         # начальные координаты
y = -300
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
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
if inside:
    for _ in range(n):
        koch_curve(LENGTH, k)
        turtle.left(360/n)
else:
    turtle.left(180*(n-2)/n)
    for _ in range(n):
        koch_curve(LENGTH, k)
        turtle.right(360/n)





    
    

