'''
二维数据
    二维数据 由多个一维数据构成，是一维数据的组合形式，可以用二维列表表示。列表的每个元素对应二维数据的一行，这个元素本身也是列表。
    二维数据一般采用相同的数据类型存储数据。

二维数据的表示:
c=[['张三','95','96','97','98'],['李四','90','91','97','98'],['王五','85','86','87','90']]

数据写入：
c = [
    ['张三','95','96','97','98'],
    ['李四','90','91','97','98'],
    ['王五','85','86','87','90'],
]
f = open('cj.csv','w',encoding='utf-8')
for i in c:
    f.write(','.join(i)+'\n')
f.close()

数据读取
f = open('cj.csv','r',encoding='utf-8')
c = []
for i in f:
    c.append(i.strip().split(','))
f.close()
print(c)

二维数据处理，等同于二维列表操作，借助循环遍历，实现对每个数据的处理。
f = open('cj.csv','r',encoding='utf-8')
c = []
for i in f:
    c.append(i.strip().split(','))
f.close()
print(c)

for i in c:
    line = ''
    for j in i:
        line += '{:10}\t'.format(j)
    print(line)

数据的共享方法：
import json
date = [1,2,3,4]     #tuple,dict,list,str等。
f = open('file.json','w')
json.dump(date,f)
'''
# c=[
#     ['姓名','语文','数学','英语','特长'],
#     ['张三','95','96','97','98'],
#     ['李四','90','91','97','98'],
#     ['王五','85','86','87','90']
# ]
# f = open('naa.csv','w',encoding='utf-8')
# for i in c:
#     f.write(','.join(i)+'\n')
# f.close()
#
# f = open('naa.csv','r',encoding='utf-8')
# c = []
# v = f.readlines()
# for i in v:
#     print(i)
#     a = i.strip().split(',')
#     c.append(a)
# f.close()
# print(c)

import json
f = open('naa.csv','r',encoding='utf-8')
v = f.read()
print(v)
print(type(v))
# f1 = open('naaa.json','w')
# json.dump(v,f1)
# f.close()
# f1.close()
#
# f1 = open('naaa.json','r')
# v = json.load(f1)
# print(v)
# print(type(v))