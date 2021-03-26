import tkinter as tk
import time
import semester_1.primality_test as test

def clicked():
    z = int(enter.get())
    if z == 1:
        lbl1.configure(text="error")
        return
    lbl1.configure(text="loading...")
    window.update()
    t0 = time.time()
    result = test.primality_test_2_0(z)
    t = time.time() - t0
    time.sleep(1) #чтобы немного повисела надпись loading
    if result:
        lbl1.configure(text="Да")
    else:
        lbl1.configure(text="Нет")
    lbl2.configure(text=str(round(t, 5)))
    window.update()


window = tk.Tk()
window.geometry('200x110')
window.title("Проверка на простоту")

lbl0 = tk.Label(window, text="Число простое?")  
lbl0.grid(column=0, row=0)

lbl1 = tk.Label(window, text="") # для вывода результата 
lbl1.grid(column=0, row=2)

lbl2 = tk.Label(window, text="")  # для вывода затраченного времени
lbl2.grid(column=1, row=3) 

lbl3 = tk.Label(window, text="Затраченное время:")  
lbl3.grid(column=0, row=3)   

enter = tk.Entry(window, width=10)
enter.focus()
enter.grid(column=0, row=1)

btn = tk.Button(window, text="Ввод", command=clicked)
btn.grid(column=1, row=1) 

window.mainloop()