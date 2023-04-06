'''
LabelFrame标签框架组件，显示一个标题，把一系列相关联的组件放置在一个容器内，默认情况下，它会绘制边框将子组件包围，并且为其显示一个标题。
语法如下：
LabelFrame(win,text='标题')
如：将一组单选框放在一个LabelFrame组件中。具休代码如下：
from tkinter import *
win=Tk()
def show():
    print(hero.get())
lf=LabelFrame(win,text='选择你的出战英雄')
lf.grid(row=0,column=1,ipadx=10,ipady=10)
hero=StringVar()
hero.set('貂蝉')
Radiobutton(lf,variable=hero,text='貂蝉',value='貂蝉',command=show).grid(row=1,column=1)
Radiobutton(lf,variable=hero,text='吕布',value='吕布',command=show).grid(row=2,column=1)
Radiobutton(lf,variable=hero,text='小乔',value='小乔',command=show).grid(row=3,column=1)
Radiobutton(lf,variable=hero,text='周瑜',value='周瑜',command=show).grid(row=4,column=1)
win.mainloop()

实例：在礼包兑换窗口中，将游戏图标，输入兑换码的文本以及兑换按钮放置在LabelFrame组件中，具体代码如下：

def duihuan():
    txt=entry.get()
    if len(txt)>0:
        re.config(text=txt+'兑换成功！')
    else:
        re.config(text='兑换码无效')
    re.grid(row=4,column=2)

from tkinter import *
win=Tk()

lf=LabelFrame(win,text='礼品兑换',bg='yellow',padx=20,pady=10,font=14)
lf.grid(row=0,column=1,ipadx=10,ipady=10)

ima1=PhotoImage(file='head.png')
Label(lf,image=ima1,bg='yellow').grid(row=1,column=2)
Label(lf,text='兑换码：',bg='yellow').grid(row=2,column=1,pady=10)
entry=Entry(lf)
entry.grid(row=2,column=2,pady=10)
Button(lf,text='确认兑换',bg='blue',borderwidth=1,command=duihuan).grid(row=3,column=2)
re=Label(lf,bg='yellow',font=16,fg='red')

win.mainloop()
'''

def duihuan():
    txt=entry.get()
    if len(txt)>0:
        re.config(text=txt+'兑换成功！')
    else:
        re.config(text='兑换码无效')
    re.grid(row=4,column=2)

from tkinter import *
win=Tk()

lf=LabelFrame(win,text='礼品兑换',bg='yellow',padx=20,pady=10,font=14)
lf.grid(row=0,column=1,ipadx=10,ipady=10)

ima1=PhotoImage(file='head.png')
Label(lf,image=ima1,bg='yellow').grid(row=1,column=2)
Label(lf,text='兑换码：',bg='yellow').grid(row=2,column=1,pady=10)
entry=Entry(lf)
entry.grid(row=2,column=2,pady=10)
Button(lf,text='确认兑换',bg='blue',borderwidth=1,command=duihuan).grid(row=3,column=2)
re=Label(lf,bg='yellow',font=16,fg='red')

win.mainloop()