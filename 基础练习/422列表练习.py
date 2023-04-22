'''
>>> ls2
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> len(ls2)
9
>>> 4%2
0
>>> ls2[-1]
9
>>> ls2[1:5]
[2, 3, 4, 5]
>>> ls2[1:-4]
[2, 3, 4, 5]
>>> [1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8]

>>> ls2=[1,2,3,4,5]
>>> ls2[2]=10
>>> ls2
[1, 2, 10, 4, 5]
>>> #修改，添加，删除，访问
>>> ls2.append(15)
>>> ls2
[1, 2, 10, 4, 5, 15]
>>> ls2.pop(2)
10
>>> ls2
[1, 2, 4, 5, 15]
>>> #索引删除和值删除
>>> ls2.remove(4)
>>> ls2
[1, 2, 5, 15]
>>>

'''

import random as r
list1=["同学%s"%i for i in range(1,r.randint(10,50))]         #列表推导式
print(list1)
#写一道程序，随机生成一个列表，里面全是人名
# 如果是奇数，请输出最中间的那个人的名字。
# 如果是偶数，请输出最后一个人的名字

#请删除偶数号同学和能被3整除的同学。
print(list1[1::2])
v2=list1[1::2]      #偶数同学
print(list1[2::3])
v3=list1[2::3]      #3的倍数同学
#删除2和3的倍数同学
for i in list1:
    if (i in v2):
        list1.remove(i)
for i in list1:
    if i in v3:
        list1.remove(i)
print(list1)

#len()  求序列长度
# v=len(list1)
# print(v)
#用for循环自己去数
# count=0
# for i in list1:
#     print(i)        #遍历
#     count+=1
# print(count)


# length=len(list1)    #索引号0，1，2，3。。。len(list1)-1
# if length%2 == 0:   #为偶数
#     print(list1[-1])
# else:               #为奇数  中间的数为长度除以2取整
#     print(list1[length//2])

#可以用while去找
# length=len(list1)
# start=0
# end=length-1
# b=-1
# while start <= end:
#     if start == end:
#         b=1
#         break
#     start+=1
#     end-=1
# if b==-1:
#     print(list1[-1])
# else:
#     print(list1[start])