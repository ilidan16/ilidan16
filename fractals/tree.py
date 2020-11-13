#Красивое дерево
"""Источники информации и вдохновения:
    wikipedia.org. L-система
    https://www.youtube.com/watch?v=5duGAaHdoE0
    https://www.youtube.com/watch?v=mAz46Z5curo&t=175s"""

"""L - система. Дерево Пифагора.
(Эти правила описывают борщевик, который мы рисовали в классе)
* переменные: 0, 1
* константы: [, ]
* аксиома: 0
* правила:
    1. 1 -> 11
    2. 0 -> 1[0]0
Команды для черепашки:
0: рисуй отрезок, кончающийся листом
1: рисуй отрезок
[: положи в стек положение и угол рисования, поверни влево
]: выбери из стека положение и угол, поверни вправо

Однака правила будут немного отличаться:
    1. 1 -> 21
    2. 0 -> 1[20]20
2 - это то же самое что и 1, но при отображение она не изменяется (2 -> 2)
Это даст следующие эффекты:
1) Длина отрезка будет увеличиваться не в два раза, а всего на одну еденицу
2) Функция 2 (как и 1) будет игнорироваться с определённой вероятностью,
в итоге длина листьев будет разной"""

import turtle as t
import random
import time
#============================================================
"""Данная функция создаёт строку функций (команд),
по которым потом черепашка будет рисовать дерево"""
def create_string_of_functions(iterations):
    str_current = "22220" # аксиома
    str_new = ""
    for _ in range(iterations):
        for ch in str_current:
            if ch == "0":           # 2-ое правило 
                str_new += "1[20]20" 
            if ch == "1":           # 1-ое правило
                str_new += "21"
            if ch == "2":           # константы не трогаем
                str_new += "2"
            if ch == "[":           
                str_new += "["
            if ch == "]":
                str_new += "]"
        
        str_current = str_new
        str_new = ""

    return str_current
#============================================================
t.setup(1440, 900)
t.hideturtle()
t.speed(0)
t.tracer(0,0)
t.penup()
t.goto(0, -350)
t.pendown()

iterations = 12
alpha = 14
length = 10

def draw_tree():
    t.setheading(90)
    thickness = 16 #начальная толщина
    t.pensize(thickness)
    """Будем записывать значения в массив,
а затем использовать последний элемент и
сразу удалять его"""
    x = []
    y = []
    angle = []
    array_thickness = []
    for ch in create_string_of_functions(iterations):
        if ch == "1" """and random.randint(0,100) > 40""":    # стебель
            t.forward(length)

        if ch == "2" and random.randint(0,100) > 40:
            t.forward(length)
            
        if ch == "0":                                   # лист
            array_thickness.append(t.pensize())
            t.pensize(4)
            r = random.randint(1,3)
            if r == 1:
                t.pencolor("#009900")
            if r == 2:
                t.pencolor("#667900")
            if r == 3:
                t.pencolor("#20BB00")
            t.forward(length - 2)
            t.pensize(array_thickness.pop())
            t.pencolor("black")
            
        if ch == "[":                       # запоминаем данные перед поворотом налево
            thickness = thickness * 3/4  
            t.pensize(thickness)
            array_thickness.append(thickness)
            x.append(t.xcor()) 
            y.append(t.ycor()) 
            angle.append(t.heading())
            t.left(alpha + random.randint(-13, 13))
            
        if ch == "]":                       #возвращаем данные и поворачиваем направо
            t.penup()
            t.goto(x.pop(), y.pop())
            t.pendown()
            thickness = array_thickness.pop()
            t.pensize(thickness)
            t.setheading(angle.pop())
            t.right(alpha + random.randint(-13, 13))
#============================================================
for _ in range(10):
    draw_tree()
    t.update()
    t.clear()
    t.penup()
    t.goto(0,-350)
    t.pendown()
    time.sleep(2)


            
            
            
        
        

    
