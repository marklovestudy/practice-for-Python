import random as r
def maopaosort(l):
    sz=len(l)
    for i in range(sz-1):
        for j in range(sz-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

def selectsort(l):
    sz=len(l)
    for i in range(sz-1):
        for j in range(i+1,sz):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]

def dg(n):
    print(n)        #他的作用打印这个数n
    if n==1:
        return
    else:
        dg(n-1)
        print(n, '结束了')


def dg_sum(n):
    if n==1:
        return 1
    else:
        return dg_sum(n-1)+n

# if __name__ == '__main__':
#     # ls=[r.randint(0,100) for i in range(25)]
#     # print(ls)
#     #maopaosort(ls)
#     # selectsort(ls)
#     # print(ls)
#     #递归：1跳出     2调用：直接调用自己：（1，2，3，4，5，6，7，8调用），间接的调用自己，
#     #dg(10)       #这是一个简单的递归实例
#     num=eval(input("输入一个数，我可以帮你求出从1加到这个数的和"))
#     re=dg_sum(num)
#     print('从1加到%d的和是：%d'%(num,re))


# if __name__ == '__main__':
#     num=eval(input("输入一个数，我可以帮你求出从1乘到这个数的积"))
#     re = dg_sum(num)
#     while re<18446744073709551615:
#         num+=1
#         re=dg_sum(num)
#         print(num)
#     print(num)
    # print('从1乘到%d的积是：%d'%(num,re))

# def dg_cj(n):
#     if n == 1:
#         return 1
#     else:
#         return dg_cj(n - 1) * n
#
# if __name__ == '__main__':
#     num = eval(input("输入一个数，我可以帮你求出从1乘到这个数的积"))
#     re=dg_cj(num)
#     print('从1乘到%d的积是：%d'%(num,re))

#创建一个列表，长度51，每个元素的值为-1的列表
#请将所有元素索引号为1的倍数的值改为相反数。
#请将所有元素索引号为2的倍数的值改为相反数。
#请将所有元素索引号为3的倍数的值改为相反数。

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