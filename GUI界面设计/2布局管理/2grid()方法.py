'''
grid()方法中的参数：
    1.row               组件所在的行
    2.column            组件所在的列
    3.rowspan           组件横向合并的行数
    4.columnspan        组件纵向合并的列数
    5.sticky            组件填充所分配空间空白区域的方式
    6.padx,pady         组件距离窗口边界的水平和垂直方向的距离

1、2、row,column          定义组件的行和列，默认值为row=0,column=0，而单元格的大小取决于最大的组件的宽度。
实例:九九乘法口决表
from tkinter import *
win = Tk()
win.title('乘法口决表')
for i in range(1,10):
    for j in range(i,10):
        Button(win,text='%s * %s = %s'%(i,j,i*j),bg='pink').grid(row=j,column=i,padx=10)
win.mainloop()

3、4、rowspan,columnspan  组件横向合并列数和纵向合并的行数
from tkinter import *
win = Tk()
win.title('乘法口决表')
l = ['red','yellow','pink','gray','purple','white','brown','green','aqua','aquamarine']
for i in range(1,10):
    for j in range(i,10):
        Button(win,text='%s * %s = %s'%(i,j,i*j),bg=l[i],width=9).grid(row=j,column=i,padx=40,pady=20,rowspan=2,columnspan=2)
win.mainloop()
注：合并行和列只会增加占用的空间(行数和列数),而不会增大组件本身的大小如：width=9

5、sticky:组件填充所分配空间空白区域的方式,其功能与anchor类似，不过它只有4个可选参数，即N(上对齐)、S(下对齐)、W(左对齐)、E(右对齐)。
实例：
from tkinter import *
win = Tk()
Label(win,text='春花秋月何时了',bg='pink',relief='groove').grid(row=0,column=0)
Label(win,text='行事知多少',bg='pink',relief='groove').grid(row=1,column=0,sticky=W)
win.mainloop()
sticky:支持组合使用：sticky=N+S,sticky=N+S+W,sticky=N+S+W+E
实例：
from tkinter import *
win = Tk()
Label(win,text='春花秋月何时了',bg='pink',relief='groove').grid(row=0,column=0)
Label(win,text='行事知多少',bg='pink',relief='groove').grid(row=1,column=0,sticky=W+E)
win.mainloop()

6、padx和pady,设置组件距离窗口的距离,单位px分辨率

rowconfigure()方法和columnconfigure()方法设置组件的缩放比例：
    tkinter窗口默认情况下是可以通过鼠标拖动来改变窗口的大小的，而当窗口大小被改变时，
    可以通过rowconfigure()方法和columnconfigure()方法设置组件行和列的缩放比例。

实例：
from tkinter import *
win = Tk()
win.rowconfigure(0,weight=1)            #前面的0表示0行，后面的weight表示放大占父容器的行比例
win.columnconfigure(1,weight=1)         #面的1表示1列，后面的weight表示放大占父容器的列比例
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=0,column=0,sticky=W+N)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=0,column=1,sticky=E+N)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=1,column=0,sticky=S+W)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=1,column=1,sticky=S+E)
win.mainloop()
注：rowconfigure()和columnconfigure()方法是设置在父容器上而并非设置在组件上，这一点要尤为注意
from tkinter import *
win = Tk()
win.rowconfigure(0,weight=1)                #设置和不设置的区别
win.columnconfigure(1,weight=1)             #设置和不设置的区别
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=0,column=0,sticky=W+N)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=0,column=1,sticky=E+N)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=1,column=0,sticky=S+W)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=1,column=1,sticky=S+E)
win.mainloop()
'''
from tkinter import *
win = Tk()
win.rowconfigure(0,weight=1)
win.columnconfigure(0,weight=1)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=0,column=0,sticky=W+N)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=0,column=1,sticky=E+N)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=1,column=0,sticky=S+W)
Label(win,width=15,height=2,bg='pink',relief='groove').grid(row=1,column=1,sticky=S+E)
win.mainloop()

from tkinter import *
import random as r
win = Tk()
win.title('成绩表')
names = ['同学'+str(i) for i in range(1,16)]
obj = ['姓名/科目','外语','数学','专业','政治','总分']
names_y=[]
for i in range(len(obj)):
    Label(win,text=obj[i],bg='pink',font='黑体 20 bold').grid(row=0,column=i)
for j in range(1,len(names)+1):
    Label(win, text=names[j-1], bg='pink',font='黑体 20 bold').grid(row=j, column=0,sticky=W+E)
for t in range(1,16):
    s = 0
    for k in range(1,5):
        if k == 1 or k== 4:
            v = r.randint(0,100)
        if k == 2 or k== 3:
            v = r.randint(0, 150)
        Label(win,text=str(v),bg='pink',font='黑体 20 bold').grid(row=t,column=k,sticky=W+E)
        s += v
    Label(win, text=str(s), bg='pink',font='黑体 20 bold').grid(row=t, column=k+1,sticky=W+E)
    if s >= 300:
        names_y.append(names[t-1])
Label(win,text='本届研究生录取名单：'+' '.join(names_y),wraplength=400,bg='red',font='黑体 20 bold').grid(row=16,columnspan=6,sticky=W+E)
win.mainloop()
