'''
PanedWindow给件也是空间管理组件，因为PanedWindow组件可以将自身分为多个模块，然后将组件放在不同的模块之内，用户不仅仅可以设置子模块的排列
方式为水平和垂直，还可以手动调整各个子模块的空间大小。语法如下：
PanedWindow(win)
常见参数及含义：
    1.bg(background)            设置背景颜色
    2.borderwidth               边界线宽度
    3.handlepad                 设置手柄位置
    4.handlesize                设置手机边长
    5.orient                    设置容器内组件的排列方式，其值有HORIZZONTAL(横向分布)和VERTICAL(垂直分布)
    6.sashrelief                面板分割线边框样式，其值有('relief'--默认值,'sunken','raised','groove','ridge')
    7.showhanddle               是否显示调节面板的手柄1True,0False
    8.width                     面板整体宽度，若忽略该值，则由子组件的尺寸决定

创建PanedWindow组件后，还需要使用add()方法将子组件添加到PanedWindow组件中，例如，
在PanedWindow组件中创建两个按钮，并用分割线将其分割开，具体代码如下：
from tkinter import *
panedwindow=PanedWindow(sashrelief='sunken',background='gray',width=200)
panedwindow.pack()
b1=Button(panedwindow,text='左侧按钮')
panedwindow.add(b1)
b2=Button(panedwindow,text='右侧按钮')
panedwindow.add(b2)
mainloop()              #可用鼠标拖动分割线

也可以设定为不可拖动，如下：
from tkinter import *
panedwindow=PanedWindow(sashrelief='sunken',background='gray',width=200)
panedwindow.pack()
b1=Button(panedwindow,text='左侧按钮',state='disabled')
panedwindow.add(b1)
b2=Button(panedwindow,text='右侧按钮',state='disabled')
panedwindow.add(b2)
mainloop()

实例：应用PanedWindow组件调整窗口中各面板的大小
from tkinter import *

pw = PanedWindow(showhandle=True, sashrelief=SUNKEN, orient=VERTICAL, width=300, handlesize=20, handlepad=100)
pw.pack(fill=BOTH, expand=1)
top = Label(pw, text='虽然只是个面板，但是它的大小可以改变', background="#E0FFFF")
pw.add(top)
bottom = Label(pw, text='拖动左侧的开关试试', background="#FFFFE0")
pw.add(bottom)
mainloop()

'''

from tkinter import *

pw = PanedWindow(showhandle=1, sashrelief=SUNKEN, orient=VERTICAL, width=300, handlesize=20,handlepad=100)
pw.pack(fill=BOTH, expand=1)
top = Label(pw, text='虽然只是个面板，但是它的大小可以改变', background="#E0FFFF")
pw.add(top)
bottom = Label(pw, text='拖动左侧的开关试试', background="#FFFFE0")
pw.add(bottom)
mainloop()
