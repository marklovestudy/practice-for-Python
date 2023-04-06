def max_win(event):
    win.geometry('600x400')

def normal_win(event):
    win.geometry('300x200')


def txt():
    global val,font_size,top
    top=Toplevel(win)
    val=StringVar()
    val.set('宋体')
    font_family=('宋体','黑体','方正舒体','楷体','隶书','方正姚体')
    family = Combobox(top,textvariable=val,values=font_family)
    family.grid(row=0,column=0)
    font_size=Spinbox(top,from_=12,to=30,increment=2,width=10)
    font_size.grid(row=0,column=1)
    btn1=Button(top,text='确定',command=font_set)
    btn1.grid(row=1,column=1)

def font_set():
    font1=(val.get(),font_size.get())
    label.config(font=font1)
from tkinter import *
from tkinter.ttk import *
win=Tk()
win.geometry('300x200')
menu1=Menu(win)                                 #创建一级菜单
menu2_1=Menu(menu1,tearoff=False)               #设置菜单能否从窗口中分离(默认值为True)
menu1.add_cascade(label='窗体',menu=menu2_1)     #给一级菜单中的‘城市’添加一个父菜单，menu2_1
menu2_1.add_command(label='最大化',accelerator='Ctrl+UP',command=lambda :max_win(''))
menu2_1.add_command(label='中等窗口',accelerator='Ctrl+DOWN',command=lambda :normal_win(''))             #给menu2_1添加命令菜单项
menu2_1.add_command(label='最小化',command=win.iconify)
menu2_1.add_separator()                         #添加分割线
menu2_1.add_command(label='关闭',command=win.quit)

menu2_2=Menu(menu1,tearoff=False)
menu1.add_cascade(label='自定义',menu=menu2_2)
menu2_2.add_command(label='文字设置',command=txt)
win.config(menu=menu1)

label=Label(win,text='这是一个窗口')
label.grid(row=0,column=0)
win.bind_all('<Control-Up>',max_win)
win.bind_all('<Control-Down>',normal_win)
win.mainloop()