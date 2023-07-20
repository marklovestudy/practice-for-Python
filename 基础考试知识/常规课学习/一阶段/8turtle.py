'''
import turtle as t
#from turtle import *
Scratch作品

# t.circle(50,360)
# t.circle(-50,360)        #第一、二个参数可以控制-顺时针还是+逆时针
# t.circle(100,360,360)         #第一个参数：半径，第二个：角度，第三个：步数
# t.dot(100,'red')
import turtle as t
t.penup()
t.goto(-100,0)
t.pendown()
t.right(90)
t.pensize(10)
t.color('green','red')
t.begin_fill()
t.circle(100,180)
t.end_fill()
t.penup()
#西瓜仔
import random as r
n=0
while n <= 100:
    x = r.randint(-100,100)
    y = r.randint(-100,-10)
    OA=(x**2+y**2)**0.5
    if OA < 90:
        t.goto(x,y)
        t.dot(10,'black')
        n+=1
t.mainloop()                #主循环，他的作用是让屏幕停留。
'''

# import turtle as t
# t.setheading(270)           #把方向设定为多少方向
# t.pensize(5)                #把画笔粗细设定为
# t.color('green','red')      #画笔颜色，第一个参数是画笔的颜色，第二参数是填充颜色
# t.begin_fill()              #开始填充
# t.circle(100,180)           #图形
# t.end_fill()                #结束填充
# t.penup()                   #抬笔
# x = 30                      #设定一个变量x
# for i in range(6):          #for循环
#     t.goto(x,-30)           #移到x多少y多少
#     t.dot(10,'black')       #画一个点，第一个参数：直径为10，第二参数：黑色
#     x += 30                 #把变量x = x + 30
# t.mainloop()                #主循环，他的作用是让屏幕停留。

import turtle as t
t.penup()
t.goto(-200,0)
t.color('white','green')
t.begin_fill()
t.setheading(270)
t.circle(200,180)
t.end_fill()
#外面的半个西瓜
t.goto(-200,0)
t.color('white','red')
t.begin_fill()
t.setheading(300)
t.circle(230,120)
t.end_fill()
#西瓜仔
import random as r
n=0
while n <= 500:
    x = r.randint(-200,200)
    y = r.randint(-115,-10)
    OA=(x**2+(y-115)**2)**0.5
    if OA < 220:
        t.goto(x,y)
        t.dot(5,'black')
        n+=1
t.mainloop()