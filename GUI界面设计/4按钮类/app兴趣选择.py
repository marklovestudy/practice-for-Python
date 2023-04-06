#需要绑定一个变量，如果选中这个复选框，返回1，否则0
# def pp():
#     print(v1.get())
# v1=IntVar()     #创建一个变量
# c1=Checkbutton(win,variable=v1,text='看电视',command=pp)
# c1.pack()
'''
from tkinter import *
win=Tk()    #制作一个屏幕
def pd():
    str1=''
    for i in range(len(user_c)):
        if user_c[i].get() == 1:
            str1+=ls[i]+' '
    l1.config(text=str1)
    return str1.strip().split()
def bf(l):
    n=0;win1=Tk();l2=Label(win1)
    l2.config(text='准备播放。。。'.format());l2.pack()
    def ok(i):
        nonlocal n
        l2.config(text='{} 正在火热播放中。。。'.format(i))
        n+=1
    def out():
        win1.destroy()
    Button(win1,text='看完了',command=lambda :ok(pd()[n])).pack()
    Button(win1,text='关闭',command=out).pack()
    win1.mainloop()
Label(win,text='欢迎来到头条APP，请问您感兴趣的主题是：').pack()  #制作一个显示模块
ls=['军事','旅游','视频','小说','小视频','娱乐','体育','NBA','美食','直播']
user_c=[]
for i in range(10):
    v=IntVar();user_c.append(v)
    Checkbutton(win,variable=v,text=ls[i],command=pd).pack()
l1=Label(win);l1.pack()
Button(win,text='确定',command=lambda :bf(pd())).pack()
win.mainloop()
'''

from tkinter import *       #载入tkinter
win=Tk()    #制作一个屏幕
def pd():                   #创建判断用户选中的项目有哪些
    str1=''
    for i in range(len(user_c)):     #遍历项目次
        if user_c[i].get() == 1:    #如果项目显示1，表示被选中
            str1+=ls[i]+' '         #将选中的内容加入到字符str1中
    l1.config(text=str1)            #把选中的内容显示在l1显示模块中
    return str1.strip().split()     #把选中的内容以列表的形式返回
Label(win,text='欢迎来到头条APP，请问您感兴趣的主题是：').pack()  #制作一个显示模块
ls=['军事','旅游','视频','小说','小视频','娱乐','体育','NBA','美食','直播']    #用户多选项内容
user_c=[]   #创建一个列表存储10个可选项的变量IntVar()
for i in range(10):     #创建10个多选框
    v=IntVar();user_c.append(v)     #创建IntVar()并存入列表
    Checkbutton(win,variable=v,text=ls[i],command=pd).pack()    #创建复选框
l1=Label(win);l1.pack()     #创建底部显示模块，用来显示选中的内容。
win.mainloop()