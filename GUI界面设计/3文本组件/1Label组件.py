'''
Label组件的基本使用
    参数：
    1.justify               设置最后一行文本的对齐方式，左对齐left,右对齐right,居中center
    2.image                 添加图片，需要先创建图片对象PhotoImage(file='png')
    3.compound              设置Label中有图片和文字的显示位置：top,bottom,left,right图片位于文字上、下、左、右，center图片在文字上
    4.jpg格式图片             pip install pillow
    5.wraplength            设置每行的限定像素。
实例：1.justify               设置最后一行文本的对齐方式，左对齐left,右对齐right,居中center
from tkinter import *
win=Tk()
str = '\n上海一大哥很帅\n下跪关公只求义\n顺风顺水'
Label(win,text=str,justify='right',font=14,bg='pink').pack(ipadx=10,ipady=5)
win.mainloop()

实例：2.image              添加图片，需要先创建图片对象PhotoImage(file='png')
from tkinter import *
win=Tk()
ima1=PhotoImage(file='Castle 2.png')
Label(win,image=ima1).pack()
win.mainloop()

实例:3.compound   设置Label中有图片和文字的显示位置：top,bottom,left,right图片位于文字上、下、左、右，center图片在文字上
from tkinter import *
win=Tk()
str = '小猫城堡'
ima1=PhotoImage(file='Castle 2.png')
Label(win,image=ima1,text=str,compound='center').pack()
win.mainloop()

实例：兑奖
from tkinter import *
win=Tk()
win.title('欢乐写数字')
win.configure(bg='#eef3c3')
ima1=PhotoImage(file='Castle 2.png')
Label(win,image=ima1,text='欢乐写数字',compound='bottom',font='楷体 20 bold').grid(row=2,column=0,columnspan=2)
Label(win,text='输入兑奖码领取稀有道具',bg='#eef3c3').grid(row=3,column=0,columnspan=2)
Label(win,text='兑奖码',font=14,bg='#eef3c3').grid(row=4,column=0,sticky=E,pady=10)
Label(win,width=15,bg='#fff',relief='groove').grid(row=4,column=1,pady=10)
Label(win,text='确认兑换',width=20,relief='groove',bg='#0996ed').grid(row=5,column=0,columnspan=2,pady=5)
win.mainloop()

实例：.添加jpg格式图片
先pip install pillow,再用Image打开图片，v = Image.open(图片)，再用ImageTk转换图片。ima1=ImageTk.PhotoImage(v)
from tkinter import *
from PIL import Image,ImageTk
win=Tk()
win.title('欢乐写数字')
win.configure(bg='#eef3c3')
im = Image.open('1.jpg')
ima1=ImageTk.PhotoImage(im)
Label(win,image=ima1,text='欢乐写数字',compound='bottom',font='楷体 20 bold').grid(row=2,column=0,columnspan=2)
Label(win,text='输入兑奖码领取稀有道具',bg='#eef3c3').grid(row=3,column=0,columnspan=2)
Label(win,text='兑奖码',font=14,bg='#eef3c3').grid(row=4,column=0,sticky=E,pady=10)
Label(win,width=15,bg='#fff',relief='groove').grid(row=4,column=1,pady=10)
Label(win,text='确认兑换',width=20,relief='groove',bg='#0996ed').grid(row=5,column=0,columnspan=2,pady=5)
win.mainloop()

5.wraplength            设置每行的限定像素。
可用作指定位置换行。
实例：
from tkinter import *
win=Tk()
win.title('欢乐写数字')
win.configure(bg='#C9EDEB')
win.maxsize(500,500)
couple = '上联：足不出户一台电脑打天下下联：窝宅在家一双巧手定乾坤横批：量我风采'
txt=Label(win,text=couple,bg='#C9EDEB',font=14,wraplength=230,justify='left')
txt.grid(padx=20,pady=20)

win.mainloop()
'''
from tkinter import *
win=Tk()
win2=Tk()
win.title('欢乐写数字')
win.configure(bg='#C9EDEB')
win.maxsize(500,500)
couple = '上联：足不出户一台电脑打天下下联：窝宅在家一双巧手定乾坤横批：量我风采'
txt=Label(win,text=couple,bg='#C9EDEB',font=14,wraplength=230,justify='left')
txt.grid(padx=20,pady=20)

win.mainloop()