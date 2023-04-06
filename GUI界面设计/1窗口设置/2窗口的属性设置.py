from tkinter import *
win = Tk()
win.title('窗口标题')                 #标题
win.geometry('400x400+200+50')      #设置几何参数：宽x高+起始x坐标+起始y坐标
win.maxsize(600,600)                #设置最大尺寸
win.minsize(100,100)                #设置最小尺寸
win.configure(bg='red')             #设置背景颜色
win.resizable(True,True)            #设置窗口能否改变，True/1表示可以,False/0表示不行
win.state('zoomed')                 #窗口最大化
# win.iconify()                     #窗口最小化
win.iconbitmap('info')              #设置窗口的默认图标:error gray12 gray25 gray50 gray75 hourglass info
win.mainloop()                      #主循环

'''
实例：
from tkinter import *
import time
win = Tk()      #创建窗口
win.title('窗口标题')                 #标题
win.geometry('400x400+200+50')      #设置几何参数：宽x高+起始x坐标+起始y坐标
win.maxsize(600,600)
win.minsize(100,100)
win.configure(bg='red')             #设置背景颜色
colors=['red','yellow','gray','purple','orange']
win.state('zoomed')                 #窗口最大化
win.iconbitmap('info')
for i in range(100):
    win.configure(bg=colors[i%5])
    time.sleep(1)
    win.update()
win.mainloop()
'''
