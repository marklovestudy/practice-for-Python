"""
Scale基本使用
    Scale(win,from_=0,to=50,resolution=1,orient=HORIZONTAL)
    resolution（决定，决心，解决，分辨率，）设置更改的数值，orient确定方向：水平HORIZONTAL垂直VERTICAL

Scale参数：
    1.resolution                （决定，决心，解决，分辨率，）设置更改的数值
    2.orient                    确定方向：水平HORIZONTAL垂直VERTICAL
    3.activebackground          鼠标悬停在滑块上时，尺度条的背景颜色
    4.command                   当Scale的数值变化时，执行某函数
    5.digits                    尺度数值
    6.label                     标签文字如果进度条是水平显示，则标签显示在其左上角；若进度条是垂直显示，则标签显示在右上角
    7.length                    长度像素。
    8.repeatdelay               按住滑块多久后可以拖动滑块。
    9.showvalue                 是否显示尺度的数值，默认为显示，若值为0，则不显示
    10.tickinterval             尺度条每单元长度的数值
    11.troughcolor               刻度尺的颜色
    12.variable                 设置或获取目前刻度尺的数值

1.resolution（决定，决心，解决，分辨率，）设置更改的数值，
2.orient确定方向：水平HORIZONTAL垂直VERTICAL
3.activebackground          鼠标悬停在滑块上时，尺度条的背景颜色
4.command                   当Scale的数值变化时，执行某函数
实例：添加1-15的水平Scale组件
from tkinter import *
win=Tk()
def aa(e):
    print(123)
Scale(win,from_=0,to=15,resolution=1,orient=HORIZONTAL,activebackground='red',command = aa).pack()
win.mainloop()

5.digits                    尺度数值
6.label                     标签文字如果进度条是水平显示，则标签显示在其左上角；若进度条是垂直显示，则标签显示在右上角
7.length                    长度像素。
8.repeatdelay               按住滑块多久后可以拖动滑块。
from tkinter import *
win=Tk()
def aa(e):
    print(123)
Scale(win,from_=1,to=15,resolution=1,orient=HORIZONTAL,digits=4,label='date',length = 200,repeatdelay=1000).pack()
win.mainloop()

9.showvalue                 是否显示尺度的数值，默认为显示，若值为0，则不显示
10.tickinterval             尺度条每单元长度的数值
11.troughcolor               刻度尺的颜色
12.variable                 设置或获取目前刻度尺的数值

from tkinter import *
win=Tk()
def aa(e):
    print(v.get())
v = StringVar()
Scale(win,from_=1,to=15,resolution=1,orient=HORIZONTAL,showvalue=1,tickinterval=10,troughcolor ='red',variable=v,command=aa).pack()
win.mainloop()

Scale组件的常用方法：
    1.coords([value])           设置或获取滑块位置相对Scale组件左上角的坐标。若value值为空，则获取滑块所在位置相对Scale组件左上角坐标；
                                反之，则设置滑块所在位置相对Scale组件左上角的坐标，如coords([2])返回第二个左上位置的坐标
    2.get():                    获得当前滑块的值。tkinter模块尽可能地返回一个整形值，否则返回一个浮点型值。
    3.identify(x,y)             判断与滑块的位置关系：返回指定位置下的Scale组件的部件，其可能的值有'slider'(滑块)，
                                'trough1'(左侧或上侧的凹槽)，'trough2'(右侧或下侧的凹槽)以及''(表示什么都没有)。
    4.set(value)                设置Scale组件的值(滑块的位置)。
实例1：
from tkinter import *
win=Tk()
def aa(e):
    print(s.coords(2))
    print(v.get())
    print(1,s.identify(0,0))            #不在滑块上
    print(2, s.identify(19,32))         #在滑块上
    print(3, s.identify(72,32))         #在右侧或下侧
    s.set(5)                            #设置Scale组件的值(滑块的位置)。
v = StringVar()
s = Scale(win,from_=1,to=15,resolution=1,orient=HORIZONTAL,variable=v,command=aa)
s.pack()

win.mainloop()

实例：通过滑块和左右按钮实现爱心暴击

from tkinter import *
num=0
def up1():
    global num
    if s.get()<50:
        num += 1
        txt.config(text = '爱心暴击+%s'%num)
        s.set(num)

def down1():
    global num
    if s.get()>0:
        num -= 1
        txt.config(text='爱心暴击+%s' % num)
        s.set(num)

def hit(e):
    global num
    num = s.get()
    txt.config(text='爱心暴击+%s' % num)

win=Tk()
win.title('爱心暴击')
#txt = Label(text='送TA玫瑰').pack(side='left)
txt = Label(text = '爱心暴击+0')
txt.pack(side=TOP)
b1 = Button(win,text='-',command=down1,width=2).pack(side='left')
s = Scale(win,from_=0,to=50,resolution=1,orient=HORIZONTAL,showvalue=0,command=hit,troughcolor='green')
s.pack(side='left')
n = Entry(win).pack(side='bottom')
b2 = Button(win,text='+',command=up1,width=2).pack(side='left')
win.mainloop()
"""
from tkinter import *
num=0
def up1():
    global num
    if s.get()<50:
        num += 1
        txt.config(text = '爱心暴击+%s'%num)
        s.set(num)
def down1():
    global num
    if s.get()>0:
        num -= 1
        txt.config(text='爱心暴击+%s' % num,)
        s.set(num)
def hit(e):
    global num
    num = s.get()
    txt.config(text='爱心暴击+%s' % num)
    if num <= 25:
        txt.config(image=ima2)
    else:
        txt.config(image=ima1)
win=Tk()
win.title('爱心暴击')
#txt = Label(text='送TA玫瑰').pack(side='left)
ima1 = PhotoImage(file = 'head.png')
ima2 = PhotoImage(file='cry.png')
txt = Label(win,text = '爱心暴击+0',image=ima1,compound='right')
txt.pack(side=TOP)
b1 = Button(win,text='-',command=down1,width=2).pack(side='left')
s = Scale(win,from_=0,to=50,resolution=1,orient=HORIZONTAL,showvalue=0,command=hit,troughcolor='green')
s.pack(side='left')
b2 = Button(win,text='+',command=up1,width=2).pack(side='left')
win.mainloop()