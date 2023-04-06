from tkinter import *
import random as r
num=0
num1=0
num2=0
num3=0
num4=0
def left():
    global num1,num2,num3,num4,num
    print(1111)
    print(num1,num2)
    if num1 + num2 == eval(e3.get()):
        num -= 1
        txt.config(text='爱心暴击+%s' % num)
        s.set(num)
        sz()
    else:
        num += 1
        txt.config(text='爱心暴击+%s' % num)
        s.set(num)
        sz()
    if num <= 25:
        txt.config(image=ima2)
    else:
        txt.config(image=ima1)
def right():
    global num1,num2,num3,num4,num
    if num3 + num4 == eval(e6.get()):
        num += 1
        txt.config(text='爱心暴击+%s' % num)
        s.set(num)
        sz()
    else:
        num -= 1
        txt.config(text='爱心暴击+%s' % num)
        s.set(num)
        sz()
    if num <= 25:
        txt.config(image=ima2)
    else:
        txt.config(image=ima1)
def hit():
    global num
    num = s.get()
    txt.config(text='爱心暴击+%s' % num)
    if num <= 25:
        txt.config(image=ima2)
    else:
        txt.config(image=ima1)
    sz()

def sz():
    global num1,num2,num3,num4
    num1 = r.randint(0, 100)
    num2 = r.randint(0, 100)
    num3 = r.randint(0, 100)
    num4 = r.randint(0, 100)
    e1.config(text=str(num1))
    e2.config(text=str(num2))
    e4.config(text=str(num3))
    e5.config(text=str(num4))
win=Tk()
win.title('爱心暴击')
#txt = Label(text='送TA玫瑰').pack(side='left)
ima1 = PhotoImage(file = 'head.png')
ima2 = PhotoImage(file='cry.png')
txt = Label(win,text = '爱心暴击+0',image=ima1,compound='right')
txt.grid(row=0,columnspan=16)
e1=Label(win)
e1.grid(row=1,column=0)
Label(win,text='+').grid(row=1,column=1)
e2=Label(win)
e2.grid(row=1,column=2)
Label(win,text='=').grid(row=1,column=3)
e3=Entry(win,width=4)
e3.grid(row=1,column=4)
e4=Label(win)
e4.grid(row=1,column=11)
Label(win,text='+').grid(row=1,column=12)
e5=Label(win)
e5.grid(row=1,column=13)
Label(win,text='=').grid(row=1,column=14)
e6=Entry(win,width=4)
e6.grid(row=1,column=15)
b1 = Button(win,text='提交1',command=left,width=4).grid(row=1,column=5)
s = Scale(win,from_=0,to=50,resolution=1,orient=HORIZONTAL,showvalue=0,command=hit,troughcolor='green')
s.grid(row=1,column=6,columnspan=5)
b2 = Button(win,text='提交2',command=right,width=4).grid(row=1,column=16)
Button(win,text='开始',command=hit).grid(row=2,column=6,columnspan=5)
win.mainloop()