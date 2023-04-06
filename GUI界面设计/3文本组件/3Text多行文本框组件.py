'''
Text多行文本框件
    方法：
    1.insert()          在文本指定的位置插入内容，insert(INSERT，text) ，INSERT指光标位置，text指内容,
    2.image_create      在指定位置插入图片，image_create(END,image=photo)，先要加载图片photo = PhotoImage(file='head.png')
    3.window_create     创建显示模块和按钮控件在Text上，同2方法一样。运用window=label,button的方式。

    常见方法
    4.get()             获得Text文本的值，如get(1.2,1.8)获得第一行的第3个字符到第9个字符的值，包头不包尾
    5.delete()          删除组件中的内容
    6.mark_set()        添加标记
    7.search()          搜索文本
    8.edit_undo()/edit_redo()       撤消操作恢复操作
    9.edit_separator()  添加分割线，添加分割线后，再进行摊销操作时，不会撤销所有操作，只是撤销上一次操作
    Text组件的索引
    index()           用于指定Text组件中文本的位置和索引一样，文本索引通常为字符串类型，并且指定Text的索引方式有以下几种
                        1.line.column:这种方式将索引位置的行号和列号以字符串的形式表示'2.3'
                        2.insert：插入光标位置
                        3.end:最后一个字符的位置，line.end表示几行的最后一个字符位置
                        4.+count chars:指定位置向后移count个字符。例如'2.1+2 chars'表示第2行第4个字符的位置。
                        5.-count chars:指定位置向前移count个字符。例如'2.3-2 chars'表示第2行第2个字符的位置。
                        注：Text中第一行的索引：1，第一列的索引为0

实例：1.insert() 2.image_create  3.window_create
i=0
def hit():
    global i
    i += 1
    label.config(text='你点击了我%s下'%i)

from tkinter import *
root = Tk()
text = Text(root,width=45,height=10,bg='#CAE1FF',relief='solid')
photo = PhotoImage(file='head.png')
text.image_create(END,image=photo)
text.insert(INSERT,'在这里添加文本：\n')
text.pack()
bt = Button(root,text='你点击我试试',command=hit,padx=10)
text.window_create('2.end',window=bt)
label=Label(root,padx=10,text='你点了我0下')
text.window_create('3.end',window=label)
root.mainloop()

4.get(),.index()
实例
from tkinter import *
win = Tk()
text = Text(win)
text.insert(INSERT,'I love pthon')
text.pack()
print(text.get(1.2))
win.mainloop()

实例： 6.mark_set()/mark_unset()        添加/取消标记    7.search()          搜索文本
8.edit_undo()/edit_redo() 撤消操作恢复操作 9.edit_separator()    添加分割线
from tkinter import *
root = Tk()
def undo1(e):
    text.edit_undo()
def redo1(e):
    text.edit_redo()
def callback(e):
    text.edit_separator()       #每次按键都会添加一个分割线，否则会撤销和恢复所有内容。
text = Text(root,width=50,height=30,undo=True,autoseparators=False)
text.pack()
text.insert(INSERT,'在下方可以添加文本，通过键盘<Ctrl+Z>撤销操作和<Ctrl+Y>键恢复操作：\n\n')
text.bind('<Key>',callback)
text.bind('<Control-Z>',undo1)
text.bind('<Control-Y>',redo1)
text.mark_set('aaa',1.4)
text.insert('aaa','王')
text.insert('aaa','sf')
text.insert('aaa','9')
v = text.search('文',1.1,'end')
print(v)
root.mainloop()
'''
from tkinter import *
root = Tk()
def undo1(e):
    text.edit_undo()
def redo1(e):
    text.edit_redo()
def callback(e):
    text.edit_separator()       #每次按键都会添加一个分割线，否则会撤销和恢复所有内容。
text = Text(root,width=50,height=30,undo=True,autoseparators=False)
text.pack()
text.insert(INSERT,'在下方可以添加文本，通过键盘<Ctrl+Z>撤销操作和<Ctrl+Y>键恢复操作：\n\n')
text.bind('<Key>',callback)
text.bind('<Control-Z>',undo1)
text.bind('<Control-Y>',redo1)
text.mark_set('aaa',1.4)
text.insert('aaa','333')
text.insert('aaa','sf')
text.insert('aaa','9')
v = text.search('文',1.1,'end')
print(v)
root.mainloop()