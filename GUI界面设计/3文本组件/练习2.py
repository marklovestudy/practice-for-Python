from tkinter import *
win=Tk()
def pd():
    if eval(v.get()) < 50:
        l1.config(image=ima2)
    else:
        l1.config(image=ima3)
def pp(e):
    print(v.get())
def reduce():
    v.set(eval(v.get())-1)
    pd()
def add():
    v.set(eval(v.get())+1)
    pd()
ima1=PhotoImage(file='ok.png')
ima2=PhotoImage(file='cry.png')
ima3=PhotoImage(file='smile.png')
l1=Label(win,image=ima1);l1.grid(row=0,columnspan=3)
Button(win,text='-',command=reduce).grid(row=1,column=0)
v=StringVar();v.set(50)
s=Scale(win,from_=0,to=100,orient=HORIZONTAL,command=pp,variable=v)
s.grid(row=1,column=1)
Button(win,text='+',command=add).grid(row=1,column=2)
win.mainloop()