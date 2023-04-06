'''
Spinbox组件的基本使用
    Spinbox组件可以理解为Entry组件的变体，可用于在多个固定值中选取一个，而固定值可以是数字，
    也可以是汉字。
    1、当定义可选值为数字时，其语法如下：
    Spinbox(win,from_=n1,to=n2)
    其中，win为该组件的父容器；from_(一定要区别于关键字from)为数值的下限；to为数值的上限，即规定数值范围为n1~n2。
    2、当定义值为汉字时，可以通过values指定可选择的值，其值可以为元组、列表等，具体代码如下：
    Spinbox(win,values=('西瓜','香蕉','苹果','草莓')).pack()

实例：实现游戏中购买道具窗口
from tkinter import *
win=Tk()
win.title('购买道具')
Label(win,text='购买道具：').grid(row=0,column=0,pady=10)
Spinbox(win,values=('绿水晶','红宝石','生命水')).grid(row=0,column=1,pady=10)
Label(win,text='购买数量：').grid(row=1,column=0,pady=10)
Spinbox(win,from_=1,to=5).grid(row=1,column=1,pady=10)
Label(win,text='限购5件').grid(row=1,column=2,pady=10)
Label(win,text='支付方式：').grid(row=2,column=0,pady=10)
Spinbox(win,values=('金币','钻石','点卷')).grid(row=2,column=1,pady=10)
win.mainloop()

Spinbox组件的相关属性介绍：
    1,activebackground              当Spinbox处于"active"(积极主动的，活跃的)状态下背景颜色
    2,buttonbackground              箭头的背景色
    3,buttoncursor                  鼠标悬停在箭头上时的样式arrow, circle, cross, plus
    4,command                       当用户通过箭头调节内容时，调用某个函数
    5,disabledbackground            当Spinbox处于'disabled'状态时的背景颜色
    6,disabledforeground            当Spinbox处于'disabled'状态时的前景颜色
    7,exportselection               指定选中的文本是否可以复制到前切板
    8,increment                     单击箭头时，Spinbox递增或递减的数值
    9,justify                       Spinbox内文本的对齐方式
    10,readonlybackground           Spinbox处于'readonly'状态时的背景颜色
    11,state                        设置Spinbox组件的状态，可选的值有'normal'(默认值)、'disabled'(完全禁止)、'readonly'(只读，可以被选中和拷贝)
    12,textvariable                 指定一个与输入框的内容相关联的tkinter模块中的变量(通常是StringVar()),当输入框的内容发生改变时，该变量的值也会相应发生改变
    注：如果state设置了'disabled'和'readonly'，那么insert()方法和delete()方法无效。

实例：布局购买道具窗口，并且计算花费的金币
from tkinter import *
win=Tk()
mon=5
def typ():
    global mon
    print(val.get())
    if val.get()=='绿水晶':
        mon = 5
    elif val.get()=='红宝石':
        mon=10
    else:
        mon=15

def pay():
    print(num.get(),type(num.get()))
    number = int(num.get())
    tatal = number*mon
    text1 = '选购'+val.get()+'总价'+str(tatal)+'金币'
    label.config(text = text1)

win.title('购买道具')
Label(win,text='购买道具：').grid(row=0,column=0,pady=10)
val = StringVar()
Spinbox(win,values=('绿水晶','红宝石','生命水'),textvariable=val,command=typ).grid(row=0,column=1,pady=10)       #1、Spinbox的选值==val.get(),和#2效果一样
Label(win,text='购买数量：').grid(row=1,column=0,pady=10)
num = Spinbox(win,from_=1,to=5,command=pay)         #2、num.get()获得的值是Spinbox选值为str
num.grid(row=1,column=1,pady=10)
Label(win,text='限购5件').grid(row=1,column=2,pady=10)
label=Label(win)
label.grid(row=3,column=0,columnspan=3,pady=10)
win.mainloop()

Spinbox组件的相关方法：
    1,get()                                 获得Spinbox当前的值
    2,insert(index,text)                    将text参数的内容插入到index参数指定的位置
    3,selection('from',index)               设置选中范围的起始位置是index参数指定的值
    4,selection('to',index)                 设置选中范围的结束位置是index参数指定的值
    5,selection('range',start,end)          设置选中范围是start到end参数之间的值
    6,selection_element(element=None)       设置或获取选择范围

实例：留言本，用户写完留言，点击提交，自动保存，并把日期写在后面。
from tkinter import *
win=Tk()
win.title('留言本')

def show():
    if spmon.get() in '13578' or spmon.get() == '10' or spmon.get() == '12':
        spday.config(to=31)
    elif spmon.get() == '2':
        spday.config(to=28)
    else:
        spday.config(to=30)

def showw():
    text1.insert('insert','\t时间：%s月%s日%s\n'%(spmon.get(),spday.get(),spweek.get()))
Label(win,text='请添加您的留言').grid(row=0,column=0,columnspan=5,pady=10)
spmon=Spinbox(win,from_=1,to=12,width=10,command = show)
spmon.grid(row=1,column=0,pady=10)
Label(win,text='月').grid(row=1,column=1,pady=10)
spday=Spinbox(win,from_=1,to=30,width=10,command=show)
spday.grid(row=1,column=2,pady=10)
Label(win,text='日').grid(row=1,column=3,pady=10)
spweek = Spinbox(win,values=('星期一','星期二','星期三','星期四','星期五','星期六','星期日'),width=10,command = show)
spweek.grid(row=1,column=5,columnspan=3,pady=10)
text1 = Text(win,width = 50,height =10,bg = '#BFEFFF')
text1.grid(row=2,columnspan=10)
Button(win,text='提交',width=30,bg='pink',command = showw).grid(row=3,columnspan=10,pady=10)
win.mainloop()
'''
from tkinter import *
win=Tk()
win.title('留言本')

def show():
    if spmon.get() in '13578' or spmon.get() == '10' or spmon.get() == '12':
        spday.config(to=31)
    elif spmon.get() == '2':
        spday.config(to=28)
    else:
        spday.config(to=30)

def showw():
    text1.insert('insert','\t时间：%s月%s日%s\n'%(spmon.get(),spday.get(),spweek.get()))
Label(win,text='请添加您的留言').grid(row=0,column=0,columnspan=5,pady=10)
spmon=Spinbox(win,from_=1,to=12,width=10,command = show)
spmon.grid(row=1,column=0,pady=10)
Label(win,text='月').grid(row=1,column=1,pady=10)
spday=Spinbox(win,from_=1,to=30,width=10,command=show)
spday.grid(row=1,column=2,pady=10)
Label(win,text='日').grid(row=1,column=3,pady=10)
spweek = Spinbox(win,values=('星期一','星期二','星期三','星期四','星期五','星期六','星期日'),width=10,command = show)
spweek.grid(row=1,column=5,columnspan=3,pady=10)
text1 = Text(win,width = 50,height =10,bg = '#BFEFFF')
text1.grid(row=2,columnspan=10)
Button(win,text='提交',width=30,bg='pink',command = showw).grid(row=3,columnspan=10,pady=10)
win.mainloop()