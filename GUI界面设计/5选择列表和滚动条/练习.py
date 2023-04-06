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