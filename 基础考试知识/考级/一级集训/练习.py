# 循环结构：重复
#
# 循环结构 条件：
#     循环体
#for i in 序列:   1字符串，range(),列表，元组，集合，字典
# for i in range(10):     #1种有限循环for
#     print(123)
#     print('ok')
# for i in 'mark':    #遍历序列
#     print(i)
# for i in range(1,10,2):
#     print(i)
# for i in [10,2,33,44,56]:#遍历序列
#     print(i)
# while True:              #2无限循环,为真执行，为假不执行
#     print(111)
#3循环直到，当为真时重复执行直到为假

#为假：0,'' [] () None,False
# n=10
# while n:
#     print(123)
#     n -= 1
# a=10
# b=20
# if a>b:         #分支嵌套
#     print('haha')
#     if a:
#         pass
#     else:
#         pass
# elif a==b:     #elif == else + if
#     print('ss')
# else:
#     print('hehe')

#用询问的方式，写一个无限循环如age=eval(input("你多大了"))。
#公园买票进入
#6岁以下免费包含6岁         输出:您可以免费进入公园
#18岁以下半价5元              输出:您需要付5元进入公园
#60岁以下全价10元             输出:您需要付10元进入公园
#60岁以上，如果是农民免费，其它人3元。   输出:您是农民可以免费进入公园  否则输出:您需要付3元进入公园