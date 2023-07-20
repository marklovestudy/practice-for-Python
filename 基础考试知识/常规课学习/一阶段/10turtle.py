'''
#彩色棒棒糖
import turtle as t
t.pensize(10)
t.color('gray')
t.goto(0,200)
colors=['red','green','gray','blue','yellow']
r = 150
for i in range(5):
    t.color(colors[i])
    t.dot(r)
    r-=30
t.mainloop()

10、speed()              #速度
import turtle as t      #载入turtle当作t
t.speed(0)              #速度设定为0，0代表最快无动画效果，1-10代表绘画速度由慢变快。
t.circle(70)            #画半径为70的圆

6、tracer()、t.update()                   #追踪，参数为False，无轨迹效果，True为有轨迹效果
当tracer()参数为False时，表示关闭轨迹，但我们需要刷新屏幕才能看到画面效果。True时会返回其值，
如True = 50，相当于50时间内返回一次画面。数字越小相当于返回的频率越高。
t.tracer(3,25)相当于3时间内返回一次画面，然后每次延时25毫秒。
import turtle as t                      #载入turtle当作t
t.speed(1)                              #速度设定为1
t.tracer(0)                             #参数设定为0表示为False
for i in range(4):                      #循环4次
    t.right(90)                         #右转90度
    t.forward(50)                       #前进50步

1.setheading(),把方向设定为多少方向。home()回到（0，0）,方向清0
import turtle as t
t.speed(1)
t.setheading(-45)
t.forward(200)
t.right(245)
t.home()
t.mainloop()

实例：绘制七角星
(180-180/n)
当n=5代表的是5角星，转180-180/5=144
'''
import turtle as t
t.tracer(False)
t.pensize(10)
t.color('gray')
t.goto(0,200)
colors=['red','green','gray','blue','yellow']
r = 150
for i in range(5):
    t.color(colors[i])
    t.dot(r)
    r-=30
t.mainloop()

import turtle as t
t.tracer(False)
v = 1
a=t.Pen()
while True:
    t.clear()
    a.clear()
    a.penup()
    a.pensize(20)
    if t.xcor()<0:
        a.goto(-200,-20)
        a.dot(50,'blue')
        a.pendown()
        a.goto(-140,-100)
    else:
        a.goto(-140, 0)
        a.dot(50,'blue')
        a.pendown()
        a.goto(-140, -100)
    if t.xcor() > 300:
        t.setx(-200)
    t.setx(t.xcor()+v)
    t.sety(-1/400*(t.xcor()+v)**2+100)
    t.dot(30,'green')   #dot(直径，颜色)
    t.update()
