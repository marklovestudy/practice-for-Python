'''
鼠标事件
    1.<Button-1>	        单击鼠标左键
    2.<Button-2>	        单击鼠标中间键
    3.<Button-3>	        单击鼠标右键
    4.<Button-4>	        向上滚动滑轮
    5.<Button-5>	        向下滚动滑轮
    6.<B1-Motion>	        按下鼠标左键并拖动鼠标
    7.<B2-Motion>	        按下鼠标中键并拖动鼠标
    8.<B3-Motion>	        按下鼠标右键并拖动鼠标
    9.<ButtonRelease-1>	    释放鼠标左键
    10.<ButtonRelease-2>	释放鼠标中键
    11.<ButtonRelease-3>	释放鼠标右键
    12.<Double-Button-1>	双击鼠标左键
    13.<Double-Button-2>	双击鼠标中键
    14.<Double-Button-3>	双击鼠标右键
    15.<Enter>              鼠标进入控件
    16.<Leaver>	            鼠标移出控件

说明：当事件发生时是，鼠标相对组件的位置会被存入对象event中(鼠标相对组件的位置(event.x,event.y))，
所以在绑定的回调函数中，即使不需要鼠标的位置，也应该接收event参数，否则会报错。
实例:在窗口中添加一个Label组件，当鼠标进入该组件时，立刻显示文字，当鼠标离开组件时，则隐藏label组件中的文字。
def show1(event):
    label.config(text='我是Label组件')
def hidden1(event):
    label.config(text='')
from tkinter import *
win=Tk()
label=Label(win,bg='#C5E1EF',width=20,height=3)
label.pack()
label.bind('<Enter>',show1)
label.bind('<Leave>',hidden1)
win.mainloop()

实例：实现找颜色眼力测试游戏
    在10x10的彩色方格中，有一个方格的颜色与众不同，找出该方块即可进入下一关。具体步骤如下：
#1首先添加窗口，然后通过for循环在窗口中添加100个小方块，并且为方块统一添加背景颜色，然后从中随机
#选择一个方块重新设置背景颜色，并且为该方块绑定单击鼠标左键事件。具体代码如下：
from tkinter import *
import random
#2编写方法col(),实现随机生成两个相近的颜色的色值，并将其保存在数组中。
num=1
inde = random.randint(0,99)
def col():
    arr=list('0123456789ABCDEF')
    #为保证颜色相近，color1+color2多数方块的颜色，color1+color3为A方块的颜色
    color1 = ''
    color2 = ''
    color3 = ''
    for i in range(4):
        color1 += arr[random.randint(0,15)]
    for i in range(2):
        color2 += arr[random.randint(0,15)]
    for i in range(2):
        color3 += arr[random.randint(0,15)]
    colorArr=[]
    colorArr.append('#'+color1+color2)
    colorArr.append('#'+color1+color3)
    return colorArr

#3编写panduan()方法，实现当用户找到颜色与众不同的方块时，自动进入下一关，并且更新当前的关数。
def panduan(event):
    global num,inde
    sqareBox[inde].unbind('<Button-1>')
    num += 1
    level.config(text='第'+str(num)+'关')
    #每刷新一次就需要获取一次方块A的索引
    inde = random.randint(0,99)
    #获取所有方块的颜色
    colorBox = col()
    for i in sqareBox:
        i.config(bg=colorBox[0])
    sqareBox[inde].config(bg=colorBox[1])
    #重新为方块A绑定鼠标单击事件
    sqareBox[inde].bind('<Button-1>',panduan)
win=Tk()
win.geometry('480x480')
win.resizable(0,0)

sqareBox=[]
colorBox=col()
for i in range(10):
    for j in range(10):
        label = Label(win,width=6,height=2,bg=colorBox[0],relief='groove')
        sqareBox.append(label)
        label.grid(row=i,column=j)
sqareBox[inde].config(bg=colorBox[1])
sqareBox[inde].bind('<Button-1>',panduan)
level = Label(win,text='第1关',font=14)
level.grid(row=11,column=0,columnspan=10,pady=10)
win.mainloop()
'''

#1首先添加窗口，然后通过for循环在窗口中添加100个小方块，并且为方块统一添加背景颜色，然后从中随机
#选择一个方块重新设置背景颜色，并且为该方块绑定单击鼠标左键事件。具体代码如下：
from tkinter import *
import random
#2编写方法col(),实现随机生成两个相近的颜色的色值，并将其保存在数组中。
num=1
inde = random.randint(0,99)
def col():
    arr=list('0123456789ABCDEF')
    #为保证颜色相近，color1+color2多数方块的颜色，color1+color3为A方块的颜色
    color1 = ''
    color2 = ''
    color3 = ''
    for i in range(4):
        color1 += arr[random.randint(0,15)]
    for i in range(2):
        color2 += arr[random.randint(0,15)]
    for i in range(2):
        color3 += arr[random.randint(0,15)]
    colorArr=[]
    colorArr.append('#'+color1+color2)
    colorArr.append('#'+color1+color3)
    return colorArr

#3编写panduan()方法，实现当用户找到颜色与众不同的方块时，自动进入下一关，并且更新当前的关数。
def panduan(event):
    global num,inde
    sqareBox[inde].unbind('<Button-1>')
    num += 1
    level.config(text='第'+str(num)+'关')
    #每刷新一次就需要获取一次方块A的索引
    inde = random.randint(0,99)
    #获取所有方块的颜色
    colorBox = col()
    for i in sqareBox:
        i.config(bg=colorBox[0])
    sqareBox[inde].config(bg=colorBox[1])
    #重新为方块A绑定鼠标单击事件
    sqareBox[inde].bind('<Button-1>',panduan)
win=Tk()
win.geometry('480x480')
win.resizable(0,0)
sqareBox=[]
colorBox=col()
for i in range(10):
    for j in range(10):
        label = Label(win,width=6,height=2,bg=colorBox[0],relief='groove')
        sqareBox.append(label)
        label.grid(row=i,column=j)
sqareBox[inde].config(bg=colorBox[1])
sqareBox[inde].bind('<Button-1>',panduan)
level = Label(win,text='第1关',font=14)
level.grid(row=11,column=0,columnspan=10,pady=10)
win.mainloop()