'''

'''
#
# ls1=[1,2,3]     #1直接创建一个列表
# ls2=list('mark')    #2函数创建
# ls3=[2*i+1 for i in range(10)]          #推导式创建：[元素 个数]
# print('直接创建',ls1)
# print('函数创建',ls2)
# print('推导式创建',ls3)
# ls1.insert(1,22)
# print('这个是插入后的ls1',ls1)
#你去排队，结果这里排队身高是students=[144,155,158,163,165,175]
#1来了一个人，身高为160，请问163的人排在第几的位置。
#2请把他排入到相应的位置。
ls1=[144,155,158,163,165,175]
idx=ls1.index(163)   #找到163的索引
ls1.insert(idx,160)       #把160插入到163之前。
print(ls1)

#请创建一个列表，ls2=['同学1','同学2','同学3',........,'同学50']
#ls2=[? for i in range(1,51)]
# import random as r
#r.randint(0,100)
# ls2=['同学'+str(i) for i in range(1,51)]
# ls2=['同学%s'%i for i in range(1,51)]
# print(ls2)
# 请创建一个，元素为随机数，范围0-50，元素个数为50的列表。
# ls3=[r.randint(0,50) for i in range(50)]

#元素为：一等奖，二等奖，三等奖，幸运奖中的一个，元素个数：50
#如：['一等奖'，‘幸运奖’，‘幸运奖’,'二等奖'，‘幸运奖’，'一等奖'....]
# import random as r
# pz=['一等奖','二等奖','三等奖','幸运奖']
# #pz[0]
# ls4=[pz[r.randint(0,3)] for i in range(50)]
# print(ls4)

#请设计一个程序：
#请输入一个名字，输入一个成绩，把这个人的名字和成绩插入到列表中
#如：原列表ls5=[['mark',99],['htl',120],['ghh',130],['xzj',140],['xzh',150]]
#输入：'aa'
#输入：135
#输出：ls5
#ls5=[['mark',99],['htl',120],['ghh',130],['aa',135],['xzj',140],['xzh',150]]
# ls5=[['mark',99],['htl',120],['ghh',130],['xzj',140],['xzh',150]]
# name=input('输入一个名字')
# score=eval('输入一个分数')
# s_n= [name,score]    #学生名字和分数组成的列表
# idx= ls5.index(['xzj',140])     #找到140分所在列表元素的索引号
# ls5.insert(idx,s_n)       #把s_n插入到140所在列表的前面。
# print(ls5)
#请输入10个数字，如果是偶数，请放在列表的最前面，如果是奇数，请放在列表的最后面。
ls6=[]
for i in range(10):
    num=eval(input("请输入一个数："))
    if num%2==0:      #为偶数
        ls6.insert(0,num)    #插入到最前面
    else:       #为奇数
        ls6.append(num)   #加入到最后面。
print(ls6)