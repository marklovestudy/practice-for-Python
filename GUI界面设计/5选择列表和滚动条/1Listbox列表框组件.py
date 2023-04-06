'''
Listbox组件的基本使用
    listbox为列表框组件，它可以包含一个或多个文本，以便进行单选或者多选。其语法如下：
    listbox=Listbox(win,option)
    代码如下：
    listbox=Listbox(win)
    listbox.insert(END,'珠海')

Listbox组件的相关属性,见实例3
    1.listvariable                  指向一个StringVar变量，用于存放Listbox组件所有项目
    2.selectbackground              某个选项被选中时的背景颜色
    3.selectmode                    选择模式，值可以是'single(单选)'，'browse(单选)'(可以拖动鼠标或使用方向键改变选项)、
                                    'multiple(多选)'，'extended(多选)'(可以通过<Shift>、<Ctrl>或者拖动鼠标实现多选)
    4.takefocus                     指定列表框是否可以通过<Tab>键转移焦点
    5.xscrollcommand                为列表框添加水平滚动条
    6.yscrollcommand                为列表框添加垂直滚动条

Listbox组件的相关方法,见实例4
    1.insert(index,text)            向列表框中指定位置添加选项，index索引，text表示添加的选项
    2.delete(start,[end])           删除列表中start-end区间的选项，如果省略end，则表示删除索引为start的选项
    3.selection_set(start,[end])    选中列表框中start-end区间的选项，如果省略，则选取索引为start的选项
    4.selection_get(index)          获取某顶的内容，index为所获取项的索引值
    5.size()                        获取列表框组的长度
    6.selection_includes()          判断某项是否被选中

可通过列表存储选项
from tkinter import *
win = Tk()
items=['苹果','香蕉','梨','葡萄','圣女果','百香果']
listbox=Listbox(win,height=6,width=20,relief='solid')
for i in items:
    listbox.insert(END,i)
listbox.pack()
win.mainloop()

实例：实现展开选择列表功能
def show(e):
    print(e)
    listbox.delete(0,END)           #删除列表组件的第一行到最后一行
    for i in items:
        listbox.insert(END,i)
        listbox.pack(fill=X)
from tkinter import *
win = Tk()
items=['重庆','北京','天津','上海','广州','上海']
listbox=Listbox(win,height=6,width=20,relief='solid')

enc = Entry(win)
enc.pack(fill=X)
enc.bind('<Button-1>',show)
listbox.bind('<Double-Button-1>',show)
win.mainloop()

实例3：获取列表框的当前选项

def show(e):
    listbox.pack(fill=X)

def typeIn(e1):
    enc.delete(0,END)
    enc.insert(0,listbox.get(listbox.curselection()))
from tkinter import *
win = Tk()
v = StringVar()
v.set('重庆 北京 天津 上海 广州 上海 岳阳 长沙 东京 纽约')      #列表中选项内容
s = Scrollbar(win)
s.pack(side=RIGHT,fill=Y)
listbox=Listbox(win,height=2,width=20,relief='solid',listvariable=v,selectbackground='pink',selectmode='single',takefocus=1,yscrollcommand=s.set)
enc = Entry(win)
enc.pack(fill=X)
enc.bind('<Button-1>',show)
listbox.bind('<Double-Button-1>',typeIn)
win.mainloop()

实例4：王者荣耀中有一个功能，玩家在局外编辑的快捷信号，在局内可以快速向其他玩家发送。
本实例实现一个类似于在游戏中编辑快捷信号的功能，并将现有快捷信号显示到系统信号栏中。

def r(e1):
    listbox2.insert(END,listbox1.get(listbox1.curselection()))
    listbox1.delete(listbox1.curselection())

def l(e2):
    listbox1.insert(END,listbox2.get(listbox2.curselection()))
    listbox2.delete(listbox2.curselection())

from tkinter import *
win = Tk()
win.title('添加快捷消息列表')
Label(win,text='系统信号').grid(row=0,column=0,padx=10,pady=6)
Label(win,text='快捷信号').grid(row=0,column=2,padx=10,pady=6)
v = StringVar()
v.set('发起进攻 请求集合 小心草丛 跟着我 开始撤退 清理兵线 回防高地 请求支援')      #列表中选项内容
listbox1=Listbox(win,height=8,width=10,relief='solid',bg='pink',listvariable=v,selectbackground='purple',selectmode='single')
listbox1.grid(row=1,column=0,rowspan=3)
b1=Button(win,text='>>>')
b1.grid(row=1,column=1)
b2=Button(win,text='<<<')
b2.grid(row=3,column=1)
listbox2=Listbox(win,height=8,width=10,relief='solid',bg='green')
listbox2.grid(row=1,column=2,rowspan=3)
b1.bind('<Button-1>',r)
b2.bind('<Button-1>',l)
win.mainloop()

升级版实例4：
def add(e1,e2):

    e2.insert(END,e1.get(e1.curselection()))
    e1.delete(e1.curselection())

from tkinter import *
win = Tk()
win.title('添加快捷消息列表')
win.geometry('250x200')
Label(win,text='系统信号').grid(row=0,column=0,padx=10,pady=6)
Label(win,text='快捷信号').grid(row=0,column=2,padx=10,pady=6)
val1 = StringVar()
val1.set('发起进攻 请求集合 小心草丛 跟着我')      #列表中选项内容
val2 = StringVar()
val2.set('开始撤退 清理兵线 回防高地 请求支援')
listbox1=Listbox(win,height=8,width=10,relief='solid',bg='pink',listvariable=val1,selectbackground='purple',selectmode='single')
listbox1.grid(row=1,column=0,rowspan=2)
b1=Button(win,text='>>>',command=lambda :add(listbox1,listbox2))
b1.grid(row=1,column=1)
b2=Button(win,text='<<<',command=lambda :add(listbox2,listbox1))
b2.grid(row=2,column=1)
listbox2=Listbox(win,height=8,width=10,relief='solid',bg='green',listvariable=val2,selectbackground='purple',selectmode='single')
listbox2.grid(row=1,column=2,rowspan=2)
win.mainloop()
'''
def add(e1,e2):

    e2.insert(END,e1.get(e1.curselection()))
    e1.delete(e1.curselection())

from tkinter import *
win = Tk()
win.title('添加快捷消息列表')
win.geometry('250x200')
Label(win,text='系统信号').grid(row=0,column=0,padx=10,pady=6)
Label(win,text='快捷信号').grid(row=0,column=2,padx=10,pady=6)
val1 = StringVar()
val1.set('发起进攻 请求集合 小心草丛 跟着我')      #列表中选项内容
val2 = StringVar()
val2.set('开始撤退 清理兵线 回防高地 请求支援')
listbox1=Listbox(win,height=8,width=10,relief='solid',bg='pink',listvariable=val1,selectbackground='purple',selectmode='single')
listbox1.grid(row=1,column=0,rowspan=2)
b1=Button(win,text='>>>',command=lambda :add(listbox1,listbox2))
b1.grid(row=1,column=1)
b2=Button(win,text='<<<',command=lambda :add(listbox2,listbox1))
b2.grid(row=2,column=1)
listbox2=Listbox(win,height=8,width=10,relief='solid',bg='green',listvariable=val2,selectbackground='purple',selectmode='single')
listbox2.grid(row=1,column=2,rowspan=2)
v=listbox2.selection_set(0,'end')
print(v)
win.mainloop()