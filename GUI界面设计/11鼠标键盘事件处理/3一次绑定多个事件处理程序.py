'''
bind()方法，参数：绑定的鼠标事件要有参数event，因为有返回值
    1.add           add=''是默认值，表示当前绑定的事件处理程序将替代与该组件相关联的其他事件处理程序。
                    如果add='+',表示将此处理程序添加到此事件类型的函数列表中。

实例      add='+'时可以同时运形bg和font,add=''时，只运形后面的font，前面的bg不运形
def fg1():
    b.config(fg='red')

def bg(e):
    b.config(bg='blue')

def font(e):
    b.config(font=14)
from tkinter import *
win=Tk()
b = Button(win,text='按钮',command=fg1)
b.bind('<Button-1>',bg,add='+')
b.bind('<Button-1>',font,add='+')
b.pack(pady=10)
win.mainloop()

实例：为多个Label组件一键添加颜色
一键换色时，改变奇数个和偶数个的颜色。
def col():
    arr=list('0123456789ABCDEF')
    #为保证颜色相近，color1+color2多数方块的颜色，color1+color3为A方块的颜色
    c = '#'
    for i in range(6):
        c += arr[random.randint(0,15)]
    return c

def color1():
    a=col()
    for i in box1:
        i.config(bg=a)

def color2(event):
    a=col()
    for i in box2:
        i.config(bg=a)
#通过循环添加多个Label，并且按照其位置奇数和偶数存储在两个数组中，便于添加颜色。并用command,bind方法分别按钮绑定事件。
from tkinter import *
import random
win=Tk()
win.geometry('330x200')
box1=[]
box2=[]
for i in range(8):
    for j in range(2):
        label = Label(win,width=5,height=1,relief='groove')
        label.grid(row=j,column=i)
        if (i+j)%2==0:
            box1.append(label)
        else:
            box2.append(label)
b = Button(win,text='一键着色',command=color1)
b.bind('<Button-1>',color2,add='+')
b.grid(row=2,column=0,columnspan=8)
win.mainloop()
'''
def col():
    arr=list('0123456789ABCDEF')
    #为保证颜色相近，color1+color2多数方块的颜色，color1+color3为A方块的颜色
    c = '#'
    for i in range(6):
        c += arr[random.randint(0,15)]
    return c

def color1():
    a=col()
    for i in box1:
        i.config(bg=a)

def color2(event):
    a=col()
    for i in box2:
        i.config(bg=a)
#通过循环添加多个Label，并且按照其位置奇数和偶数存储在两个数组中，便于添加颜色。并用command,bind方法分别按钮绑定事件。
from tkinter import *
import random
win=Tk()
win.geometry('330x200')
box1=[]
box2=[]
for i in range(8):
    for j in range(2):
        label = Label(win,width=5,height=1,relief='groove')
        label.grid(row=j,column=i)
        if (i+j)%2==0:
            box1.append(label)
        else:
            box2.append(label)
b = Button(win,text='一键着色',command=color1)
b.bind('<Button-1>',color2,add='+')
b.grid(row=2,column=0,columnspan=8)
win.mainloop()