import sys

import pygame
screen = pygame.display.set_mode((800,600))         #制定屏幕
sur1=pygame.image.load('img1.png').convert_alpha()   #载入图片

i=0
j=0
def ck(w,s,a,d):
    global i,j
    if event.key == pygame.K_a:  # 左走
        j = a  # 表示第二排
        i += 1  # 0-3
        i %= 4
    if event.key == pygame.K_d:  # 左走
        j = d  # 表示第二排
        i += 1  # 0-3
        i %= 4
    if event.key == pygame.K_w:  # 左走
        j = w  # 表示第二排
        i += 1  # 0-3
        i %= 4
    if event.key == pygame.K_s:  # 左走
        j = s  # 表示第二排
        i += 1  # 0-3
        i %= 4
while True:
    for event in pygame.event.get():                           #获取事件
        if event.type == pygame.QUIT:
            sys.exit()                                 #退出系统
        elif event.type == pygame.KEYDOWN:          #是否按下键盘
            ck(3,0,1,2)
    sur2 = sur1.subsurface((i*22, j*33, 22, 33))
    screen.fill('green')                            #填充背景颜色
    screen.blit(sur1,(300,300))                      #把角色sur1绘制到背景上
    screen.blit(sur2,(100,100))
    pygame.display.update()
