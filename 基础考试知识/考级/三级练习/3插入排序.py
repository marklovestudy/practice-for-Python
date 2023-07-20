import random as r
a=[]
for i in range(100):
    a.append(r.randint(0,100))
print(a)

def crpx(l):
    for i in range(1,len(l)):
        for j in range(0,i):
            if l[i] <= l[j]:
                v = l.pop(i)
                l.insert(j,v)
                break                   #跳出本次循环

crpx(a)
print(a)