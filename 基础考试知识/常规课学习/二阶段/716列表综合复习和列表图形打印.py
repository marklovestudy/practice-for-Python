# 1   创建一个列表[1,2,3],在末尾添加4
#list1=[1,2,3]
#list1.append(4)
# 2   用list把'mark'创建成列表
#list2=list('mark')
# 3   用推导式创建列表，元素为0，1，2，3，4，5，6，7，8，9
#list3=[i for i in range(10)]
# 4   l1=[1,2,3],在l1索引为1的位置插入66这个数。
#l1.insert(1,66)
# 5   l2=[111,222,333,444,555]请用index找出333的索引号
#l2.index(333)
# 6   请创建l3=['同学1','同学2','同学3',,,,'同学100']
#l3=['同学%s'%i for i in range(1,101)]
# 7   请删除l4=[1,2,3,4,5,6]中的6。
#l4.remove(6)
# 8   请删除l5=[11,22,33,44,55]中的索引为3的元素。
#l5.pop(3)
# 9   请在列表l6=[1,2,3]的后面添加66
#l6.append(66)
# 10  请删除列表中l7=[1,2,3,4,5,6,7,8,9,10]中的偶数
# l7=[1,2,3,4,5,6,7,8,9,10]
# for i in l7:
#     if i%2==0:
#         l7.remove(i)
# print(l7)

# l1=[2,6,3,4,5]
# l1.reverse()
# print('翻转后：',l1)
# l1.sort()       #=l1.sort(reverse=False)
# print('排序后：',l1)
# l1.sort(reverse=True)
# print('从大到小：',l1)

#1请把[8,2,3,7,5]翻转
# l1=[8,2,3,7,5]
# l1.reverse()
#2请把['c','d','a','b']从小到大排序
# l2=['c','d','a','b']
# l2.sort()
#3请把[3,9,1,6]从大到小排列。
# l3=[3,9,1,6]
# l3.sort(reverse=True)

#l1=[1,2,3,4,5,6,7,8,9]
#请求出l1的元素的和
# sum1=0
# l1=[1,2,3,4,5,6,7,8,9]
# for i in l1:
#     # sum1=sum1+i
#     sum1+=i
# print(sum1)
# #请求出l1中所有元素的积
# sum1=1
# l1=[1,2,3,4,5,6,7,8,9]
# for i in l1:
#     # sum1=sum1+i
#     sum1*=i
# print(sum1)
#请求出l1中所有奇数的和
# sum1=0
# l1=[1,2,3,4,5,6,7,8,9]
# for i in l1:
#     if i%2==1:
#         sum1+=i
# print(sum1)

# for i in range(10):             #i表示行，j表示列
#     for j in range(10):
#         print('*',end='')
#     print()

# for i in range(10):             #i表示行，j表示列
#     for j in range(10-i):
#         print('*',end='')
#     print()

# for i in range(10):             #i表示行，j表示列
#     for j in range(i+i+1):
#         print('*',end='')
#     print()

#程序设计
n=eval(input('请输入一个整数：'))
for i in range(n):             #i表示行，j表示列
    for j in range(i+i+1):
        print('*',end='')
    print()
for i in range(n):             #i表示行，j表示列
    for j in range(n+n-1-i-i):
        print('*',end='')
    print()