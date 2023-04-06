import sys
from tkinter import *
def qidong():
    zh=e1.get()
    mm=e2.get()
    if zh=='mark' and mm=='123':
        print('启动游戏')
        youxi()
    else:
        print('登陆失败')

def youxi():
    import pygame
    screen=pygame.display.set_mode((800,600))   #surface/rect
          #scratch.显示.制作屏幕（大小）
    while True:
        #获取很多事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill('red')
        pygame.display.update()
        #pygame.显示.刷新
win = Tk()      #创建界面
win.title('游戏中心')
Label(win,text='账号').grid(row=0,column=0)
Label(win,text='密码').grid(row=1,column=0)
e1=Entry(win)           #单行文本组件
e1.grid(row=0,column=1)
e2=Entry(win,show='*')           #单行文本组件
e2.grid(row=1,column=1)
Button(win,text='登陆',command=qidong).grid(row=2,columnspan=2)
win.mainloop()

