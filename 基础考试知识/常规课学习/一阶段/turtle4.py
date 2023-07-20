import turtle as t
import random as r
def pink():
    color=(1,r.random(),1)
    return color
def heart(r):
    t.color(pink())         #1确定一个随机颜色
    t.begin_fill()          #2开始填充
    t.circle(r,180)
    t.right(90)
    t.circle(r, 180)
    t.forward(2*r)
    t.left(90)
    t.forward(2*r)
    t.end_fill()        #4结束填充
t.setup(800,600,0,0)    #宽，高，左上X，左上Y
t.bgcolor('green')          #填充背景为绿色
for i in range(100):
    t.penup()
    #t.goto(r.randint(-300,300),r.randint(-300,300))
    t.setx(r.randint(-300,300))         #把X坐标设定为-300，300
    t.sety(r.randint(-300,300))         #把Y坐标设定为-300，300
    t.pendown()
    heart(r.randint(3,30))
t.mainloop()