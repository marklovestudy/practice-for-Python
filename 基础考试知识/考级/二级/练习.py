# text='I am sk,I am from china,I like play football and game.'
# #1请把text,标题化。
# #2请在text中计算‘a’的数量
# #3请判断text是不是以's'开头，是不是以'e'结尾。
# d1=dict(zip((1,2,3),(4,5,6)))
# print(d1)
# d1['a']='aa'
# d1['b']='bb'
# d1['c']='cc'
# print(d1)
# #遍历字典的键：第一种方式。
# for k in d1:
#     print(k)
# #遍历字典的键：第二种方式。
# for k in d1.keys():
#     print(k)
# #遍历值
# for v in d1.values():
#     print(v)
#
# for k,v in d1.items():
#     print(k,v)
#怎么遍历键：二种方法，
#怎么遍历值：一种方法，
#怎么遍历键和值：一种方法。

#创建一个怪物列表
# import random as r
# list1=['僵尸','狼人','精灵']
# list2=[r.choice(list1) for i in range(100)]
# #用fromkeys()方式创建一个怪物字典d1，血量100
# d1=dict().fromkeys(list1,100)
# while len(d1):
#     for k,v in d1.items():
#         if v <= 0:
#             d1.pop(k)
#             break
#         else:
#             d1[k] -= r.randint(0,5)
#     print(d1)
# print('已经杀死全部怪物')

# 请用while循环计算：
# n=eval(input('n=?'))
# s=1*2*3...n     #1
# s=1+2+3...n     #2
# while True:
#     print('计算数的阶乘：s=1*2*3...*n')
#     n = eval(input('n=?'))
#     s = 1
#     a = 1
#     while a <= n:
#         s *= a
#         a += 1
#     print('从1乘到%s的结果是%s'%(n,s))
#插入排序：
# import random as r
# l=[r.randint(0,100) for i in range(25)]
# print(l)
# def insertsort(l):
#     for i in range(1,len(l)):       #次数
#         for j in range(i+1):          #范围
#             if l[j] > l[i]:
#                 l.insert(j,l.pop(i))
#                 break
# insertsort(l)
# print(l)

#1创建一个‘键-值’对为姓名-年龄，如：'mark':38的字典,字典有三个以上的元素
#2创建一个while循环,当用户输入姓名时，输出用户对应的年龄。
#3当用户输入‘q’时，退出循环。

#请取出'how are you today? fine thank you and you?'
#第一种方法用字符索引取
#用split取
#用range()取
# a='how are you today? fine thank you and you?'
# v=a.split('?')
# print(v)
# print(range(len(a)))

#方法1：翻译法则
#1创建一个翻译法则
#2按翻译法则翻译被翻译的对象
# 方法2：索引取值
# v=eval(input('v?'))
# print(b[v])
# 方法3：列表索引取值
# 方法：if
# a='123456789'
# b='一二三四五六七八九'
# f=str.maketrans(a,b)
# while True:
#     v=input('put in')
#     new=v.translate(f)
#     print(new)
# with open('aa.txt','w',encoding='utf-8') as f:
#     f.write('aaasdddd')

# dict1={'name':'mark','age':38,'tall':173}
# print(dict1.get('name'))        #方法1
# print(dict1['age'])             #方法2
# dict1['name']='tank'            #修改内容
# print(dict1)
# dict1['sex']='male'             #增加元素
# print(dict1)                    #


#list1请随机创建一个列表含50个元素，范围：a-z
#str1=list1转变而来
# dict1={'d':7,'f':8,'s':3}       #随机出现的字符串。
#a-z,请创建一个字典来统计字母出现的次数，键值对如：'字母'：数量
# import random as r
# zm='abcdefghijklmn'
# list1=[r.choice(zm) for i in range(50)]
# str1=''.join(list1)     #'ceabnbgemnbklnmibgaclkfbblkgjegnhdfjjle'
# dict1=dict()
# for i in str1:
#       if i not in dict1:
#             dict1[i]= str1.count(i)        #值 str1.count(i)
# print(str1)
# print(dict1)
#求s=1*2*3*4....*n    叫n的阶乘
#求s=1+2+3+4+5+6....n   求和
# s=1
# n= eval(input('你想求几个阶乘：?'))
# while n>1:                    #运用条件变化控制while,break,continue
#       s *= n
#       n -= 1
# print('阶乘为：',s)
# import time
# for j in range(10):                             #二级
#       print(j)
#       for i in range(10000):                    #一级
#             time.sleep(1)
#             if i%2==0:
#                 continue                        #continue跳出本次循环
#                 print('碰到了continue',i)
#             elif i == 11:
#                   break                         #break停止当前循环体
#
#             print('没有碰到continue',i)


#1创建：变量str1='marksfeifeisweiweisxiaomingszzhshysteacher'
#2请把字符串以's'分割成列表。
#3请遍历列表，当碰到weiwei时跳过，当碰到hy时停止整个循环
# str1='marksfeifeisweiweisxiaomingszzhshysteacher'
# list1=str1.split('s')
# import time
# for i in range(100):
#     if i == 20:
#         break
#     for j in range(30):
#         print('第%s次'%i,j)
#     time.sleep(0.2)
