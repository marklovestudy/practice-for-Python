'''
Combobox是ttk模块的组件，相当于Entry和OptionMenu组件的组合，用户可以输入内容，也可以通过下接选择内容。
语法如下：
Combobox(win,textvariable=StringVar(),values=('苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝'))

实例1
from tkinter import *
from tkinter.ttk import *
win=Tk()
val=StringVar()
fruits=('苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝')
Combobox(win,textvariable=val,values=('苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝')).pack(padx=10,pady=10)
win.mainloop()

实例：以管理员身份查看报表
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.title('Combobox的创建')
Label(win,text='选择管理员身份：').grid(row=0,column=0,pady=10)
list1=['蓝色妖姬','烈焰焚情','寒冰幽兰','岁岁芳华','朝暮盈霄','陌上花开']
c1=Combobox(win,textvariable=StringVar(),values=list1)
c1.grid(row=0,column=1,pady=10)
c1.current(0)           #设置默认值是0号索引的内容
Label(win,text='查看类别:').grid(row=2,column=0,pady=10)
list2=['进销总览','销量','库存','进售价','账单','经办人']
c2=Combobox(win,textvariable=StringVar(),values=list2)
c2.grid(row=2,column=1,pady=10)
c2.current(0)           #设置默认值是0号索引的内容
Button(win,text='提交').grid(row=3,columnspan=4,pady=10,sticky=W+E)

win.mainloop()

Combobox组件的相关方法：
    1.get()                     获取被选中的选项
    2.set(value)                设置当前选中的值为value.
    3.current(index)            设置默认值为索引号的选项。

实例：会员办理
from tkinter import *
from tkinter.ttk import *
def set1():
    c1.set('128元钻石卡会员')
def get1():
    l1.config(text='恭喜!'+c1.get()+'办理成功')
    l1.grid(row=4,columnspan=3)
win=Tk()
win.title('Combobox的创建')
Label(win,text='选择会员：').grid(row=0,column=0,pady=10)
list1=['38元银卡会员','68元黄金卡会员','98元白金卡会员','128元钻石卡会员','158元大师卡会员','168元王者卡会员']
c1=Combobox(win,textvariable=StringVar())
c1['values']=list1
c1.grid(row=0,column=1,pady=10)
c1.current(0)           #设置默认值是0号索引的内容
Button(win,text='一键选择钻石会员',command=set1).grid(row=0,column=2,pady=10)
Button(win,text='提交',command=get1).grid(row=2,columnspan=4,pady=10)
l1=Label(win,foreground='red',font=14)
win.mainloop()

实例：记事添加日历
from tkinter import *
from tkinter.ttk import *
def getMon(e):
    if c1.get() == '4' or c1.get() == '6' or c1.get() == '9' or c1.get() == '11':
        d = tuple(range(1, 31))
    elif c1.get() == '2':
        d = tuple(range(1, 29))
    else:
        d = tuple(range(1, 32))
    c2['values']=d
def getdate():
    info=l1.cget('text')
    print(info)
    temp=c1.get()+'月'+c2.get()+'日：\t'+text1.get('0.0',END)
    l1.config(text=info+temp)
    text1.delete('0.0',END)
win=Tk()
win.title('添加日程')
m=tuple(range(1,13))            #月份元组
d=tuple(range(1,31))            #日元组，可根据分支结构设定不同的天数

c1=Combobox(win,textvariable=StringVar())
c1['values']=m
c1.grid(row=0,column=0,pady=10)
Label(win,text='月').grid(row=0,column=1,pady=10)
c1.current(0)           #设置默认值是0号索引的内容
c1.bind('<<ComboboxSelected>>',getMon)

c2=Combobox(win,textvariable=StringVar())
c2['values']=d
c2.grid(row=0,column=2,pady=10)
Label(win,text='日').grid(row=0,column=3,pady=10)
c2.current(0)           #设置默认值是0号索引的内容
text1 = Text(win)
text1.grid(row=1,columnspan=6,pady=10)

Button(win,text='确定',command=getdate).grid(row=2,columnspan=6,pady=10)

l1=Label(win)
l1.grid(row=3,columnspan=6,pady=10)
win.mainloop()


'''

from tkinter import *
from tkinter.ttk import *
def getMon(e):
    if c1.get() == '4' or c1.get() == '6' or c1.get() == '9' or c1.get() == '11':
        d = tuple(range(1, 31))
    elif c1.get() == '2':
        d = tuple(range(1, 29))
    else:
        d = tuple(range(1, 32))
    c2['values']=d
def getdate():
    info=l1.cget('text')
    print(info)
    temp=c1.get()+'月'+c2.get()+'日：\t'+text1.get('0.0',END)
    l1.config(text=info+temp)
    text1.delete('0.0',END)
win=Tk()
win.title('添加日程')
m=tuple(range(1,13))            #月份元组
d=tuple(range(1,31))            #日元组，可根据分支结构设定不同的天数

c1=Combobox(win,textvariable=StringVar())
c1['values']=m
c1.grid(row=0,column=0,pady=10)
Label(win,text='月').grid(row=0,column=1,pady=10)
c1.current(0)           #设置默认值是0号索引的内容
c1.bind('<<ComboboxSelected>>',getMon)

c2=Combobox(win,textvariable=StringVar())
c2['values']=d
c2.grid(row=0,column=2,pady=10)
Label(win,text='日').grid(row=0,column=3,pady=10)
c2.current(0)           #设置默认值是0号索引的内容
text1 = Text(win)
text1.grid(row=1,columnspan=6,pady=10)

Button(win,text='确定',command=getdate).grid(row=2,columnspan=6,pady=10)

l1=Label(win)
l1.grid(row=3,columnspan=6,pady=10)
win.mainloop()