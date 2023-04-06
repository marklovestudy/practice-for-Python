'''
Canvas组件主要是绘制图形，文字，设计动画，语法如下：
canvas=Canvas(win,option)
    参数如下：
    1.bd                    边框宽度，默认为2像素
    2.bg                    设置背景颜色
    3.confine               如果为true(默认值)，则画布不能滚动到可滑动区域外
    4.cursor                设置鼠标悬停Canvas组件上时的形状
    5.height                设置画布的高度
    6.width                 设置画布的宽度
    7.highlightcolor        设置画布高亮边框的颜色
    8.relief                设置边框的样式
    9.scrollregion          其值为元素tuple(w,n,e,s)，分别定义左、上、右、下四个方向可滚动的最大区域
    10.xscrollincrement     水平方向滚动时，请求滚动的数量值
    11.yscrollincrement     垂直方向滚动时，请求滚动的数量值
    12.xscrollcommand       绑定水平滚动条
    13.yscrollcommand       绑定垂直滚动条

形状：
    1.canvas.create_line(x1,y1,x2,y2...xn,yn,option)            绘制线条
    2.create_rectangle(x1,y1,x2,y2,opthion)                     绘制矩形
    3.create_oval(x1,y1,x2,y2,option)                           绘制椭圆
    4.create_arc(x1,y1,x2,y2,extent=-180,style=ARC,option)      绘制圆弧和扇形  (x1,y1)起点,(x2,y2)终点extent角度，style是类型
    5.canvas.create_polygon(x1,y1,x2,y2,xn,yn,option)           绘制多边形(x1,y1),(x2,y2),(xn,yn)为多边形的顶点
    6.canvas.create_text(x,y,text=str,option)                   绘制文字option属性：font,fill,justify.
    7.create_image(x,y,image=house1,option)                     绘制图像

改变坐标：
    1.move(image,add_x,add_y)
    2.coords(image,(x,y))
实例：窗口中创建画布
from tkinter import *
win = Tk()
win.title('创建canvas画布')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,bg='yellow').pack()
win.mainloop()

实例：绘制线条：canvas.create_line(x1,y1,x2,y2...xn,yn,option)
create_line参数及含义
    1.arrow             是否添加箭头，默认为无箭头，另外还可以设置其值为FIRST(起始端右箭头)、LAST(末端右箭头)、BOTH(两端都有箭头)
    2.arrowshap         设置箭头的形状，其值为元素(d1,d2,d3,)分别表示三角形箭头的底、斜边和高的距离
    3.capstyle          线条终点的样式，其属性值有BUTT(默认值)、PROJECTING和ROUND
    4.dash              设置线条为虚线，以及虚线的形状，其值为元组(x1，x2)表示x1像素的实线和x2像素的空白交替出现
    5.dashoffset        与dash相近，不过含义为x1像素的空白和x2像素的实现交替显示
    6.fill              设置线条颜色
    7.joinstyle         设置线条焦点的颜色，其值有ROUND(默认值)、BEVEL和MITER
    8.stipple           绘制位图线条
    9.width             设置线条宽度
from tkinter import *
win = Tk()
win.title('创建canvas画布')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,bg='yellow')
line1=(14,65,66,65,83,19,99,64,148,64,111,96,126,143,83,113,44,142,58,97,14,65)
canvas.create_line(*line1,fill='red')
canvas.pack()
win.mainloop()

绘制矩形
create_rectangle(x1,y1,x2,y2,opthion)
(x1,y1),(x1,y2),(x2,y1),(x2.y2)四个点。x2-x1=y2-y1时为正方形
#canvas.move(对象，x_v,y_v)        x_v为x增加值，y_v为y的增加值
def up1(event):
    canvas.move(rect,0,-2)
def down1(event):
    canvas.move(rect,0,2)
def left1(event):
    canvas.move(rect,-2,0)
def right1(event):
    canvas.move(rect,2,0)
from tkinter import *
win = Tk()
win.title('创建canvas画布')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,bg='yellow',relief='solid')
line1=(10,10,50,50)
rect=canvas.create_rectangle(*line1,fill='red')
canvas.pack()
win.bind('<Up>',up1)
win.bind('<Down>',down1)
win.bind('<Left>',left1)
win.bind('<Right>',right1)
win.mainloop()

绘制椭圆
create_oval(x1,y1,x2,y2,option)
(x1,y1),(x1,y2),(x2,y1),(x2.y2)四个点为椭圆外切矩形的四个角
def up1(event):
    canvas.move(rect,0,-2)      #canvas.move(对象，x_v,y_v)
def down1(event):
    canvas.move(rect,0,2)
def left1(event):
    canvas.move(rect,-2,0)
def right1(event):
    canvas.move(rect,2,0)
from tkinter import *
win = Tk()
win.title('创建canvas画布')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,bg='yellow',relief='solid')
line1=(10,10,30,50)
rect=canvas.create_oval(*line1,fill='red')
canvas.pack()
win.bind('<Up>',up1)
win.bind('<Down>',down1)
win.bind('<Left>',left1)
win.bind('<Right>',right1)
win.mainloop()

实例：绘制简单人脸
def up1(event):
    global com
    for i in com:
        canvas.move(i,0,-2)      #canvas.move(对象，x_v,y_v)
def down1(event):
    global com
    for i in com:
        canvas.move(i,0,2)
def left1(event):
    global com
    for i in com:
        canvas.move(i,-2,0)
def right1(event):
    global com
    for i in com:
        canvas.move(i,2,0)
from tkinter import *
win = Tk()
win.title('创建canvas画布')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,bg='yellow',relief='solid')

rect1=canvas.create_oval(34,68,143,127,fill='#C8F7F2')
rect2=canvas.create_oval(59,83,71,99,fill='#E6F1B7')
rect3=canvas.create_oval(61,86,71,94,fill='#000000')
rect4=canvas.create_oval(101,83,113,99,fill='#E6F1B7')
rect5=canvas.create_oval(100,86,109,94,fill='#000000')
com=[rect1,rect2,rect3,rect4,rect5]

canvas.pack()
win.bind('<Up>',up1)
win.bind('<Down>',down1)
win.bind('<Left>',left1)
win.bind('<Right>',right1)
win.mainloop()

绘制圆弧和扇形
create_arc(x1,y1,x2,y2,extent=-180,style=ARC,option)        (x1,y1)起点,(x2,y2)终点extent角度，style是类型
from tkinter import *
win = Tk()
win.title('创建canvas画布')
win.geometry('500x400')
canvas=Canvas(win,width=500,height=400,bg='yellow',relief='solid')
rect1=canvas.create_arc(20,40,150,150,extent=120,outline='red',start=30,width=2,style=ARC)
rect2=canvas.create_arc(170,40,300,150,extent=120,outline='red',start=30,width=2,style=CHORD)
rect3=canvas.create_arc(320,40,450,150,extent=120,outline='red',start=30,width=2,style=PIESLICE)
canvas.pack()
win.mainloop()

绘制有籽西瓜
from tkinter import *
win = Tk()
win.title('西瓜')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,relief='solid')

rect1=canvas.create_arc(40,40,150,150,extent=-180,outline='green',fill='red',width=5)
rect2=canvas.create_line(42,94,148,94,width=7,fill='red')
rect3=canvas.create_oval(95,95,100,100,fill='#000000')
rect4=canvas.create_oval(70,97,75,102,fill='#000000')
rect5=canvas.create_oval(95,125,100,130,fill='#000000')
rect6=canvas.create_oval(65,125,70,130,fill='#000000')
rect7=canvas.create_oval(125,110,130,115,fill='#000000')

canvas.pack()
win.mainloop()

绘制扇形
from tkinter import *
win = Tk()
win.title('西瓜')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,relief='solid')

canvas.create_line(95,124,95,194,width=12,fill='#E9D39D',capstyle=ROUND)
rect1=canvas.create_arc(40,40,150,150,extent=-40,outline='green',fill='red',start=-70,width=5,style=PIESLICE)
rect2=canvas.create_arc(8,-67,181,155,extent=-40,outline='red',fill='red',start=-70,width=2,style=PIESLICE)

canvas.create_oval(92,74,97,79,fill='#000000')
canvas.create_oval(97,94,102,99,fill='#000000')
canvas.create_oval(110,124,113,127,fill='#000000')
canvas.create_oval(90,134,93,137,fill='#000000')

canvas.pack()
win.mainloop()

绘制多边形
canvas.create_polygon(x1,y1,x2,y2,xn,yn,option)     (x1,y1),(x2,y2),(xn,yn)为多边形的顶点
from tkinter import *
win = Tk()
win.title('多边形')
win.geometry('300x200')
canvas=Canvas(win,width=200,height=200,relief='solid')

canvas.create_polygon(27,8,27,62,54,34,fill='#000000')
canvas.create_polygon(54,34,81,8,81,63,fill='#000000')

canvas.pack()
win.mainloop()

绘制文字
canvas.create_text(x,y,text=str,option)     option属性：font,fill,justify.
from tkinter import *
import random
fill_color = ['red','pink','yellow','blue','green']
font_family = ['方正舒体','方正姚体','华文琥珀','宋体','华文行楷','楷体','华文新魏','隶书']
def draw():
    canvas.delete('all')            #清空画布
    color=fill_color[random.randint(0,4)]
    family=font_family[random.randint(0,7)]
    text=canvas.create_text(160,60,text=str1,font=(family,20),fill=color)

win = Tk()
win.title('绘制文字')
win.geometry('330x200')
canvas=Canvas(win,width=300,height=160,relief='solid')
str1='人因梦想而伟大'
canvas.pack()
Button(win,text='绘制',command=draw).pack()
win.mainloop()

绘制图像
create_image(x,y,image=house1,option)
from tkinter import *
from tkinter.messagebox import *
#拖动鼠标，移动小鸟
def draw(event):
    canvas.coords(bird,event.x,event.y)
#判断小鸟是否回家
def panduan(event):
    canvas.coords(bird, event.x, event.y)
    x1=abs(event.x-340)
    y1=abs(event.y-70)
    if x1 <70 and y1<75:
        showinfo('小鸟回家','谢谢你成功帮小鸟回家')

win = Tk()
win.title('帮助小鸟回家')
win.geometry('400x320')
canvas=Canvas(win,width=400,height=320,relief='solid',bg='#E7D2BB')
bird1=PhotoImage(file='bird.png')
house1=PhotoImage(file='house.png')
house = canvas.create_image(340,70,image=house1)            #绘制房子
bird = canvas.create_image(150,250,image=bird1)             #绘制小鸟
canvas.grid(row=0,column=0,columnspan=2)
canvas.bind('<B1-Motion>',draw)                             #绑定鼠标按住左键移动事件
canvas.bind('<ButtonRelease-1>',panduan)                    #绑定鼠标松开左键事件

win.mainloop()

拖动鼠标绘制图形
from tkinter import *

#拖动鼠标，移动小鸟
def draw(event):
    global text1
    text1=canvas.create_oval(event.x,event.y,event.x+10,event.y+10,fill='green',outline='')
#判断小鸟是否回家
def delete1():
    canvas.delete('all')
    can()

win = Tk()
win.title('书法秀')
win.geometry('420x420')
canvas=Canvas(win,width=400,height=400,relief='solid',bg='#F1E9D0')
def can():
    rect = canvas.create_rectangle(4,4,400,385,outline='red',width=2)
    line1 = canvas.create_line(2,198,400,198,dash=(2,2),fill='red')         #画2像素空一下
    line2 = canvas.create_line(198,2,198,400,dash=(2,2),fill='red')
    line3 = canvas.create_line(0, 0, 400, 400, dash=(2, 2), fill='red')
    line4 = canvas.create_line(0, 400, 400,0, dash=(2, 2), fill='red')
    canvas.pack(side='bottom')
    canvas.bind('<B1-Motion>',draw)                             #绑定鼠标按住左键移动事件

Button(win,text='清屏',command=delete1).pack(side='bottom')
can()
win.mainloop()

设计动画
实例：小猫钓鱼
#1导入模块，小猫，小鱼。
from tkinter import *
from tkinter.messagebox import *
import time
#2通过coords()方法让鱼游动，然后通过sleep()方法让鱼每隔0.1秒移动step，然后通过update()
#方法强制刷新窗口，具体在步骤1的第3行代码后面添加如下代码
x1=350
step=2
op=1
bar=1
def move1():
    global bar,x1,fish,op
    bar=1
    if (x1>=350):
        op=-1
        canvas.delete(fish)
        fish = canvas.create_image(x1,50,image=fish1)

    if (x1<=0):
        op=1
        canvas.delete(fish)
        fish = canvas.create_image(x1,50,image=fish2)
    x1=x1+op*step
    canvas.coords(fish,(x1,50))

def move_fish():
    while bar:
        move1()
        time.sleep(0.1)
        win.update()

#3当玩家单击按钮'钓鱼'按钮时，将猫移动到最上方，然后判断小猫是否抓到鱼，具体在步骤2的代码后面直接添加如下代码:
def catch_fish():
    canvas.coords(cat,(150,50))
    global bar
    if abs(x1-50)<=160 and abs(x1-50)>=40:
        showinfo('成功钓鱼','恭喜钓到一条鱼')
    else:
        showinfo('钓鱼失败', '哇哦，钓鱼失败了')
win = Tk()
win.title('小猫钓鱼')
win.geometry('400x400')
canvas=Canvas(win,width=400,height=320,relief='solid',bg='#E7D2BB')
cat1=PhotoImage(file='cat.png')
fish1=PhotoImage(file='fish1.png')
fish2=PhotoImage(file='fish2.png')
fish=canvas.create_image(350,50,image=fish1)        #绘制小鱼
cat=canvas.create_image(150,250,image=cat1)
canvas.grid(row=0,column=0,columnspan=2)
btn=Button(win,text='开始',command=move_fish)
btn.grid(row=1,column=0)
Button(win,text='钓鱼',command=catch_fish).grid(row=1,column=1)
win.mainloop()
'''

