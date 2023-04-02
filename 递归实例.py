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

地毯：
import turtle as t
import math
import random as r
t.tracer(0)
t.penup()
def sq(n,d,x,y):
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(d)
        t.left(90)
    t.penup()
    if n == 1:
        return
    else:
        sq(n-1,d/3,x+d/3,y+d/3)
def dt(n,d,x,y):
    sq(2,d,x,y)
    if n==1:
        return
    else:
        dt(n-1,d/3,x,y)
        dt(n - 1, d / 3, x+d/3, y)
        dt(n - 1, d / 3, x+2*d/3, y)
        dt(n - 1, d / 3, x, y+d/3)
        dt(n - 1, d / 3, x+2*d/3, y+d/3)
        dt(n - 1, d / 3, x, y+2*d/3)
        dt(n - 1, d / 3, x+d/3, y+2*d/3)
        dt(n - 1, d / 3, x+2*d/3, y+2*d/3)
dt(4,200,-100,-100)
t.update()
t.mainloop()

总结：1递归首先是找规律，找出最基本的图形。
    2然后找出最基本图形的规律。
    3然后找出最基本图形的规律。
    4一直找规律直到达到目的。

#拓展1方格：
import turtle as t
t.tracer(0)
def sq(n,d,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
        t.forward(d)
        t.left(90)
    if n == 1:
        return
    else:
        sq(n - 1, d / 2, x , y)
        sq(n - 1, d / 2, x, y + d / 2)
        sq(n-1,d/2,x+d/2,y)
        sq(n - 1, d / 2, x + d / 2, y+ d / 2)
sq(5,200,-100,-100)
t.update()
t.mainloop()

#拓展2花：
import turtle as t
import random as r
t.tracer(0)
def sq(d,x,y,c):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(0,405,45):
        t.seth(i)
        t.circle(d,90)
        t.left(90)
        t.circle(d,90)
    t.end_fill()
    if d <= 5:
        return
    else:
        c=r.random(),r.random(),r.random()
        sq(d-5,x,y,c)
c=r.random(),r.random(),r.random()
sq(200,0,0,c)
t.update()
t.mainloop()

#拓展  动花：
import turtle as t
import random as r
import time
t.hideturtle()
def sq(d,x,y,c,n):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(0,405,45):
        t.seth(i)
        t.circle(d,90)
        t.left(90)
        t.circle(d,90)
    t.end_fill()
    if d <= 5:
        return
    else:
        c=r.random(),r.random(),r.random()
        sq(d-n,x,y,c,n)

while 1:
    t.clear()
    t.tracer(0)
    c=r.random(),r.random(),r.random()
    n=r.randint(5,20)
    m=r.randint(100,150)
    sq(m,0,0,c,n)
    t.update()
    time.sleep(1)
'''

#拓展：
import turtle as t
import random as r
import time
t.hideturtle()
def sq(d,x,y,c,n):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(c)
    t.begin_fill()
    for i in range(0,405,45):
        t.seth(i)
        t.circle(d,90)
        t.left(90)
        t.circle(d,90)
    t.end_fill()
    if d <= 5:
        return
    else:
        c=r.random(),r.random(),r.random()
        sq(d-n,x,y,c,n)

while 1:
    t.clear()
    t.tracer(0)
    c=r.random(),r.random(),r.random()
    n=r.randint(5,20)
    m=r.randint(100,150)
    sq(m,0,0,c,n)
    t.update()
    time.sleep(1)

