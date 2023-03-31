'''
汉诺塔
def hanota(n,A,B,C):
    if n == 1:
        print(A,'>>>',C,n)
    else:
        hanota(n-1,A,C,B)
        print(A,'>>>',C,n)
        hanota(n-1,B,A,C)
hanota(2,'A','B','C')

青蛙跳街
def tiaojie(n):
    if n == 1:
        print('从{}跳到{}'.format(1,0))
        return 1
    elif n==2:
        print('方法1：')
        print('从{}跳到{}'.format(2, 0))
        print('方法2：')
        print('从{}跳到{}'.format(2, 1))
        print('从{}跳到{}'.format(1, 0))
        return 2
    else:
        print('方法1：')
        print('从{}跳到{}'.format(n, n-1))
        print('方法2：')
        print('从{}跳到{}'.format(n, n-2))
        return tiaojie(n-1)+tiaojie(n-2)

v=tiaojie(3)
print(v)

青蛙跳街说出每种跳法的祥情
def tiaojie(n):
    if n==0:
        return
    if n == 1:
        print('从{}跳到{}'.format(1,0))
    elif n==2:
        for j in range(1,3):
            print('从{}跳到{}'.format(2,n-j))
            tiaojie(n-j)
    else:
        for i in range(1, 3):
            print('从{}跳到{}'.format(n, n-i))
            tiaojie(n - i)
v=tiaojie(4)

print(v)

递归绘制谢尔宾斯基三角形
import turtle as t
import math
import turtle as t
import math
import random as r
def delta(n,d,x,y,c,c1):
    san(d,x,y,c1)
    c1=r.random(),r.random(),r.random()
    if n == 1:
        san(d,x,y,c)
    else:
        delta(n - 1, d/2, x, y,c,c1)
        delta(n-1,d/2,x+d/2,y,c,c1)
        delta(n-1,d/2,x+d*math.cos(math.pi/3)/2,y+d*math.sin(math.pi/3)/2,c,c1)


def san(d,x,y,c):
    t.goto(x,y)
    t.seth(0)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(3):
        t.forward(d)
        t.left(120)
    t.end_fill()
    t.penup()
t.tracer(0)
t.penup()
print(math.pi/3)
c=r.random(),r.random(),r.random()
c1=r.random(),r.random(),r.random()
delta(4,400,-200,-200,c,c1)
t.update()
t.mainloop()

雪花
import turtle as t
import math
import random as r
t.tracer(0)
def xuehua(n,d):
    if n==0:
        t.forward(d)
    else:
        for ang in [0,60,-120,60]:
            t.left(ang)
            xuehua(n-1,d/3)

def xuexue(n,d):
    for i in range(3):
        xuehua(n,d)
        t.right(120)
xuexue(5,300)
t.update()
t.mainloop()
'''
import turtle as t
import math
import random as r
t.tracer(0)
def xuehua(n,d):
    if n==0:
        t.forward(d)
    else:
        for ang in [0,60,-120,60]:
            t.left(ang)
            xuehua(n-1,d/3)

def xuexue(n,d):
    for i in range(3):
        xuehua(n,d)
        t.right(120)
xuexue(5,300)
t.update()
t.mainloop()