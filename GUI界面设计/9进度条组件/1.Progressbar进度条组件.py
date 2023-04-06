'''
Progressbar进度条组件，是ttk组件中的模块，用于显示当前任务的执行进度。其语法如下:
Progressbar(win,option)
相关参数如下：
    1.orient            设置进度条水平显示或垂直显示，可选的值有horizontal(水平)、vertical(垂直)
    2.length            指定进度条的长度(若进度条垂直显示，则指定进度条的高度)
    3.mode              进度条加载动画的模式，可选的值有“determinate”(指针从起点移动到终点后，在此从起
                        点开始移动，默认值)和“indeterminate”(指针在起点与终点间来回滚动)
    4.maximum           指定进度条的最大值，默认值为100
    5.value             进度条的当前值。当mode="determinate"时，value表示已完成的工作量:
                        若mode="indeterminate"，当value="maximum”时，指针在进度条最右侧
    6.variable          为进度条的值绑定一个变量，当变量的值发生变化时，进度条值也会发生改变

实例：在窗口中添加进度条，具体代码如下：
from tkinter import *
from tkinter.ttk import *
win=Tk()
Progressbar(win,value=50).pack(pady=10)
win.mainloop()

实例：模拟小猫进食游戏
在小猫进食游戏中，每点一次大鱼或小鱼，猫则投食一次。大鱼增加2点饱腹度，小鱼为1，当最大饱腹度到50时，小猫就吃饱了。再喂也不会增加饱腹感。
def add1(c):
    global val
    val += c
    if val > pro['max']:
        v.set('我吃饱了')
    else:
        v1.set(val)
from tkinter import *
from tkinter.ttk import *
win=Tk()
Label(win,text='投食：').grid(row=0,column=0,pady=10)
Button(win,text='大鱼',command=lambda :add1(2)).grid(row=0,column=1,pady=10)
Button(win,text='小鱼',command=lambda :add1(1)).grid(row=0,column=2,pady=10)
ima1=PhotoImage(file='cat.png')
v = StringVar()
v.set('我饿了')
l=Label(win,image=ima1,compound=TOP,textvariable=v)
l.grid(row=1,column=1,pady=10)
v1=IntVar()
val=0
v1.set(val)
pro=Progressbar(win,variable=v1,max=50)
pro.grid(row=3,columnspan=3,sticky=W+E,pady=10)
win.mainloop()

Progressbar组件的相关方法
    1.start(interval=None):     开始自动递增模式，每隔interval时间，就调用一次step(amount=None)方法.interval的默认值为50毫秒。
    2.step(amount=None):        设置进度条递增的步进值，默认值amount为1.0。
    3.stop():                   停止start(interval)的运行。

实例：
模拟加载游戏的进度条，当单击'进入游戏'或者'游戏加速'按钮时，进度条加载动画，单击'停止加载'按钮时，动画停止。
def rego():
    pro.stop()
    pro.step(amount=5)
    pro.start()
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('灵魂画师')
ima1=PhotoImage(file='draw.png')
l=Label(win,image=ima1,text='灵魂画师',compound=BOTTOM,font=('华文新魏',18),foreground='red')
l.grid(row=0,column=1,padx=20,pady=10)
v1=IntVar()
val=0
v1.set(val)
pro=Progressbar(win,value=0,max=100,mode='determinate',length=200)
pro.grid(row=1,columnspan=3,pady=10)
Button(win,text='进入游戏',command=pro.start).grid(row=2,column=0,pady=10)
Button(win,text='游戏加速',command=rego).grid(row=2,column=1,pady=10)
Button(win,text='停止游戏',command=pro.stop).grid(row=2,column=2,pady=10)

win.mainloop()
'''

def rego():
    pro.stop()
    pro.step(amount=5)
    pro.start()
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('灵魂画师')
ima1=PhotoImage(file='draw.png')
l=Label(win,image=ima1,text='灵魂画师',compound=BOTTOM,font=('华文新魏',18),foreground='red')
l.grid(row=0,column=1,padx=20,pady=10)
v1=IntVar()
val=0
v1.set(val)
pro=Progressbar(win,value=0,max=100,mode='determinate',length=200)
pro.grid(row=1,columnspan=3,pady=10)
Button(win,text='进入游戏',command=pro.start).grid(row=2,column=0,pady=10)
Button(win,text='游戏加速',command=rego).grid(row=2,column=1,pady=10)
Button(win,text='停止游戏',command=pro.stop).grid(row=2,column=2,pady=10)

win.mainloop()