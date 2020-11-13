#Красивое дерево
"""Источники информации и вдохновения:
    wikipedia.org. L-система
    https://www.youtube.com/watch?v=5duGAaHdoE0
    https://www.youtube.com/watch?v=mAz46Z5curo&t=175s"""

"""L - система. Дерево Пифагора.
* переменные: 0, 1, 2
* константы: [, ], 2
* аксиома: 0
* правила:
    1. 1 -> 21
    2. 0 -> 1[0]0
Команды для черепашки:
0: рисуй отрезок, кончающийся листом
1: рисуй отрезок
2: тоже рисует отрезок как 1, но является константой
[: положи в стек положение и угол рисования, поверни влево
]: выбери из стека положение и угол, поверни вправо

2 была добавлена, чтобы при увелечении
количества итераций длина отрезка
увеличивалась не в два раза, а увеличивалась на одну единицу"""

import turtle as t
import random
#============================================================
"""Данная функция создаёт строку функций (команд),
по которым потом черепашка будет рисовать дерево"""
def create_string_of_functions(iterations):
    str_current = "0" # аксиома
    str_new = ""
    for _ in range(iterations):
        for ch in str_current:
            if ch == "0":           # 2-ое правило
                str_new += "1[0]0"
            if ch == "1":           # 1-ое правило
                str_new += "21"
            if ch == "2":           # # константы не трогаем
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
t.width(0)
t.penup()
t.goto(0, -300)
t.pendown()

iterations = 11
alpha = 20
length = 10
width_0 = 16 #начальная толщина
def draw_tree():
    t.setheading(90)
    """Будем записывать значения в массив,
а затем использовать последний элемент и
сразу удалять его"""
    x = []
    y = []
    angle = []
    width = []
    for ch in create_string_of_functions(iterations):
        if ch == "1":
            t.forward(length)

        """Команду 2 будем выполнять с некоторой вероятностью"""
        if ch == "2" and random.randint(0,100) > 40:
            t.forward(length)
            
        if ch == "0":
            t.pencolor("green")
            t.forward(length)
            t.pencolor("black")
            
        if ch == "[":
            x.append(t.xcor()) 
            y.append(t.ycor()) 
            angle.append(t.heading()) 
            t.left(alpha + random.randint(-13, 13))
            
        if ch == "]":
            t.penup()
            t.goto(x.pop(), y.pop())
            t.pendown()
            t.setheading(angle.pop())
            t.right(alpha + random.randint(-13, 13))
#============================================================
draw_tree()
print (create_string_of_functions(iterations))


            
            
            
        
        

    
