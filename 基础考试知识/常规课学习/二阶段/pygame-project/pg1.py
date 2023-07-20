import sys
import pygame
#1在CMD里面pip install pygame   (pip 需要更新：python -m pip install --upgrade pip)
#2pycharm--文件--设置--解释器--下面是已经安装库--+搜索pygame--左下安装软件
#3全库安装
#1创建角色
#创建一个屏幕
"""
display:显示
"""
screen=pygame.display.set_mode((800,600),flags=pygame.FULLSCREEN)      #对象
#2创建循环
x=100
y=200
x_v=0.1
y_v=0.3

def fd():
    global x,y,x_v,y_v
    x += x_v
    y += y_v
    if x < 100 or x > 700:
        x_v = -x_v
    if y < 100 or y > 500:
        y_v = -y_v
while True:
    for event in pygame.event.get():    #遍历所有事件
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill('green')
    pygame.draw.circle(screen,'red',(x,y),100,10)
    pygame.draw.rect(screen,'yellow',(x,y,30,30),10)
    fd()
    pygame.display.update()