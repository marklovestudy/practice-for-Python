'''
messagebox会话框分类
    messagebox模块是tkinter模块中的一个模块，该模块根据会话窗口的应用场合，提供了8种会话框：
                会话框                             含义
    1.showinfo(title,message,option)            显示消息提示
    2.showwarning(title,message,option)         显示警告消息
    3.showerror(title,message,option)           显示错误消息
    4.askquestion(title,message,option)         显示询问消息,返回yes和no
    5.askokcancle(title,message,option)         显示‘确定’或‘取消’。若用户选择‘确定’，返回True,选择‘取消’返回False
    6.askyesno(title,message,option)            显示‘是’或‘否’。若用户选择‘是’，返回True,选择‘否’返回False
    7.askyesnocancle(title,message,option)      显示‘是’、‘否’和‘取消’。选择‘是’，返回True,选择‘否’返回False，选择‘取消’，返回None
    8.askretrycancle(title,message,option)      显示‘重试’和‘取消’。选择‘重试’，返回True,选择‘取消’返回False

以上8种会话框：参数基本相同，title是会话框标题，message是文字内容，option可选参数，主要有以下3个参数：
    1.default       设置默认的按钮，即按下回车键时响应的按钮，默认值为第一个按钮
    2.icon          设定显示的图标，有INFO、ERROR、QUESTION以及WARNING。
    3.parent        指定当会话框关闭时，焦点指向的父窗口。

messagebox是tkinter中的一个模块，所以需要通过from...import...引入该模块才能使用各会话消息框
实例：使用showInfo(title,message,option)方法可以显示提示消息会话框，并且该会话框中含有一个‘确定’按钮，单击即可关闭该会话框。
模拟游戏中老玩家回归游戏的欢迎功能：
def mess():
    showinfo('welcome','好久不见，欢迎回归')
    showwarning('警告','好久不见，欢迎回归')
    showerror('错误','好久不见，欢迎回归')
    v=askquestion('问题','好久不见，欢迎回归',default='no')
    print('问题', v)
    v=askokcancel('确定和取消','好久不见，欢迎回归',default='ok')        #设置默认值abort, retry, ignore, ok, cancel, no, or yes
    print('确定和取消',v)
    v=askyesno('是和否','好久不见，欢迎回归',icon=ERROR)                #设置图标
    print('是和否', v)
    v=askyesnocancel('是、否、取消','好久不见，欢迎回归',parent=win)
    print('是、否、取消', v)
    v=askretrycancel('重试、取消','好久不见，欢迎回归')
    print('重试、取消', v)
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title('会话框')
Button(win,text='进入游戏',command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建showinfo()会话框
    showinfo("welcome！","好久不见，欢迎回归")
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="进入游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建showinfo()会话框
    showwarning("警告","您正在退出游戏，退出后，将会失去本轮游戏所有得分")
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("警告会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="退出游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建showerror()会话框
    showerror("错误提醒","XX游戏请求开启摄像头权限，\n您拒绝了此项请求，导致游戏无法正常进行")
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("错误会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="进入游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建askokcancel()会话框
    boo=askokcancel("关闭提醒","您正在关闭主窗口，点击确定即可关闭主窗口")
    if boo==True:
        win.quit()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("关闭会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="关闭窗口",command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建askyesno()会话框
    boo=askyesno("关闭提醒","您正在关闭主窗口，点击确定即可关闭主窗口")
    if boo==True:
        win.quit()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("关闭会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="关闭窗口",command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建showinfoerror()会话框
    boo=askyesnocancel("退出提醒","您正在退出程序，点击确定即可退出程序,点击否后台运行程序，单击取消则关闭该会话框")
    if boo==True:          #用户选择 是
        win.quit()
    elif boo==False:       #用户选择否
        win.iconify()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("警告会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="退出程序",command=mess).pack(padx=20,pady=20)
win.mainloop()

def mess():
    # 创建showinfoerror()会话框
    boo=askretrycancel("重试提醒","打开游戏出现错误，请选择重试或者取消")
    if boo==True:          #用户选择 重试
        mess()
    else:                  #用户选择取消
        win.quit()
from tkinter import *
from tkinter.messagebox import *
win=Tk()
win.title("警告会话框")
#创建一个按钮，单击按钮时，弹出会话框
Button(win,text="打开游戏",command=mess).pack(padx=20,pady=20)
win.mainloop()
'''
