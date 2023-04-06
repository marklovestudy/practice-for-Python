'''
    1.justify               设置最后一行文本的对齐方式，左对齐left,右对齐right,居中center
    2.image                 添加图片，需要先创建图片对象PhotoImage(file='png')
    3.compound              设置Label中有图片和文字的显示位置：top,bottom,left,right图片位于文字上、下、左、右，center图片在文字上
    4.jpg格式图片             pip install pillow
    5.wraplength            设置每行的限定像素。
    6.ipadx                      文本和组件边缘的水平间距
    7.ipady                      文本和组件边缘的垂直间距
    8.text                      文本内容
'''
from tkinter import *
win=Tk()
str = '点我试试'
ima1=PhotoImage(file='11.png')
Label(win,text=str,image=ima1,compound='center',font='黑体 24 bold',fg='red').pack()
x=100
y=100
x_v=0.1
y_v=0.1
while True:
    win.geometry('120x120+%d+%d'%(x,y))
    win.update()
    if x > 1200 or x < 0 :
        x_v=-x_v
    if y > 600 or y < 0 :
        y_v=-y_v
    x+=x_v
    y+=y_v
win.mainloop()