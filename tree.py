#Красивое дерево
"""Источники информации и вдохновения:
    wikipedia.org. L-система
    https://www.youtube.com/watch?v=5duGAaHdoE0
    https://www.youtube.com/watch?v=mAz46Z5curo&t=175s"""

"""L - система. Дерево Пифагора.
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
]: выбери из стека положение и угол, поверни вправо"""

import turtle as t
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
                str_new += "11"
            if ch == "[":           # константы не трогаем
                str_new += "["
            if ch == "]":
                str_new += "]"
        
        str_current = str_new
        str_new = ""

    return str_current
#============================================================
t.speed(0)
t.tracer(0,0)
t.penup()
t.goto(0, -200)
t.pendown()

iterations = 5
alpha = 30
length = 10
def draw_tree():
    t.setheading(90)
    """Будем записывать значения в массив,
а затем использовать последний элемент и
сразу удалять его"""
    x = []
    y = []
    angle = []
    for ch in create_string_of_functions(iterations):
        if ch == "1":
            t.forward(length)
        if ch == "0":
            t.pencolor("green")
            t.forward(length)
            t.pencolor("black")
        if ch == "[":
            x.append(t.xcor()) 
            y.append(t.ycor()) 
            angle.append(t.heading()) 
            t.left(alpha)
        if ch == "]":
            t.penup()
            t.goto(x.pop(), y.pop())
            t.pendown()
            t.setheading(angle.pop())
            t.right(alpha)
#============================================================
draw_tree()
print (create_string_of_functions(iterations))


            
            
            
        
        

    
