import tkinter as tk
import semester_1.primality_test as test

def clicked():
    z = enter.get()
    text = test.primality_test_2_0(z)
    lbl.configure(text=str(text))

window = tk.Tk()
window.geometry('500x300')
window.title(":)")
enter = tk.Entry(window, width=10)
#enter.focus()
enter.grid(column=2, row=0)
btn = tk.Button(window, text="Ввод", command=clicked)
btn.grid(column=10, row=10)
lbl = tk.Label(window, text="Привет")  
lbl.grid(column=0, row=0) 
window.mainloop()