#1导入模块，小猫，小鱼。
from tkinter import *
from tkinter.messagebox import *
import time
#2通过coords()方法让鱼游动，然后通过sleep()方法让鱼每隔0.1秒移动step，然后通过update()
#方法强制刷新窗口，具体在步骤1的第3行代码后面添加如下代码
x1=350
step=2
op=1
bar=1
def move1():
    global bar,x1,fish,op
    bar=1
    if (x1>=350):
        op=-1
        canvas.delete(fish)
        fish = canvas.create_image(x1,50,image=fish1)

    if (x1<=0):
        op=1
        canvas.delete(fish)
        fish = canvas.create_image(x1,50,image=fish2)
    x1=x1+op*step
    canvas.coords(fish,(x1,50))

def move_fish():
    while bar:
        move1()
        time.sleep(0.1)
        win.update()

#3当玩家单击按钮'钓鱼'按钮时，将猫移动到最上方，然后判断小猫是否抓到鱼，具体在步骤2的代码后面直接添加如下代码:
def catch_fish():
    canvas.coords(cat,(150,50))
    global bar
    if abs(x1-50)<=160 and abs(x1-50)>=40:
        showinfo('成功钓鱼','恭喜钓到一条鱼')
    else:
        showinfo('钓鱼失败', '哇哦，钓鱼失败了')
win = Tk()
win.title('小猫钓鱼')
win.geometry('400x400')
canvas=Canvas(win,width=400,height=320,relief='solid',bg='#E7D2BB')
cat1=PhotoImage(file='cat.png')
fish1=PhotoImage(file='fish1.png')
fish2=PhotoImage(file='fish2.png')
fish=canvas.create_image(350,50,image=fish1)        #绘制小鱼
cat=canvas.create_image(150,250,image=cat1)
canvas.grid(row=0,column=0,columnspan=2)
btn=Button(win,text='开始',command=move_fish)
btn.grid(row=1,column=0)
Button(win,text='钓鱼',command=catch_fish).grid(row=1,column=1)
win.mainloop()