def xrsort(l):
    n=len(l)
    gap=int(n/2)
    while gap>0:
        for i in range(gap,n):
            temp=l[i]
            j=i
            while j >= gap and l[j-gap]>temp:
                l[j]=l[j-gap]
                j-=gap
                l[j]=temp
        gap=int(gap/2)

import random as r
l=[r.randint(0,100) for i in range(25)]
print(l)
xrsort(l)
print(l)