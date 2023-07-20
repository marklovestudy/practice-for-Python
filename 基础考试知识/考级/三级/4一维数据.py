'''
一维数据 由对等关系的有序或无序数据构成，采用线性方式组织，对应数学中的数组的概念
一维数据具有线性特点。
任何表现为序列或集合的对象都可以看作是一维数据。

一维数据的表示
主要用列表表示。
c = ['北京'，'上海','广州','深圳']

一维数据的存储
1.采用空格分隔元素
2.采用逗号分隔元素      #常用，CSV格式
3.采用换行分隔元素
4.采用其它特殊符号分隔元素（比如;）

注：CSV格式
CSV格式就是逗号分隔值，是一种通用的、相对简单的文件格式，广泛应用，大部分编辑器都支持直接读入或保存为CSV格式。记事本、excel等。扩展名：.csv

存储数据
c = ['北京','上海','广州','深圳']
f = open('city.csv','w',encoding='utf-8')
f.write(','.join(c)+'\n')
f.close()

读取数据
c = ['北京','上海','广州','深圳']
f = open('city.csv','r',encoding='utf-8')
f.read().strip().split(',')
f.close()
print(c)
'''
# fo=open('class1.csv','w',encoding='utf-8')
# print(fo)
# names = ['姓名','年龄','身高','体重']
# fo.write(','.join(names)+'\n')
# for i in range(4):
#     e=input("请输入名字，年龄，身高，体重：")
#     fo.write(e+'\n')
# fo.close()
# fo=open('1十进制与二进制.py','r',encoding='utf-8')
# #read()读取全部，返回一个字符串
# #readline() 读取光标行   #readlines()读取全部，返回一个列表，每个元素是一行
# #请读取一个文件，计算里面的，
# # 1小字英文字符的数量，       ord('a')+26
# # 2大字英文字符的数量，       ord('A')+26
# # 3中文字符的数量，          u'\u4e00'-u'\u9fa5'
# # 4数字的数量，             isdigit()
# #5其它字符的数量。
# #6所有字符的数量。          len(str)
# e=0
# E=0
# c=0
# for i in fo.read():
#     if ord('a')<=ord(i)<=ord('a')+26:
#         e+=1
#     elif ord('A')<=ord(i)<=ord('A')+26:
#         E+=1
#     elif u'\u4e00'<=i<=u'\u9fa5':
#         c+=1
# print(e,E,c)

