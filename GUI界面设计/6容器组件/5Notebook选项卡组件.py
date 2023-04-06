'''
Notebook组件的基本使用
    Notebook选项卡组件是ttk模块提供的组件，其特点是可以显示多个选项。当用户单击选项时，下方的面板
    中就会显示对应的内容。其语法如下：
    note=Notebook(win)
    上面的语法只是创建了Notebook，其中，win是父容器，还需要通过add()方法将子组件添加到Notebook组件中。
    语法如下：
    note.add(pane,text='title')
    其中，note表示选项卡组件，pane表示向选项卡容器中添加的子组件，text为该子组件的标题，运行程序时，单击
    选项卡标题即可显示对应子组件。

实例：仿制Win7系统中设置日期和时间窗口选项卡
    众所周知，各操作系统的电脑都可以自动更新本地时间，当然用户也可以手动调整时间，接下来通过选项卡实现
    设置日期和时间的选项卡，具体代码如下：
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('日期和时间')
note=Notebook(win,width=250,height=150)         #添加选项卡容器
pane1=Frame()                                   #子选项卡的容器
Button(pane1,text='更改日期时间').pack(pady=20)   #第一个选项卡的内容
pane2=Frame()
Checkbutton(pane2,text='显示此时钟',variable=StringVar()).pack(pady=20)
pane3=Frame()
Button(pane3,text='更改设置').pack(pady=20)
note.add(pane1,text='日期和时间')
note.add(pane2,text='附加时钟')
note.add(pane3,text='Internet时间')
note.pack()
win.mainloop()

实例：实现单击游戏名称时显示游戏介绍的功能
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('游戏介绍')
note=Notebook(win,width=250,height=150)         #添加选项卡容器
pane1=Frame()                                   #子选项卡的容器
ima1=PhotoImage(file='head.png')
Label(pane1,text='脑洞大不大，一问便知',image=ima1,compound=TOP).pack()
Button(pane1,text='现在就玩').pack(pady=20)   #第一个选项卡的内容
pane2=Frame()
ima2=PhotoImage(file='pawd.png')
Label(pane2,text='抽象派还是形象派，你到底是哪一派',image=ima2,compound=TOP).pack()
Button(pane2,text='现在就玩').pack(pady=20)
note.add(pane1,text='最强的大脑')
note.add(pane2,text='水泼墨画')
note.pack()
win.mainloop()
'''
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('游戏介绍')
note=Notebook(win,width=250,height=150)         #添加选项卡容器
pane1=Frame()                                   #子选项卡的容器
ima1=PhotoImage(file='head.png')
Label(pane1,text='脑洞大不大，一问便知',image=ima1,compound=TOP).pack()
Button(pane1,text='现在就玩').pack(pady=20)   #第一个选项卡的内容
pane2=Frame()
ima2=PhotoImage(file='pawd.png')
Label(pane2,text='抽象派还是形象派，你到底是哪一派',image=ima2,compound=TOP).pack()
Button(pane2,text='现在就玩').pack(pady=20)
note.add(pane1,text='最强的大脑')
note.add(pane2,text='水泼墨画')
note.pack()
win.mainloop()