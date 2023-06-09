'''
百钱买百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题，问题的原文是：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
这个问题用现代文描述起来就是：公鸡5文钱1只，母鸡3文钱1只，小鸡3只1文钱。
如果用100文钱买100只鸡，那么公鸡、母鸡和小鸡各应该买多少只呢？
请完成下面程序中空白处的语句，实现对问题的求解，找出所有符合题目要求的买鸡方案，并输出。
'''
#分析问题：100钱，
# 5钱一只g,g>=1,g<=19
# 3钱一只m,m>=1,m<=31
# 1钱三只x.x>=1,x<=98
# 一共要买100只：g+m+x=100只
# for g in range(1,21):
#     for m in range(1,34):
#         for x in range(1,99):
#             if g+m+x==100 and 5*g+3*m+x/3==100:
#                 print("公鸡:{}，母鸡：{}，小鸡：{}".format(g,m,x))
"""
>>> "how are you? %s"%'mark'
'how are you? mark'
>>> "how are you? %s   %f    %d"%('mark',4.5,6.8)    #占位符
'how are you? mark   4.500000    6'
>>> "how are you? %s"%5
'how are you? 5'
>>> #引用符
>>> name='王欣宇'
>>> name
'王欣宇'
>>> f"how are you? {name}"
'how are you? 王欣宇'
>>> "how are you? {}".format(name)
'how are you? 王欣宇'

关系运算符：> < != == >= <=
逻辑运算：and or not
"""

#若要生成一个由若干小写字母组成的互不重复的随机数组，
# 已知小写字母的ASCII码值为97~122整数范围，并将其进行从小到大输出，
# 如图所示，请将相关程序补充完整。
import random as r              #导入随机库
ls=[]                           #创建一个空列表
n=eval(input('有多少个元素'))     #0-26个元素
while n>0:                      #n表示有n元素,每添加一个元素，n减少1
    x=r.randint(97,122)         #随机生成一个97-122之间的整数
    c=chr(x)                    #把整数转换为整数所对应的ascii码字符
    if c not in ls:             #如果这个字符不在列表中，添加，字符数减少1
        ls.append(c)
        n-=1
print('排序前：',ls)
ls.sort()   #排序
print('排序后：',ls)


#ord/chr/sort方法的使用如下：
'''
>>> ord('s')            #找字符's'所对应的ascii码数字
115
>>> chr(115)            #找数字所对应的ascii码字符
's'
>>> chr(122)
'z'
>>> [3,2,6].sort()      #对列表排序的使用方法
>>> ls=[3,2,6]
>>> ls.sort()           #对列表进行排序
>>> ls
[2, 3, 6]
>>> ls=['b','c','a']
>>> ls.sort()           #对列表进行排序
>>> ls
['a', 'b', 'c']
'''
