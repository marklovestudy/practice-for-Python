# import turtle
# turtle.forward()        #调用函数
# import turtle as t
# t.forward()                 #调用函数
# from turtle import *
# forward()                   #不需要用‘库名.函数’，可以直接调用
# import turtle as t
# a = t.Pen()
# a.pendown()
# for i in range(4):
#     a.forward(50)
#     a.right(90)
# a.penup()
# a.forward(150)
# a.pendown()
# for i in range(4):
#     a.forward(50)
#     a.right(90)
#
# t.mainloop()                #内循环，他的作用是画屏保留


# a.color('green','red')          #确定画笔pencolor和填充颜色fillcolor
# a.begin_fill()                  #开始填充
# for i in range(4):              #被填充的图形
#     a.forward(50)
#     a.right(90)
# a.end_fill()                    #结束填充
# import turtle as t
# a = t.Pen()
# #长方形
# a.penup()
# a.goto(0,0)
# a.pendown()
# a.color('red','red')
# a.begin_fill()
# for i in range(2):
#     a.forward(200)
#     a.right(90)
#     a.forward(150)
#     a.right(90)
# a.end_fill()
#
# #五角星
# a.penup()
# a.goto(20,-40)
# a.pendown()
# a.color('yellow','yellow')
# a.begin_fill()
# for i in range(5):
#     a.forward(50)
#     a.right(144)
# a.end_fill()
# t.mainloop()

# t.pensize(5)
# t.penup()       #抬笔penup()、pu()、up()        #画笔抬起
# t.pendown()     #落笔pendown()、pd()、down()     #画笔落下
# #给图形填充颜色：1确定被填充的颜色，2开始填充，3被填充的图形，4结束填充
#颜色的确定二种方式：
#:1--t.color('green','red')   #t.color(t.pencolor(),t.fillcolor())
#2-- t.pencolor()    t.fillcolor()
#3--t.color((0.1,0.5,0.6))      #t.color((r.random(),r.random(),r.random()))
#4--第一步：修改颜色范围t.colormode(255)  第二步：确定颜色t.color((1,2,3),(255,255,255))
# import turtle as t
# import random as r
# t.colormode(255)
# t.pensize(20)
# t.color((r.randint(0,255),r.randint(0,255),r.randint(0,255)),(r.randint(0,255),r.randint(0,255),r.randint(0,255)))          #1确定颜色
# t.begin_fill()                  #2开始填充
# for i in range(4):              #3被填充的图形
#     t.forward(100)
#     t.right(90)
# t.end_fill()                    #4结束填充
# t.mainloop()

import turtle as t
a = t.Pen()
#长方形
a.penup()
a.goto(0,0)
a.pendown()
a.color('red')
a.begin_fill()
for i in range(2):
    a.forward(200)
    a.right(90)
    a.forward(150)
    a.right(90)
a.end_fill()
#五角星
a.penup()
a.goto(20,-40)
a.pendown()
a.color('yellow','yellow')
a.begin_fill()
for i in range(5):
    a.forward(50)
    a.right(144)
a.end_fill()
t.mainloop()