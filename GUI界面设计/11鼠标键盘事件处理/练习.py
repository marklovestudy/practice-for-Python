from tkinter import *
import random as r
win=Tk()
colors=[]
#1创建100个模块 用for row in range(10)   for column in range(10)
#创建1个目标模块
#2创建随机颜色color1和color2,用16进制表示，前4个16进制是一样的后2个不一样
#3判断目标模块是否被点击，如果被点击下一关，调用#1函数
#1
def color():
    pass
def pd():
    pass
for row in range(10):
    for column in range(10):
        Label(win,bg=colors[0]).grid(row=row,column=column)
l=Label(win,bg=colors[1]).grid(row=r.randint(0,10),column=r.randint(0,10))
l.bind('<Button-1>',pd)
win.mainloop()