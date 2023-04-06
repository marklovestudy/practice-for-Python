'''
Entry属性：
    1.show              可以用来隐藏数据如show='*'

Entry方法：
    1.get()             获取文本中的内容
    2.insert()          在文本指定的位置插入内容，insert(index，str) ，index指位置，str指内容
    3.delete()          删除文本框中指定的内容，delete(first,end),包头不包尾

实例：出发地和目的地
from tkinter import *
win = Tk()
Label(win,text='出发地：',font=14).grid(pady=10,row=0,column=0)
Entry(win).grid(row=0,column=1)
Label(win,text='目的地：',font=14).grid(pady=10,row=1,column=0)
Entry(win).grid(row=1,column=1)
win.mainloop()

 1.show              可以用来隐藏数据如show='*'
实例：账号密码登陆
from tkinter import *
win = Tk()
Label(win,text='账号：',font=14).grid(pady=10,row=0,column=0)
Entry(win).grid(row=0,column=1)
Label(win,text='密码：',font=14).grid(pady=10,row=1,column=0)
Entry(win,show='*').grid(row=1,column=1)
win.mainloop()

from tkinter import *
win = Tk()
user = PhotoImage(file = 'head.png')
passward = PhotoImage(file = 'pawd.png')
Label(win,image=user,text='账号：',font=14,compound = 'left').grid(pady=10,row=0,column=0)
Entry(win).grid(row=0,column=1)
Label(win,image=passward,text='密码：',font=14,compound = 'left').grid(pady=10,row=1,column=0)
Entry(win,show='*').grid(row=1,column=1)
win.mainloop()

1.get()             获取文本中的内容
from tkinter import *
win = Tk()
def show():
    str=entry.get()
    print(str)
entry=Entry(win)
entry.grid(row=0)
Button(win,text='显示',command=show).grid(row=0,column=1)
win.mainloop()

2.insert()          在文本指定的位置插入内容，insert(index，str) ，index指位置，str指内容
from tkinter import *
win = Tk()
Label(win,text='用户名：').grid(row=0,column=0)
entry=Entry(win,relief='groove')
entry.insert(0,'admin')
entry.grid(row=0,column=1)
win.mainloop()

3.delete()          删除文本框中指定的内容，delete(first,end),包头不包尾
from tkinter import *
win = Tk()
def back():
    length=len(op1.get())
    op1.delete(length-1,END)
op1=Entry(win,relief='groove')
op1.insert(INSERT,'春风又绿江南岸')
op1.grid(row=0)
Button(win,text='后退',command=back).grid(row=0,column=1)
win.mainloop()

from tkinter import *
win = Tk()
win.configure(bg='yellow')
def add():
    re.delete(0,END)
    add1=op1.get()
    add2=op2.get()
    re.insert(INSERT,eval(add1)+eval(add2))
op1=Entry(win,width=5,relief='groove')
op1.grid(row=0,pady=20)
Label(win,text='+',bg='#F3E4A4').grid(row=0,column=1)
op2=Entry(win,width=5,relief='groove')
op2.grid(row=0,column=2)
Label(win,text='=',bg='#F3E4A4').grid(row=0,column=3)
re=Entry(win,width=5,relief='groove')
re.grid(row=0,column=4)
Button(win,text='计算',command=add,relief='groove',bg='#10C9F5').grid(row=1,columnspan=5,ipadx=10)
win.mainloop()
'''
from tkinter import *
win = Tk()
win.configure(bg='yellow')
def add():
    re.delete(0,END)
    add1=op1.get()
    add2=op2.get()
    re.insert(INSERT,eval(add1)+eval(add2))
op1=Entry(win,width=5,relief='groove')
op1.grid(row=0,pady=20)
Label(win,text='+',bg='#F3E4A4').grid(row=0,column=1)
op2=Entry(win,width=5,relief='groove')
op2.grid(row=0,column=2)
Label(win,text='=',bg='#F3E4A4').grid(row=0,column=3)
re=Entry(win,width=5,relief='groove')
re.grid(row=0,column=4)
Button(win,text='计算',command=add,relief='groove',bg='#10C9F5').grid(row=1,columnspan=5,ipadx=10)
win.mainloop()