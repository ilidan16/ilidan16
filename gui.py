import tkinter as tk
import semester_1.primality_test as test
import time

def clicked():
    z = int(enter.get())
    t0 = time.time()
    result = test.primality_test_2_0(z)
    t = time.time() - t0
    if result:
        lbl1.configure(text="Простое")
    else:
        lbl1.configure(text="Не простое")
    lbl2.configure(text=str(round(t, 5)))

window = tk.Tk()
window.geometry('500x300')
window.title("Проверка на простоту")

lbl1 = tk.Label(window, text="")  
lbl1.grid(column=0, row=1)

lbl2 = tk.Label(window, text="")  
lbl2.grid(column=0, row=10)  

enter = tk.Entry(window, width=10)
enter.focus()
enter.grid(column=0, row=0)

btn = tk.Button(window, text="Ввод", command=clicked)
btn.grid(column=1, row=0) 

window.mainloop()