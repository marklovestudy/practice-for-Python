import random as r
l=[r.randint(0,100) for i in range(25)]

def maopao(l):
    sz=len(l)
    for i in range(sz-1):
        for j in range(sz-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

def selectsort(l):
    sz=len(l)
    for i in range(sz-1):
        for j in range(i+1,sz):
            if l[j]<l[i]:
                l[i],l[j]=l[j],l[i]

def fun(n):
    #1退出条件，2调用自己
    if n==1:
        return 1
    else:
        return fun(n-1)+n
#1+2+3+4+5    fun(5)=fun(4)+5=fun(3)+4+5=fun(2)+3+4+5=1+2+3+4+5
#1+2+3+4      fun(4)+5

if __name__ == '__main__':
    #print(l)
    #maopao(l)
    #selenctsort(l)
    #print(l)
    #求1+2+3+。。。100的和
    #求1*2*3    6的积
    n=eval(input("你想求1到多少的和，n=??"))
    re=fun(n)
    print("1+...+%d=%d"%(n,re))