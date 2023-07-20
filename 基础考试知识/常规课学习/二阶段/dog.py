class Dog():                #第一步写下类名
    def __init__(self,name,age,tall):       #创建属性,参数不能直接在类内部传递
        self.name = name
        self.age = age
        self.tall = tall

    def pp(self):               #创建第一个方法：显示方法
        print(self.name)
        print(self.age)
        print(self.tall)
        #print(name,age,tall)           #不能传递

    def zwjs(self):             #创建第二个方法：自我介绍
        print('大家好，我的名字叫%s，我今年%s岁了，身高%s公分'%(self.name,self.age,self.tall))

    def dg(self):               #创建第三个方法：打滚
        print('大家好，我的名字叫%s，我来给你们打个滚'%self.name)

import sys
import pygame
screen=pygame.display.set_mode((800,600))       #设置屏幕大小
pygame.display.set_caption('世纪之战')          #设置标题
screen.fill('yellow')
while True:
    for event in pygame.event.get():            #获取事件
        if event.type == pygame.QUIT:           #如果点X退出
            sys.exit()
    pygame.draw.line(screen,'black',(0,0),(800,600),10)     #画直线，画在哪，颜色，始末坐标，粗细
    pygame.display.update()                     #更新显示