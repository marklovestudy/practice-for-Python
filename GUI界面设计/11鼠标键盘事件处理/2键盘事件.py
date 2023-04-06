'''
键盘事件：
    1.<Return>              按下回车键
    2.<space>               按下空格键
    3.<Key>                 按下某键，键值会作为event对象参数被传递
    4.<Shift-Up>            同时按住<Shift>键和<Up>键
    5.<Alt-Up>              同时按下<Alt>键和<Up>键
    6.<Control-Up>          同时按下<Ctrl>键和<Up>键

实例：
def prt(event):
    le = len(text.get('0.0',END))
    label.config(text=str(le))
    print(type(event),event,event.char)
from tkinter import *
win = Tk()
text = Text(win,width=20,height=5)
text.pack()
label=Label(win)
label.pack()
text.bind('<Key>',prt)
win.mainloop()

实例：模拟贪吃蛇游戏中通过键盘控制蛇的移动方向键控制贪吃蛇向指定方向移动。具体实现步骤如下：
#1首先定义蛇头的初始位置，组成蛇身体的方块的数量等，以便于修改。具体代码如下：
w=10                    #蛇身体由正方形组成，w为正方形的边长
x1=0                    #蛇头的初始位置
y1=10
num=5                   #初始状态的蛇由5个方块组成
step=10                 #蛇移动的单元距离

#3编写up1(),down1()等方法，分别实现上下左右
#控制上移动
def up1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])-step)
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))
#单击下键，控制蛇向下移动
def down1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])+step)
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def left1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind])-step,y=yy(snake[ind]))
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def right1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind])+step,y=yy(snake[ind]))
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def xx(module):
    print(module.winfo_geometry())
    return int(module.winfo_geometry().split('+')[1])

def yy(module):
    return int(module.winfo_geometry().split('+')[2])
#2创建窗口，并且在窗口中添加'蛇'，并且为窗口绑定键盘事件。
#添加蛇
from tkinter import *
win = Tk()
#贪吃蛇
snake=[]
for i in range(num):
    item1=Frame(width=10,height=10,bg='#86E7DD')
    snake.append(item1)
    item1.place(x=x1,y=y1+i*w)
snake[0].config(bg='#E7869D')
win.bind('<Up>',up1)
win.bind('<Down>',down1)
win.bind('<Left>',left1)
win.bind('<Right>',right1)
win.mainloop()
'''
#1首先定义蛇头的初始位置，组成蛇身体的方块的数量等，以便于修改。具体代码如下：
w=10                    #蛇身体由正方形组成，w为正方形的边长
x1=0                    #蛇头的初始位置
y1=10
num=5                   #初始状态的蛇由5个方块组成
step=10                 #蛇移动的单元距离

#3编写up1(),down1()等方法，分别实现上下左右
#控制上移动
def up1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])-step)
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))
#单击下键，控制蛇向下移动
def down1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind]),y=yy(snake[ind])+step)
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def left1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind])-step,y=yy(snake[ind]))
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def right1(event):
    for index,ch in enumerate(snake):
        ind=len(snake)-index-1
        if ind == 0:    #蛇头的移动
            snake[ind].place(x=xx(snake[ind])+step,y=yy(snake[ind]))
        else:           #蛇身体移动
            snake[ind].place(x=xx(snake[ind-1]),y=yy(snake[ind-1]))

def xx(module):
    print(module.winfo_geometry())
    return int(module.winfo_geometry().split('+')[1])

def yy(module):
    return int(module.winfo_geometry().split('+')[2])
#2创建窗口，并且在窗口中添加'蛇'，并且为窗口绑定键盘事件。
#添加蛇
from tkinter import *
win = Tk()
#贪吃蛇
snake=[]
for i in range(num):
    item1=Frame(width=10,height=10,bg='#86E7DD')
    snake.append(item1)
    item1.place(x=x1,y=y1+i*w)
snake[0].config(bg='#E7869D')
win.bind('<Up>',up1)
win.bind('<Down>',down1)
win.bind('<Left>',left1)
win.bind('<Right>',right1)
win.mainloop()