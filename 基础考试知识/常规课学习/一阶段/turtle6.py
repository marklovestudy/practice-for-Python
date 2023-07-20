'''
#第一种方式：
t.register_shape('cxk.gif')
#t.shape('cxk.gif')
'''
import turtle as t                  #载入turtle库
import random as r                  #载入随机库
t.tracer(False)                     #关闭轨迹、动画
t.bgpic('Wetland.png')              #载入背景图片
#第二种方式
q = t.Shape("compound")             #创建一个混合图形对象：q   compound:混合
q.addcomponent(((-2,3),(2,3),(2,-3),(-2,-3)),'gray','gray')    #绘制混合图形对象：q
t.register_shape('rain',q)              #给对象q取名：注册图形q,并取名为：’rain‘
print(t.getshapes())                    #打印当前可以获得的所有图形
t.shape('rain')                         #把光标的图像设定为’rain‘
t.setheading(45)                        #把方向设定为90
t.hideturtle()                          #隐藏本体
t.penup()                               #抬笔
#制作1000个雨滴.
rains=[]
for i in range(1000):                   #循环1000次
    ra=t.clone()                        #克隆光标t，克隆雨滴
    ra.setx(r.randint(-475,475))        #设置x坐标随机(-475,475)之间
    ra.sety(r.randint(-350,350))        #设置y坐标随机(-475,475)之间
    ra.showturtle()                     #显示
    rains.append(ra)                    #把雨滴添加到列表rains中。
while True:                             #无限循环
    for ra in rains:                    #遍历雨滴列表
        if ra.ycor() < -350:            #如果雨滴的y坐标小于-350
            ra.sety(350)                #把雨洋的y坐标设定为350
        else:
            ra.sety(ra.ycor()-5)        #把y坐标增加-5
        if ra.xcor() < -475:            #如果雨滴的y坐标小于-350
            ra.setx(475)                #把雨洋的y坐标设定为350
        else:
            ra.setx(ra.xcor()-5)        #把y坐标增加-5
    t.update()