'''
Frame组件，如果组件比较多。管理起来比较麻烦，这时候可以用Frame容器组件来分类管理。
1实例：设置鼠标停在Frame组件上的样式
from tkinter import *
win = Tk()
win.geometry('360x180')
for i in range(6):
    if i%2 == 0:
        Frame(win,width=60,height=40,bg='red',cursor='cross').grid(row=0,column=i,pady=20)
    else:
        Frame(win,width=60,height=40, bg='yellow',cursor='plus').grid(row=0,column=i,pady=20)
win.mainloop()

实例：把一个Label组件和一组单选按钮位置放置在同一个Frame组件中。
from tkinter import *
win = Tk()
win.geometry('360x120')
def c():
    print(v.get())
box=Frame(win,width=100,height=100,relief='groove',borderwidth=5)
box.grid(row=0,column=0,padx=10,pady=10)
txt='小明去钓鱼，结果6条无头，8条只有半个身子，9条无尾，请问小明一共钓了几条鱼？'
Label(box,text=txt,wraplength=320,justify='left',font=14).grid(columnspan=4)
select=['8条','6条','9条','0条']
v = StringVar()
for i in range(len(select)):
    Radiobutton(box,text=select[i],value=i,variable=v,command=c).grid(row=1,column=i)
win.mainloop()

2实例：使用Frame组件实现显示地铁信息的功能
from tkinter import *
from tkinter.ttk import *           #因为要使用ttk模块中的分割线，所以引入ttk模块
win = Tk()
win.title('珠海地铁一号线')
win.configure(bg='#AFEBE5')
win.geometry('250x200')
sty1=Style()            #创建对象sty1
sty1.configure('BW.TLabel',foreground='yellow',background='red')        #设定对象sty1的参数，取名为'BW.TLabel'
sty2=Style()             #创建对象sty2
sty2.configure('BW.TFrame',background='#AFEBE5')                        #设定对象sty1的参数，取名为'BW.TFrame'

left=Frame(win,style='BW.TLabel',width=260)
left.pack(side='left')
Label(left,text='2022-12-30',background='red',foreground='#fff').pack()
Label(left,text='08:56',background='red',foreground='#fff').pack()
Label(left,text='星期一,sun',background='red',foreground='#fff').pack()
Separator(left,orient=HORIZONTAL).pack(side=TOP,fill=X)         #分割线

Label(left,text='本站',background='red',foreground='#fff').pack(ipady=5)
Label(left,text='华润万家',background='red',foreground='#fff').pack(ipady=5)
Separator(left,orient=HORIZONTAL).pack(side=TOP,fill=X)         #分割线

Label(left,text='下一站',background='red',foreground='#fff').pack(ipady=5)
Label(left,text='明珠北',background='red',foreground='#fff').pack(ipady=5)

right=Frame(win,style='BW.TFrame',width=260)
right.pack(side='left')
Label(right,text='请排队上下车先下后上',background='#AFEBE5',justify='center',wraplength=100,font=16).pack(padx=40)
win.mainloop()

3在Frame组件中添加单选按钮与复选框
通过全选与反选功能的实例，来演示Frame组件的使用方法
实例：实现全选，全不选，反选功能
    在窗口中添加两个容器，第一个容器中添加全选、反选与全不选这3个单选按钮，第二个容器中添加各复选框。具体步骤如下：
    1首先在文件中添加两个Frame组件，分别放置单选按钮与复选框，，具体代码如下：
#全选
def al():
    for index,item in enumerate(checkbox):
        item.set(True)
#全不选
def no():
    for index,item in enumerate(checkbox):
        item.set(False)
#反选
def inverse():
    for index,item in enumerate(checkbox):
        if item.get() == False:
            item.set(True)
        else:
            item.set(False)

from tkinter import *
win = Tk()
win.title('珠海地铁一号线')

f1=Frame(win,width=200,height=50)
f1.grid(row=0,column=0)
f2=Frame(win,width=200,height=50)
f2.grid(row=1,column=0)
v=BooleanVar()              #定义一个tkinter模块变量，用于单选框按钮绑定该变量
v.set(1)
r1=Radiobutton(f1,value=0,variable=v,text='全选',command=al)
r1.grid(row=0,column=0)
r2=Radiobutton(f1,value=1,variable=v,text='全不选',command=no)
r2.grid(row=0,column=1)
r3=Radiobutton(f1,value=2,variable=v,text='反选',command=inverse)
r3.grid(row=0,column=2)

fruits=['苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝']
checkbox=[]
for index,item in enumerate(fruits):
    str1=BooleanVar()
    str1.set(False)
    Checkbutton(f2,text=item,variable=str1).grid(row=index+1,column=1)      #复选框的值为True表示选择，False表示不选
    checkbox.append(str1)
win.mainloop()
'''
#全选
def al():
    for index,item in enumerate(checkbox):
        item.set(True)
#全不选
def no():
    for index,item in enumerate(checkbox):
        item.set(False)
#反选
def inverse():
    for index,item in enumerate(checkbox):
        if item.get() == False:
            item.set(True)
        else:
            item.set(False)

from tkinter import *
win = Tk()
win.title('珠海地铁一号线')

f1=Frame(win,width=200,height=50)
f1.grid(row=0,column=0)
f2=Frame(win,width=200,height=50)
f2.grid(row=1,column=0)
v=BooleanVar()  #定义一个tkinter模块变量，用于单选框按钮绑定该变量
v.set(1)
r1=Radiobutton(f1,value=0,variable=v,text='全选',command=al)
r1.grid(row=0,column=0)
r2=Radiobutton(f1,value=1,variable=v,text='取消全选',command=no)
r2.grid(row=0,column=1)
r3=Radiobutton(f1,value=2,variable=v,text='反选',command=inverse)
r3.grid(row=0,column=2)

fruits=['苹果','香蕉','梨','葡萄','圣女果','百香果','菠萝']
checkbox=[]
for index,item in enumerate(fruits):
    str1=BooleanVar()
    str1.set(False)
    Checkbutton(f2,text=item,variable=str1).grid(row=index+1,column=1)      #复选框的值为True表示选择，False表示不选
    checkbox.append(str1)
win.mainloop()
