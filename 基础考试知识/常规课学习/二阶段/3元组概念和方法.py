"""
一、元组的概念：
类型名称：tuple
定界符:()
可变行：不可变
有序性：有序
对元素类型与值的要求：无
元素是否重复：可以
元素查找速度：较慢
增删元素速度：不可以

元组的概念：
元组是轻量级的列表，在形式上元组的所有元素放在一对圆括号中，元素之间使用逗号分隔，如果元组中只有一个元素，则
必须在最后增加一个逗号。

二、创建方式
    第一种直接创建
    t1=(1,2,3,4)
    第二种函数创建
    t1=tuple(range(10))         #tuple(序列)
    推导式创建：生成器：
    t = ((i+2)**2 for i in range(3))    #创建生成器对象，区别于列表：列表快速创建是列表，不是生成器
生成器推导式的概念：
    生成器推导式的用法与列表推导式相似。使用圆括号作为定界符。与列表推导式最大的不同是生成器推导式的结果
    是一个生成器对象。生成器对象类似于迭代器对象。具有惰性求值的特点，比列表推导式更高效，空间占用少。
    使用生成器对象的元素时，可以将其转换为列表或元组，也可以使用生成器对象的__next__()方法或 next()函数
    进行遍历。或者直接使用 for 循环来遍历其中的元素。只能从左往后正方向访问其中的元素。没有任何方法可以
    再次访问已访问过的元素，也不支持使用下标访问其中的元素。

三、访问元组：
    索引访问：
    t1 = (i for i in range(2,20,2))
    print(t1[0])
    print(t1[2:4])
    print(t1[1:8:3])             #1代表起始索引位置，8代表结束位置，3代表步长

四、通用操作：
1判断元素是否在序列之内：in,not in.
                2连接序列：list1+list2
                3重复序列元素：list1*n
                4索引访问：s[i]，s[i:j],s[i:j:k]
                5获取序列属性：长度len(s),最小值min(s),最大值max(s),和sum(s)
                6检索某个元素第一次出现的元素下标s.index('x')
                7检索某个元素出现的次数s.count('x')

五、元组的方法：
1.index(3)    找到第一个指定元素的位置，如果没有找到就报错
2.count(3)    计算指定元素在元组中出现的次数
t1 = (1,2,3,4,5,6,3)
v = t1.count(3)
print(v)

实例：
classmate = ('银牌','铜牌','金牌','银牌','银牌','铜牌','银牌','铜牌','银牌','铜牌')
#请找出金牌是第几项运动中获得的。
#请计算银牌和铜牌的数量
v1 = classmate.index('金牌')
print('金牌是在第%s项运动中获的'%(v1+1))
v2 = classmate.count('银牌')
v3 = classmate.count('铜牌')
print('共获得银牌%s块，铜牌%s块'%(v2,v3))
#

prize = ('银牌','铜牌','金牌','银牌','银牌','铜牌','银牌','铜牌','银牌','铜牌')
#请找出金牌是第几项运动中获得的。
#请计算银牌和铜牌的数量
'''
请把['mark','a','b','c']转化成一个字符串，
再把这个字符串以'a'为分割符转成列表。
再把这个列表转换成元组。
再把这个元组转换成生成器，iter()
再一一调用这个生成器的数据。
v=['mark','a','b','c']
v1=''.join(v)
v2=v1.split('a')
v3=tuple(v2)
v4=iter(v3)
print(v4.__next__())
print(v4.__next__())
print(v4.__next__())
#
# 生成器推导式
# >>> t = ((i+2)**2 for i in range(3))    #创建生成器对象，区别于列表：列表快速创建是列表，不是生成器
# >>> t
# <generator object <genexpr> at 0x0000000002ED1890>
# >>> tuple(t)
# (4, 9, 16)
# >>> list(t)     #遍历结束，无元素，只能遍历一次
# []
#
# t = ((i+2)**2 for i in range(3))
# >>> t.__next__()        #可以__next__(),next(t)访问
# 4
# >>>
可以用for循环遍历
for i in t:
    print(i)
"""
# t = (i for i in range(10))
# print(list(t),'第一次打印')
# print(list(t),'第二次打印')
# import random as r                          #载入random
# import time as t                            #载入time
# monster = ['骷髅兵','僵尸','异形']            #怪物类型
# monster1 = []                               #第一关的怪物列表(上节课的内容温习)
# for i in range(100):                        #for循环100次
#     monster1.append(r.choice(monster))      #把随机的怪物类型添加到第一关的怪物列表
# product_monster = (i for i in monster1)     #用元组做一个生成器(元组的高级用法)
# for i in range(99):                        #循环100次
#     v = product_monster.__next__()          #生成器可以用next()和__next__()方法逐一提取生成器中的对象
#     print('现在刷新出来了一只%s怪，血量100'%v)   #显示生成器提取的对象
#     t.sleep(1)                              #等待一秒
# print(list(product_monster),'这是怪物生成器还有这些怪物')    #最后查看生成器中剩余的对象。

'''
数据转换：
# #字符串转列表的二种方式
# v1='mark'
# list1=v1.split('a')
# list2=list(v1)
# print(list1)
# print(list2)
# #列表转字符串
# list1=['a','b','c']
# str1=''.join(list1)
# str2=str(list1)
# print(str1)
# print(str2,type(str2))
# v1='mark'
# t1=v1.partition('a')
# t2=tuple(v1)
# print(t1)
# print(t2)
# list1=['a','b','c']
# t1=tuple(list1)
# print(t1)
# t1=('a', 'b', 'c')
# str1=''.join(t1)
# list1=list(t1)
# print(str1)
# print(list1)
'''

import random as r          #导入随机库
import time                 #导入时间模块
import turtle as t
t.penup()
monster = ['骷髅兵','僵尸','异形','Boss','精英骷髅兵','精英僵尸','精英异形']    #创建怪物列表
#gw = (monster[i%7] for i in range(100))         #创建一个100个随机怪的生成器
#monster[i%7]指的是元组gw的元素，monster[i%7]是通过索引取值的元素，也可以随机：
gw1 = (r.choice(monster) for i in range(100))
for i in range(100):
    dqgw=gw1.__next__()
    if dqgw in ['骷髅兵','僵尸','异形']:
        print('当前怪物为%s,血量：100，防御：6'%(dqgw))
        t.goto(r.randint(-500,500),r.randint(-250, 250))
        t.shape('circle')
        t.color('green')
        t.clone()
        t.write('    %s,HP：100，F：6'%(dqgw))
    elif dqgw in ['精英骷髅兵','精英僵尸','精英异形']:
        print('当前怪物为%s,血量：200，防御：12'%(dqgw))
        t.goto(r.randint(-500,500),r.randint(-250, 250))
        t.shape('square')
        t.color('black')
        t.clone()
        t.write('    %s,HP：100，F：6' % (dqgw))
    else:
        print('当前怪物为%s,血量：500，防御：30' % (dqgw))
        t.goto(r.randint(-500, 500),r.randint(-250, 250))
        t.shape('turtle')
        t.color('red')
        t.clone()
        t.write('    %s,HP：100，F：6' % (dqgw))
    time.sleep(1)
t.mainloop()