import turtle as t
import random as r
t.tracer(0)             #关闭动画效果
#画一个五角星
def xx(c,a,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c)
    t.begin_fill()
    for i in range(5):
        t.forward(a)
        t.right(144)
    t.end_fill()
#画100个星星
stars=[]
for i in range(100):
    c=r.random(),r.random(),r.random()      #随机颜色
    a=r.randint(5,30)
    x=r.randint(-400,400)
    y=r.randint(-400,400)
    xx(c,a,x,y)
#记录星星的位置，大小
    stars.append([x,y,a])
print(stars)
#用循环来控制100个星星移动：改变X坐标，
#用循环来控制100个星星颜色：改变c
#用循环来控制100个星星，不改变大小，所以要读取原来的大小。
