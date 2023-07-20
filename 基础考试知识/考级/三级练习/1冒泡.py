import random as r
a=[]
for i in range(100):
    a.append(r.randint(0,100))
print(a)

def maopao(l):
    for i in range(1,len(l)):               #循环的次数
        for j in range(len(l)-i):           #一次循环要对比的项数
            if l[j] >= l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

maopao(a)
print(a)