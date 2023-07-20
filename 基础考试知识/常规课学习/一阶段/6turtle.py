# import turtle       #载入库，方式1
# import turtle as t      #载入方式2
#from turtle import *        #载入方式3，载入所有
# h = t.Turtle()   #先拿一个对象
# for i in range(4):
#     h.forward(100)      #前进
#     h.right(90)         #右转90度
#
# for i in range(1):
#     t.forward(-100)
#     t.right(-120)
# t.mainloop()       #主循环

'''
1、forward()、fd()        #前进
2、right()、rt()          #右转
'''

# import turtle as t
# t.forward(120)
# t.right(-120)
# t.forward(120)
# t.right(-120)
# t.forward(120)
# t.right(-120)
# t.forward(20)
# t.right(90)
# t.forward(100)
# t.right(-90)
# t.forward(40)
# t.right(-90)
# t.forward(100)
# t.right(90)
# t.forward(40)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(40)
#
# t.mainloop()
# import turtle as t
# #h = t.Pen()             #所有笔的总称，定义一支笔的对象
# #四边形
# for i in range(4):      #for循环
#     t.forward(100)      #前进100
#     t.right(90)         #右转
# #三角形
# t.forward(200)
# t.right(120)
# t.forward(200)
# t.right(120)
# t.forward(200)
# t.right(120)
# t.mainloop()            #主循环,内置循环

# import turtle as t
# a=30
# for n in range(4):
#     for i in range(6):
#         for j in range(3):
#             t.forward(a)
#             t.right(120)
#         t.right(60)
#     a +=30
# t.mainloop()
import turtle as t
screen = t.Screen()
screen.bgcolor('black')
a = t.Turtle('turtle')                   #把光标的形状换成小乌龟
b = t.Turtle('turtle')
a.color('white')
b.color('white')
a.speed(0)
b.speed(0)
# for n in range(30,181,30):          #步长
#     for i in range(6):
#         for j in range(3):
#             a.forward(n)
#             a.right(120)
#         a.right(60)

b.goto(100,0)
for q in range(114514):
    for n in range(30,181,30):          #步长
        for i in range(6):
            for j in range(3):
                a.forward(n)
                a.right(120)
                b.forward(n)
                b.right(120)
            a.right(60)
            b.right(60)
t.mainloop()