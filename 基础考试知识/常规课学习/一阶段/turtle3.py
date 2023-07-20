'''
数学上的函数：Y=2X    #自变量，x的范围就叫定义域，y的范围就叫值域，
函数的概念：
    函数的意义：
    在写一段程序的时候，需要多次用到同样的功能，如果每次都要重复写相同的代码，不仅会增加代码量，
    而且阅读与修改极不方便。如果把实现相同功能的代码作为一个代码块封装在一起，形成一个函数，每
    次仅需要时调用这个函数，就很方便了！

def user():                 #函数名，以冒号结尾，括号内可有参数。
    print('hello world')    #函数体，用来完成的功能代码
user()                      #使用函数名()的方式调用

向函数传递参数信息
def user(name):                 #函数名，以冒号结尾，括号内可有参数。
    print('hello world',name)    #函数体，用来完成的功能代码
user('mark')
'''
import time
import turtle as t
import random as r
t.speed(0)
t.tracer(False)
t.bgcolor('black')     # t.bgpic('图片1.png')    # t.screensize(1200,800,'black')
stars_position=[]
def xx(color1,a,x,y):           #创建星星函数
    t.penup()
    t.goto(x,y)
    b = [t.xcor(),t.ycor(),a]
    stars_position.append(b)
    t.pendown()
    t.color(color1,color1)
    t.begin_fill()
    for i in range(5):
        t.forward(a)
        t.right(144)
    t.end_fill()
for i in range(50):
    color2=(r.random(),r.random(),r.random())           #创建变量
    xx(color2,r.randint(5,30),r.randint(-400,400),r.randint(-300,300))      #调用函数
print(stars_position)
t.hideturtle()
while True:
    for i in stars_position:
        if i[0] < -400:
            i[0] = 400
        else:
            i[0] -= 1
    t.clear()
    for i in range(50):
        color2 = (r.random(), r.random(), r.random())  # 创建变量
        xx(color2, stars_position[i][2], stars_position[i][0], stars_position[i][1])  # 调用函数
    t.update()      #刷新屏幕