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