# number = eval(input("请输入一个整数："))    #1234567689  输出把13579存储在m中
# m=0
# idex=1
# while number:
#     if number%2==1:
#         m=idex*(number%10)+m
#         idex*=10
#     number=number//10
# print(m)

# ls=[]
# while number:
#     if number%2==1:
#         ls.append(number%10)
#     number//=10
# print(ls)
# m=0
# for i in ls[::-1]:
#     m=m*10+i
# print(m)

# list1=[['mark',55,45,67],
#        ['weiwei',65,85,67],
#        ['dafei',45,85,97],
#        ['xiaoz',54,76,37]]

'''
# >>> list1=[['mark',55,45,67],
#        ['weiwei',65,85,67],
#        ['dafei',45,85,97],
#        ['xiaoz',54,76,37]]
# >>> list1
# [['mark', 55, 45, 67], ['weiwei', 65, 85, 67], ['dafei', 45, 85, 97], ['xiaoz', 54, 76, 37]]
# >>> for i in list1:
# 	print(i)
#
#
# ['mark', 55, 45, 67]
# ['weiwei', 65, 85, 67]
# ['dafei', 45, 85, 97]
# ['xiaoz', 54, 76, 37]
# >>> for i in list1:
# 	print(i[1:])
#
#
# [55, 45, 67]
# [65, 85, 67]
# [45, 85, 97]
# [54, 76, 37]
#
# >>> for i in list1:
# 	print(sum(i[1:]))
#
#
# 167
# 217
# 227
# 167
# >>> list2=[sum(i[1:]) for i in list1]
# >>> list2
# [167, 217, 227, 167]
# >>> max(list2)
# 227
# >>> min(list2)
# 167
'''

# t1=(1,2,3,4)
# t2=tuple('mark')
# t3=(i for i in range(10))
# print(t1)
# print(t2)
# print(t3)

classmate = ('银牌','铜牌','金牌','银牌','银牌','铜牌','银牌','铜牌','银牌','铜牌')
#请找出金牌是第几项运动中获得的。           #index(元素)，查找元素索引
#请计算银牌和铜牌的数量                   #count(元素),计算元组中指定元素的个数。

#下节课重点讲解join和split

#按图画画
import turtle as t
colors=('red','blue','orange','green')
for i in range(50):
    t.color(colors[i%4])
    t.forward(15+5*i)
    t.left(90)
t.mainloop()