#1做一个输入显示框
#2做十个输入按钮
#3四个+-*/=
from tkinter import *
win=Tk()
def wi(a):
    if a in list1[:-2]:       #如果输入的是0123456789+-*/
        e1.insert('end',a)    #把内容插入到单行文本的最后面
    elif a == 'X':            #如果点击的是X后退
        e1.delete(len(e1.get())-1,'end')  #删除最后一个字符：起始位置：文本长度-1，结束位置：最后
    elif a == '=':          #如果按键是=号，计算结果
        str1=eval(e1.get())    #把提取字符串，相当于计算，str1为计算结果
        e1.delete(0,'end')      #删除全部，超始位置为：最开头，结束位置为：最后
        e1.insert('end',str(str1))  #在单行文本e1最后插入前面的计算结果：str1
def cb(n,fc,row,column):    #创建按键函数，目的是创建局部变量函数调用不同值的问题
    Button(win, text=list1[n], command=lambda :fc(list1[n])).grid(row=row, column=column, sticky=W + E)
    return list1[n]     #创建按钮，设置按钮。设置返回值为list1[n]
e1=Entry(win);e1.grid(row=0,columnspan=4)
list1=['0','1','2','3','4','5','6','7','8','9','+','-','*','/','=','X']
n=0
for row in range(1,5):
    for column in range(4):
        cb(n,wi,row,column)
        n+=1
win.mainloop()
