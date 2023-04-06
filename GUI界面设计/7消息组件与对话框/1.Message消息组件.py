'''
Message组件的基本使用
    Message组件主要用来展示一些短消息，它与Label组件类似，不过在文字展示方面，Message组件更灵活，其语法如下：
    参数：
    1.anchor                文本在Message组件中的位置
    2.aspect                宽/高*100%=150为默认值
    3.cursor                鼠标放置在Message组件上时的样式
    4.font                  Message组件里文字设置
    5.justify               有多行文本时，设置最后一行文本的对齐方式，值有LEFT,CENTER,RIGHT
    6.relief                设置组件的边框样式
    7.takefocus             若值为TRUE，则Message接受输入焦点(Tab)
    8.text                  Message组件中的文字，必要时可以插入换行符以获得所需的宽高比
    9.textvariable          变量StringVar()
    10.width                宽度以字符为单位

实例：
仿制聊天消息：
i=0
def mes():
    global i
    v = entry.get()
    Message(box1,text=v,bg='#CBEDE9',width=140).grid(row=i,column=0,sticky=W)
    Message(box1, text='你说：'+v, bg='#CBEDE9', width=140).grid(row=i+1, column=2)
    i+=2

from tkinter import *
win=Tk()
win.geometry('300x230')
box1=Frame(width=300,height=200)
box1.place(x=0,y=0)
box2=Frame(width=250,height=20)
box2.place(x=40,y=200)

entry = Entry(box2)
entry.pack(side=LEFT,fill=BOTH)

b=Button(box2,text='发送',command=mes).pack(side=LEFT)
win.mainloop()
mess=Message(win,text='你好',bg='#CBEDE9',takefocus=False)
mess.pack(pady=10)

Message组件的高级使用
模拟支付宝集福卡活动过程
def coll():
    mess.config(fg='red')
    a = randint(0,6)
    if a == 0:
        text='恭喜获得敬业福一张'
    elif a == 1:
        text = '恭喜获得友善福一张'
    elif a == 2:
        text = '恭喜获得爱国福一张'
    elif a == 3:
        text = '恭喜获得富强福一张'
    elif a == 4:
        text = '恭喜获得和谐福一张'
    else:
        text = '很遗憾，什么也没得到'
        mess.config(fg='#000')
    v.set('\n'+text+'\n')
    mess.pack()
from tkinter import *
from random import *
win=Tk()
win.geometry('300x230')
win.title('集福卡')
v=StringVar()
mess=Message(win,textvariable=v,font=14,aspect=350,fg='red')
Button(win,text='集福卡',command=coll).pack(side=TOP)
win.mainloop()
'''
def coll():
    mess.config(fg='red')
    a = randint(0,6)
    if a == 0:
        text='恭喜获得敬业福一张'
    elif a == 1:
        text = '恭喜获得友善福一张'
    elif a == 2:
        text = '恭喜获得爱国福一张'
    elif a == 3:
        text = '恭喜获得富强福一张'
    elif a == 4:
        text = '恭喜获得和谐福一张'
    else:
        text = '很遗憾，什么也没得到'
        mess.config(fg='#000')
    v.set('\n'+text+'\n')
    mess.pack()
from tkinter import *
from random import *
win=Tk()
win.geometry('300x230')
win.title('集福卡')
v=StringVar()
mess=Message(win,textvariable=v,font=14,aspect=350,fg='red')
Button(win,text='集福卡',command=coll).pack(side=TOP)
win.mainloop()
