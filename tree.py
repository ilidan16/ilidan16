import turtle as t

"""L - система. Дерево Пифагора.
* переменные: 0, 1
* константы: [, ]
* аксиома: 0
* правила: (1 -> 11), (0 -> 1[0]0)
Команды для черепашки:
0: рисуй отрезок, кончающийся листом
1: рисуй отрезок
[: положи в стек положение и угол рисования, поверни влево
]: выбери из стека положение и угол, поверни вправо"""

#============================================================
# Данная функция создаёт строку функций (команд),
# по которым потом черепашка будет рисовать деревья
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
iterations = 3
alpha = 30
length = 50
def draw_tree():
    for ch in create_string_of_functions(iterations):
        if ch == "1":
            t.forward(length)
        if ch == "0":
            t.pencolor("green")
            t.forward(length)
            t.pencolor("black")
        if ch == "[":
            x = xcor()
            y = ycor()
            t.setheading(-alpha) # повернуть на лево
        if ch == "]":
            
            
            
            
            
        
        

    
