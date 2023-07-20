import random as r
def maopaosort(l):
    sz=len(l)
    for i in range(sz-1):       #轮数
        for j in range(sz-1-i):     #范围
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
def selectsort(l):
    sz=len(l)
    for i in range(sz-1):   #轮数，i当前选择的位置
        for j in range(i+1,sz):     #在这个范围最小值。
            if l[i]>l[j]:       #说明当前位置i的值不是最小值
                l[i],l[j]=l[j],l[i]
def insertsort(l):
    sz=len(l)
    for i in range(1,sz):       #轮数，当前需要排的数
        for j in range(i):      #排好的范围0-i之间，把当前需要排的数i,插入到已经排好的序列中
            if l[i]<l[j]:
                l.insert(j,l.pop(i))

def sumdg(n):
    if n==1:
        return 1
    else:
        return sumdg(n-1)+n

# if __name__ == '__main__':
#     # ls=[r.randint(0,100) for i in range(25)]
#     # print(ls)
#     # #maopaosort(ls)
#     # #selectsort(ls)
#     # insertsort(ls)
#     # print(ls)
#     # sum=sumdg(100)
#     # print("1-100的和为：",sum)
# def ppdg1(n):
#     print(n,end=' ')
#     if n==1:
#         pass
#     else:
#         ppdg1(n-1)
# def ppdg2(n):
#     if n==1:
#         pass
#     else:
#         ppdg2(n-1)
#     print(n,end=' ')
#
# if __name__ == '__main__':
#     # ppdg1(100)
#     ppdg2(100)

'''
#有50道门，这50道编号为1-50.这50道门开始是关闭的
#什么相反操作：如果门是关闭的就打开，如果是打开的就闭
#1号操作员，会把所有1的倍数的门作相反的操作。
#2号操作员，会把所有2的倍数的门作相反的操作。
#3号操作员，会把所有3的倍数的门作相反的操作。
#4号操作员，会把所有4的倍数的门作相反的操作。
#。。。。。。。。
#50号操作员，会把所有50的倍数的门作相反的操作。
#问哪些门是打开的。
'''
# def taked(n):       #n代表的是操作员的编号
#     for j in range(50):   #j代表的是门
#         if j%(n+1)==0:          #门如果是操作员的倍数
#             doors[j]=-doors[j]      #相反操作
# if __name__ == '__main__':
#     doors=[-1 for i in range(50)]   #创建所有的门,-1代表关闭
#     for i in range(50):           #i代表1-50号操作员
#         taked(i)
#     for i in range(50):
#         if doors[i]==1:
#             print('{}号门是开着的'.format(i))
def czm(j,i):   #j代表门，i代表操作员的编号     操作门函数
    if j%i == 0:        #如果门是操作员的位数
        ls[j]=-ls[j]    #对门进行操作
    if j==50:           #当门是50时跳出条件
        pass
    else:
        czm(j+1,i)
def czy(n):             #操作员函数
    czm(1,n)            #把1号门和n号操作员传进去
    if n>50:
        pass
    else:
        czy(n+1)
if __name__ == '__main__':
    ls=[-1 for i in range(51)]
    czy(1)          #把1号操作员传进去
    for i in range(1,51):
        if ls[i]==1:
            print(i,end='  ')
