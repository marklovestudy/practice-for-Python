'''
递归算法
    在定义一个函数或过程时出现调用自身的成分，称之为递归。

递归算法
    递归程序设计是程序设计中的一种重要的方法，它使许多复杂的问题变得简单，容易解决了。
    就递归算法而言并不涉及高深的数学知识，但要建立递归概念，深入了解递归过程也不容易。

计算:fx=1+2+3+4+5。。。的值：
def fx(a):
    if a <= 1:
        return 1
    else:
        return a + fx(a-1)
print(fx(5))

例：求，一个数的一半取整
def caic(n):
    print(n)
    if int(n/2) == 0:
        return n
    n = int(n/2)
    re = caic(n)
    return re

print(caic(42))

递归实例1
teachers = ["mark","weiwei","dafei","xigua","dabai"]
def wenti(teachers):
    if len(teachers) == 0:
        return "真是可惜，没有人知道怎么做这道题.."
    teacher = teachers.pop(0)
    if teacher == "xigua":
        return "这道题so easy!!%s会做"%teacher
    print("%s你好：这道题我想了一会太难了，实在不会，请问怎么做"%teacher)
    print("%s回答道：我想了一会，我也不会，你等着，我帮你问问%s"%(teacher,teachers))
    result = wenti(teachers)
    print("%s说："%teacher,result)
    return result
s = wenti(teachers)
print(s)

实例2
数学中的阶乘定义：
    1的阶乘：1
    2的阶乘：1*2
    3的阶乘：1*2*3
    n的阶乘：1*2*3*4*......*(n-1)*n
def jc(n):
    if n <= 1:
        return 1
    else:
        return n*jc(n-1)
print(jc(5))

**递归算法的基本思想是把规模较大的问题变成规模较小的，规模较小的问题又变成规模较小的问题，当问题小到
一定程度的时，可以直接得出它的解，从而得到原来问题的解。即采用'大事化小，小事化了'的基本思想。

递归算法的实现要点
    1有明确的结束递归的边界条件(又称终止条件)以及结束的边界值，可以通过条件语句(if语句)来实现
    2函数的描述中包含其本身，即能用递归形式表示，且递归终止条件的发展。
    def jc(n):
    if n <= 1:              #边界条件
        return 1
    else:
        return n*jc(n-1)    #包含其本身

常规函数求阶乘：
def jc(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
    本例而言，同学们认为递归算法可能是多余的，费力不讨好。但许多实际问题不可能或不容易找到显而易见的
    递推关系，这时递归算法就表现出了明显的优越性。

汉诺塔问题：
def aa(n,A,B,C):
    m = 0
    def hanota(n,A,B,C):
        nonlocal m
        if n == 1:
            print(A,'-->',C,' ',n)
            m +=1
        else:
            hanota(n-1,A,C,B)               #先把n-1作为整体从A搬到B
            print(A, '-->', C, ' ', n)      #再把n从A搬到C
            m += 1                          #次数加1
            hanota(n - 1, B, A, C)          #再把n-1作为整体从B搬到C
    hanota(n,A,B,C)
    print('共%s次'%m)
aa(2,'A','B','C')

例第n个人比第n-1个人大一岁的问题。
def duoda(n):
    if n == 1:
        return 8
    else:
        return duoda(n-1) + 1
v = duoda(5)
print(v)
'''

import turtle as t
def shu(d):
    if d < 6:
        return
    else:
        t.forward(d)
        t.right(20)
        shu(d-5)
        t.left(40)
        shu(d - 5)
        t.right(20)
        t.backward(d)

t.seth(90)
shu(50)
t.mainloop()