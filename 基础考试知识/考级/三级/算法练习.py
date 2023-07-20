#生成一个随机数列25个元素
def maopao(l):
    ls=l.copy()
    sz=len(ls)
    for i in range(sz-1):
        for j in range(sz-1-i):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
    return ls

def xz(l):
    ls=l.copy()
    sz=len(l)
    for i in range(sz-1):
        k=i
        for j in range(i,sz):
            if ls[k]>ls[j]:
                k=j
        if k !=i:
            ls[i],ls[k]=ls[k],ls[i]
    return ls

def insertpx(l):
    ls = l.copy()
    sz = len(l)
    for i in range(1,sz):
        for j in range(i):
            if ls[i]<ls[j]:
                v=ls.pop(i)
                ls.insert(j,v)
                break
    return ls

def qkpx(l):
    ls = l.copy()
    sz = len(l)
    i,j=0,sz-1
    def px(ls,start,end):
        if start > end:
            return
        i,j=start,end
        k=i
        while True:
            while i<j and ls[j]>=ls[k]:
                j-=1
            while i<j and ls[i]<=ls[k]:
                i+=1
            if i<j:
                ls[i],ls[j]=ls[j],l[i]
            else:
                ls[j],ls[k]=ls[k],ls[j]
                break
        px(ls,start,k-1)
        px(ls,k+1,end)
    px(ls,i,j)

def duifenfind(l,k):
    sz = len(l)
    left=0
    right=sz-1
    b=-1
    while left <= right:
        mid=(left+right)//2
        if k==l[mid]:
            b=mid
            break
        elif k>l[mid]:      #找右边
            left = mid+1
        else:
            right=mid-1
    if b==-1:
        print("没找到")
    else:
        print("位置",b)
import random as r
ls=[r.randint(0,100) for i in range(25)]
print(ls)       #打印操作前的原数列
re1=maopao(ls)      #冒泡排序，希望不要改变原列表。所以写一个返回值
re2=xz(ls)          #选择排序，希望不要改变原列表。所以写一个返回值
re3=insertpx(ls)    #插入排序，希望不要改变原列表。所以写一个返回值
re4=qkpx(ls)        #快速排序，希望不要改变原列表。所以写一个返回值
print(re1)
print(re2)
print(re3)
print(ls)
duifenfind([1,2,3,4,5,6,7,8,9,10],6)


