import random as r
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

def insertsort(l):
    sz=len(l)
    for i in range(1,sz):
        for j in range(i):
            if l[j]>l[i]:
                l.insert(j,l.pop(i))
def dgh(n):
    if n==1:
        return 1
    return dgh(n-1)+n

def dgj(n):
    if n==1:
        return 1
    return dgj(n-1)*n

def manip(n):
    for i in range(1,51):
        if i%n==0:
            doors[i]=-doors[i]

def kgdoor(n):
    for i in range(1,51):
        if i%n==0:
            doors[i]=-doors[i]
    if n==50:
        return
    else:
        kgdoor(n+1)

if __name__ == '__main__':
    # ls=[r.randint(0,100) for i in range(25)]
    # print(ls)
    # #maopao(ls)
    # #selectsort(ls)
    # #insertsort(ls)
    # print(ls)
    # re=dgh(eval(input("n?")))
    # print(re)
    # re1 = dgj(eval(input("n?")))
    # print(re1)
    doors=[-1 for i in range(51)]
    # for i in range(1,51):       #从1号到50号操作员
    #     manip(i)                #让i号操作员对门进行相反操作。
    # for i in range(51):         #查看数据
    #     if doors[i] ==1:
    #         print('%s是开着的'%i)
    kgdoor(1)
    for i in range(51):         #查看数据
        if doors[i] ==1:
            print('%s是开着的'%i)

