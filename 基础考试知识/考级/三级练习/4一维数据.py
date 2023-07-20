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

names = ['mark','weiwei','dafei','xigua']
f = open('na.csv','w',encoding='utf-8')
print(type(','.join(names)+'\n'))
print(','.join(names)+'\n')
f.write(','.join(names)+'\n')
f.close()

f = open('na.csv','r',encoding='utf-8')
name = f.read().strip().split(',')
f.close()
print(name)