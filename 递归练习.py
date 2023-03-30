'''
递归 实例1，将n/2  到商为0
def dg(n):
    if n==0:
        return
    print(n)
    dg(n//2)

def dg(n):
    v=n//2
    print(v)
    if v==0:
        return
    dg(v)
dg(89)

实例2  求阶乘

def jc(n):
    if n==1:
        return 1
    return n*jc(n-1)

v=jc(5)
print(v)

实例3，求和
def su(n):
    if n==1:
        return 1
    return n+su(n-1)

v=su(5)
print(v)

实例4：递归推斐波那契数列  求n项的值
def fabo(n):
    if n==1 or n==2:
        return 1
    return fabo(n-1)+fabo(n-2)
v=fabo(5)
print(v)

实例5：二分法找有序列表指定值
import random as r
l=[i for i in range(25)]
l.sort()
def difind(n,ls,min,max):
    mid=(min+max)//2
    if n == ls[mid]:
        print('{}在{}项'.format(n,mid))
        return mid
    elif n < ls[mid]:      #找左边
        difind(n,ls,min,mid)
    else:
        difind(n,ls,mid+1,max)
print(l)
v = difind(6,l,0,len(l))
print(v)

实例6：汉诺塔
def hanota(n,A,B,C):
    if n==1:
        print(A,'>>>',C,n)
    else:
        hanota(n-1,A,C,B)
        print(A,'>>>',C,n)
        hanota(n-1,B,A,C)
hanota(3,'A','B','C')

'''


