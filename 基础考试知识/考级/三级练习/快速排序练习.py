import random as r
l=[r.randint(0,100) for i in range(25)]
print(l)
n=0
def kspx(l,start,end):
    global n
    n+=1
    if start > end:
        return
    k=l[start]
    i,j=start,end
    while True:
        while i < j and l[j] >= k:   #1,从右到左找到一个小于k的值
            j -= 1
        while i < j and l[i] <= k:   #2,从左到右找到一个大于k的值
            i += 1
        if i < j:
            l[i],l[j]=l[j],l[i]
        else:
            l[start],l[j]=l[j],l[start]
            break
    kspx(l,start,j-1)
    kspx(l,j+1,end)
kspx(l,0,len(l)-1)
print(l)
print(n)