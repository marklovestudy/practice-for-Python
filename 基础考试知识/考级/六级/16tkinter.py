'''
概念：
图形用户界面（Graphical User Interface,简称GUI），是指采用图形方式显示的计算机操作用户界面。
与计算机的命令行界面相比，图形界面对于用户的操作显得更加直观和简便。
tkinter是 Python的内置GUI模块。使用 tkinter可以快速地创建GUI应用程序，
而且IDLE也是用 tkinter模块编写而成的。使用 tkinter创建图形界面时，首先使用import语句导入 tkinter模块，
然后使用 tkinter. Tk生成一个主窗体对象。例如，创建一个没有组件的GUI程序，其程序代码如下图左所示，测试效果如下图右所示

该例中生成的窗体，具有一般应用程序窗体的基本功能，可以最小化、最大化或关闭，甚至可以使用鼠标调整其大小。
其中设置窗体大小，可用Tk对象提供的一个方法 geometry(  )。为了使窗体中添加的组件能得到及时刷新，
可用Tk对象提供的另一个方法 mainloop(  )。1#代码：

import tkinter     #导入tkinter模块
win=tkinter.Tk()   #生成一个主窗体对象
win.geometry("250x130")  #窗体大小
win.title("没有组件的窗体")

win.mainloop()     #进入消息循环

常用组件：
当主窗体生成后，向窗体里添加组件，这样就可以处理窗体及其内部组件的事件。例如，使用 tkinter向窗体添加“退出”按钮，
其程序代码如右图上所示，测试效果如右图下所示。2#代码：

程序代码中，首先自定义单击这个按钮后的事件处理函数my_quit( )，然后实例化 tkinter模块中的1个按钮(Button)组件，
最后调用组件的pack( )方法，将这个组件添加到主窗体中。

import tkinter as tk    #导入并重命名为tk
win=tk.Tk()   #生成一个主窗体对象
win.title("带退出按钮的窗体")
win.geometry("250x130")  #窗体大小
#退出按钮事件处理函数
def my_quit():
        win.quit()
        win.destroy()
#退出按钮对象添加
but_quit=tk.Button(win,text='退出',
                   command=my_quit,width=10,height=2)
but_quit.pack()
win.mainloop()     #进入消息循环

常用组件：
tkinter的常用组件，如下表所示。
Label       显示
Text        文本
Button      按钮
Entry       输入

tkinter布局管理器能控制组件的位置摆放，提供三种布局方法，如右下表所示。
pack()
grid()
place()

tkinter模块的综合应用：
在程序设计中，解决复杂问题的最有效方法是“自顶向下”的设计方法和自底向上”的执行方法。
其基本思想是:首先将一个复杂问题分解为多个小问题，然后只需把处理这些小问题的解决方法组合起来，就可以得到整体的解决方案。
1.运用 Python的 tkinter模块，设计的用户登录界面如下图左所示，测试效果如下图右所示。
设计思路
（1）设计基本框架
（2）设计提示标签、输入框和按钮。
（3）设计功能函数。
（4）设计组件布局
（5）完整程序组合。

tkinter模块的综合应用：
1.运用 Python的 tkinter模块，设计的用户登录界面如下图左所示，测试效果如下图右所示。
设计思路
（1）设计基本框架
（2）设计提示标签、输入框和按钮。
（3）设计功能函数。
（4）设计组件布局
（5）完整程序组合。
2.程序详细分析
（1）设计基本框架，程序代码如图所示。

tkinter模块的综合应用：
2.程序详细分析
（1）设计基本框架，程序代码如图所示。
（2）设计提示标签、输入框和按钮

tkinter模块的综合应用：
2.程序详细分析
（1）设计基本框架，程序代码如图所示。
（2）设计提示标签、输入框和按钮

2.程序详细分析
（1）设计基本框架，程序代码如图所示。
（2）设计提示标签、输入框和按钮
（3）设计功能函数，程序代码如图所示
（4）设计组件布局，程序代码如右图所示

2.程序详细分析
（1）设计基本框架，程序代码如图所示。
（2）设计提示标签、输入框和按钮
（3）设计功能函数，程序代码如图所示
（4）设计组件布局，程序代码如右图所示
（5）完整程序组合，程序代码如图所示

#设计基本框架
import tkinter as tk
import tkinter.messagebox
win=tk.Tk()
win.title("用户登录")
win.geometry("250x130")
#----功能代码开始-----
#--设计功能函数--
#设置变量
var_Name=tk.StringVar()  #设置变量为StringVar对象
var_Name.set('')
var_Pwd=tk.StringVar()
var_Pwd.set('')

#按钮处理函数
def login():
        name=var_Name.get()  #获取用户名
        pwd=var_Pwd.get()   #获取密码
        if name=='admin' and pwd=='python@16':
                tk.messagebox.showinfo(title='用户登录',message='成功！')
        else:
                tk.messagebox.showinfo(title='用户登录',message='失败！')
def cancel():
        var_Name.set('')   #清空用户名
        var_Pwd.set('')   #清空密码
def _quit():
        win.quit()
        win.destroy()

#----登录窗口各组件设计--
#设计2个提示标签
labname=tk.Label(win,text='帐号：',width=80)
labpwd=tk.Label(win,text='密码：',width=80)
#设计2个输入框(textvariable为文本框的值，并关联变量var_Name)
entname=tk.Entry(win,width=100,textvariable=var_Name)
entpwd=tk.Entry(win,show='*',width=100,textvariable=var_Pwd)
#设计3个按钮
but_Ok=tk.Button(win,text='登录',command=login)
but_Cancel=tk.Button(win,text='重置',command=cancel)
but_quit=tk.Button(win,text='退出',command=_quit)

#--登录窗口各组件布局--
#组件的窗口布局
labname.place(x=20,y=10,width=80,height=20)
labpwd.place(x=20,y=40,width=80,height=20)
entname.place(x=120,y=10,width=80,height=20)
entpwd.place(x=120,y=40,width=80,height=20)
but_Ok.place(x=30,y=80,width=50,height=20)
but_Cancel.place(x=100,y=80,width=50,height=20)
but_quit.place(x=170,y=80,width=50,height=20)
#-----功能代码结束-------
win.mainloop()

例题：
温度转换，摄氏温度华氏温度互换，界面如下图：


'''