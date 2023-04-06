users={'mark':'mark123456'}                         #创建字典存储用户信息
def dl():
    global users                                    #申明users为全局变量
    if e1.get() in users.keys():                    #查看用户是否存在e1.get()获取e1的获取值
        if e2.get() == users[e1.get()]:             #如果用户密码正确，成功登陆
            l1.config(text='登陆成功')              #设置显示块l1的内容为‘登陆成功’
        else:
            l1.config(text='密码不正确，登陆失败')    #设置显示块l1的内容为‘失败’
    else:
        l1.config(text='账号不存在，请注册')          #如果用户不存在，提示注册
from tkinter import *       #载入tkinter
win=Tk()                    #创建窗口
win.title('用户登录和注册')   #设置标题名字
Label(win,text='用户：').grid(row=0,column=0)    #创建显示模块，row:行，column:列
Label(win,text='密码：').grid(row=1,column=0)    #创建显示模块，row:行，column:列
e1=Entry(win);e1.grid(row=0,column=1)              #创建单行输入模块
e2=Entry(win,show='*');e2.grid(row=1,column=1)              #创建单行输入模块
Button(win,text='登陆',command=dl).grid(row=2,column=1)      #创建按钮模块
Button(win,text='注册').grid(row=2,column=0)      #创建按钮模块
l1=Label(win);l1.grid(row=3,columnspan=2)        #添加一个显示模块
win.mainloop()              #内循环