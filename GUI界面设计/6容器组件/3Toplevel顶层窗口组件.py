'''
Toplevel顶层窗口组件的基本使用
    Toplevel可以弹出一个窗口，而这个窗口显示在父窗口的上层，当父窗口被关闭时，Toplevel窗口也会被关闭，但是Toplevel关闭不影响父窗口。
    win2=Toplevel()

实例：
def creat():
    top=Toplevel()
    top.geometry('150x150')
    top.title('创建顶层窗口')
    top.configure(bg='green')
    Label(top,text='这是Toplevel组件窗口').pack()
from tkinter import *
win1=Tk()
win1.geometry('200x200')
win1.configure(bg='pink')
Button(win1,text='创建顶层窗口',command=creat).pack()
win1.mainloop()

Toplevel组件的高级使用
通过Toplevel组件实现窗口会话框。
实例：模拟游戏中玩家匹配房间及提醒玩家准备功能
很多多人互动游戏都是将多个玩家匹配到一个'房间'，当这个'房间'里的所有玩家进入准备状态后，游戏才能开始。
下面实现窗口会话框，模拟玩家匹配房间以及提醒玩家准备功能。具体代码如下：
'''
def begin():
    top=Toplevel()
    top.geometry('200x120')
    top.title('准备游戏')
    top.configure(bg='pink')
    Label(top,text='玩家准备就绪，请准备！',font=14,bg='pink').pack(pady=50)
    time.sleep(2)
    print(top.keys())

def change():
    top=Toplevel()
    top.geometry('200x120')
    top.title('2号棋牌室')
    top.configure(bg='pink')
    Label(top, text='欢迎来到2号棋牌室', font=14,bg='pink').pack(pady=10)
    Label(top,text='玩家准备就绪，请准备！',font=16,bg='pink').pack(pady=20)
from tkinter import *
import time
win1=Tk()
win1.geometry('270x220')
win1.title('1号棋牌室')
win1.configure(bg='pink')
l1=Label(win1,text='欢迎进入1号棋牌室',background='yellow',font=14,width=35)
l1.grid(row=0,column=0,columnspan=5,ipady=8)
b1=Button(win1,text='开始对局',background='blue',command=begin)
b1.grid(row=2,column=1,pady=10)
b2=Button(win1,text='更换房间',background='red',command=change)
b2.grid(row=2,column=3,pady=10)
win1.mainloop()