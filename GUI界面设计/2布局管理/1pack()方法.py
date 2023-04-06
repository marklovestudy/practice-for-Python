'''
pack()方法中的参数：
    1.side              设置组件水平展示或者垂直展示
    2.padx              设置组件距离窗口的水平距离
    3.pady              设置组件距离窗口的垂直距离
    4.ipadx             设置组件内的文字距离组件边界的水平距离
    5.ipady             设置组件内的文字距离组件边界的垂直距离
    6.fill              设置组件填充所在的空白空间的方式
    7.expand            设置组件是否完全填充其余空间
    8.anchor            设置组件在窗口中的位置
    9.before            设置该组件应该位于指定组件的前面
    10.after            设置该组件应该位于指定组件的后面

1.side在水平、垂直主要有4个属性：
    1.top               指组件从上到下依次排列，这是side参数的默认值。
    2.bottom            指组件从下到上依次排列。
    3.left              指组件从左到右依次排列。
    4.right             指组件从右向左依次排列。
实例1：左到右
from tkinter import *
win = Tk()
v1 = '门前一颗树'
v2 = '左边一口井'
v3 = '右边一辆车'
Label(win,text=v1,bg='green').pack(side='left')
Label(win,text=v2,bg='pink').pack(side='left')
Label(win,text=v3,bg='yellow').pack(side='left')
win.mainloop()

实例2：下到上
from tkinter import *
win = Tk()
v1 = '门前一颗树'
v2 = '左边一口井'
v3 = '右边一辆车'
Label(win,text=v1,bg='green').pack(side='bottom')
Label(win,text=v2,bg='pink').pack(side='bottom')
Label(win,text=v3,bg='yellow').pack(side='bottom')
win.mainloop()

2、3、padx和pady,设置组件距离窗口的距离,单位px分辨率
from tkinter import *
win = Tk()
v1 = '门前一颗树'
v2 = '左边一口井'
v3 = '右边一辆车'
Label(win,text=v1,bg='green').pack(side='bottom',padx=50,pady=30)
Label(win,text=v2,bg='pink').pack(side='bottom',padx=50,pady=30)
Label(win,text=v3,bg='yellow').pack(side='bottom',padx=50,pady=30)
win.mainloop()

4、5、ipadx和ipady,设置组件内的文字距离组件边界的距离,单位px分辨率
from tkinter import *
win = Tk()
v1 = '门前一颗树'
v2 = '左边一口井'
v3 = '右边一辆车'
Label(win,text=v1,bg='green').pack(side='bottom',padx=50,pady=30,ipadx=50,ipady=30)
Label(win,text=v2,bg='pink').pack(side='bottom',padx=50,pady=30,ipadx=50,ipady=30)
Label(win,text=v3,bg='yellow').pack(side='bottom',padx=50,pady=30,ipadx=50,ipady=30)
win.mainloop()

实例斗兽棋的规则
from tkinter import *
win = Tk()
win.title('斗兽棋规则')

l1 = Label(win,text='象吃狮',bg='red',font=14)
l2 = Label(win,text='狮吃虎',bg='red',font=14)
l3 = Label(win,text='虎吃豹',bg='red',font=14)
l4 = Label(win,text='豹吃狼',bg='red',font=14)
l5 = Label(win,text='狼吃狗',bg='red',font=14)
l6 = Label(win,text='狗吃猫',bg='red',font=14)
l7 = Label(win,text='猫吃鼠',bg='red',font=14)
l8 = Label(win,text='鼠吃象',bg='red',font=14)

l1.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l2.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l3.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l4.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l5.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l6.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l7.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
l8.pack(side='left',padx=10,pady=5,ipadx=6,ipady=4)
win.mainloop()

6、fill,设置组件填充所在的空白空间的方式,它有4个属性：
    x:表示完全填充水平方向的空白空间。
    y:表示完全填充垂直方向的空白空间。
    both:表示完全填充水平和垂直方向的空白空间。
    none:表示不填充空白空间(默认值)。

实例：运行后，你不管怎么拉窗口的大小，y方向上都是填充满的，但x就会有空白
from tkinter import *
win = Tk()
v = '天若有情天亦老，人间正道是沧桑'
l1 = Label(win,text=v,bg='#ba55d3',font='14',fg='red').pack(side='left',fill='y')
win.mainloop()

实例斗兽棋的规则 纵向填充

l1.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l2.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l3.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l4.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l5.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l6.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l7.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
l8.pack(side='left',padx=10,pady=5,ipadx=6,fill='y')
win.mainloop()

7、expand:设置组件是否填满父容器的额外空间，其属性值有两个，分别是True(或者1)和False(或者0)。
    1True/1         表示组件填满父容器的整个空间。
    2False/0        表示组件不填满父容器的整个空间。

实例：当上下水平拉伸时可以看到效果
l1.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l2.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l3.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l4.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l5.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l6.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l7.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l8.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
win.mainloop()

8、anchor            设置组件在父窗口中的位置，默认为center(上下左右居中)，另可选：八方(e,s,w,n,nw,ne,sw,se)
from tkinter import *
win = Tk()
l1 = Button(win,text='下一步',bg='gray',font=14)
l1.pack(anchor='s',side='right',padx=10,pady=10)
win.mainloop()

实例：模拟确认退出本窗口的对话框
from tkinter import *
win=Tk()
win.geometry('350x150')
win.title('tkinter的初使用')
b1 = Label(win,text='确定退出本窗口吗？')
b2 = Button(win,text='确定退出',bg='red')
b3 = Button(win,text='我再想想',bg='green')
b1.pack(fill='x',pady=20)
b2.pack(side='right',padx='10',ipadx='6',pady='20',anchor='se')
b3.pack(side='right',padx='10',ipadx='6',pady='20',anchor='se')
win.mainloop()

9、10、before、after            设置该组件应该位于指定组件的前后顺序
from tkinter import *
win = Tk()
win.title('tkinter使用')

#打乱顺序
l4 = Label(win,text='豹吃狼',bg='red',font=14)
l2 = Label(win,text='狮吃虎',bg='red',font=14)
l3 = Label(win,text='虎吃豹',bg='red',font=14)
l5 = Label(win,text='狼吃狗',bg='red',font=14)
l7 = Label(win,text='猫吃鼠',bg='red',font=14)
l6 = Label(win,text='狗吃猫',bg='red',font=14)
l8 = Label(win,text='鼠吃象',bg='red',font=14)
l1 = Label(win,text='象吃狮',bg='red',font=14)

l1.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1)
l2.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l1)
l3.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l2)
l4.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l3)
l5.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l4)
l6.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l5)
l7.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l6)
l8.pack(side='left',padx=10,pady=5,ipadx=6,fill='y',expand=1,before=l7)
win.mainloop()

说明：anchor,fill,side等参数的作用效果是相互影响的，大家要灵活使用。
'''
