def mess(n):
    showinfo('welcome','好久不见，欢迎回归')
    print(n)
def aa(n):
    F=Frame()
    Button(F,text="打开游戏%s"%n,command=lambda :mess(n)).pack(padx=20,pady=20)
    nt.add(F,text='儿子%s'%n)
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
win=Tk()
nt=Notebook(win)
nt.pack()
for i in range(1,9):
    aa(i)
win.mainloop()