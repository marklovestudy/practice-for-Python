import random as r
# a=[]
# for i in range(100):
#     a.append(r.randint(0,100))
# print(a)
#
def xianzhepx(l,a):
    global j
    for i in range(len(l)):               #循环的次数
        k = i
        m = l[k]
        for j in range(i,len(l)):           #一次循环要对比的项数
            if l[j] >= m:
                k = j
                m = l[k]
        l.insert(i,l.pop(k))                #字黄的值
        a.insert(i,a.pop(k))                #字典的键
#
# xianzhepx(a)
# print(a)


#升级实例，班级成功排名
calss1 = {}
for i in range(1,51):
    calss1['name'+str(i)] = r.randint(0,100)

print(calss1)
lk=[]
lv=[]
for k,v in calss1.items():
    lk.append(k)
    lv.append(v)

xianzhepx(lv,lk)

calss2={}
for i in range(len(lv)):
    calss2[lk[i]]=lv[i]

print(calss2)
