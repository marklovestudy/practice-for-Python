#推导式创建列表
# ls1=[1 for i in range(100)]
#
# import random as r
# ls2=[r.randint(1,100) for i in range(25)]
# #randint(1,100) 是指在1-100之间取随机整数。
# print(ls2)
# #请创建一个元素为随机26个小写字母的列表，元素有25个。
# # 'abcde-----z'[0-25]
# str1='abcdefghijklmnopqrstuvwxyz'
# ls3=[str1[r.randint(0,25)] for i in range(25)]
# print(ls3)
# str2='mark'
# ls4=[i for i in str2]
# print(ls4)
#请输入一个字符串input()
#用for循环遍历，如果是：123  if elif else
#1请把这个字符串中的字母加入v1列表中.isalpha()
#2请把这个字符串中的数字加入v2列表中.isdigit()
#3请把这个字符串中的其它加入v3列表中   用append()加入
# str1=input("请输入一个字符串：")
# v1=[]
# v2=[]
# v3=[]
# for i in str1:
#     if i.isalpha():             #判断是不是字母和汉字，如果是返回True,如果不是返回False  字符串45个，列表11个，元组2，集合10，字典13个
#         v1.append(i)
#     elif i.isdigit():           #判断是不是数字，如果是返回True,如果不是返回False
#         v2.append(i)
#     else:                       #其它
#         v3.append(i)
# print("这个是V1:",v1)
# print("这个是V2:",v2)
# print("这个是V3:",v3)

# st1='abc123def456'
# n=eval(input("请输一个整数"))   #输入：2   打印：c123def45ab
# #输入：3   打印：123def45abc
# for i in range(n):
#     st1=st1[1:]+st1[0]
# print(st1)

v=["mark","dafei","lingling","xmkai","hongkong",'zjl']
v1=v.copy()
#请删除元素长度小于6的元素 ，pop(索引号) remove(值)
# 求数据长度len(数据)
for name in v1:
    if len(name)<6:
        v.remove(name)
print(v)

