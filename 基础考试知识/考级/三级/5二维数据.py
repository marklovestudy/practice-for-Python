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
# def fwrite(ls2,filename):
#     f=open(filename,'w',encoding='utf-8')
#     for i in ls2:
#         for j in i:
#             f.write(j+',')
#         f.write('\n')
#     f.close()
#
# def fread(filename):
#     ls=[]
#     f = open(filename, 'r', encoding='utf-8')
#     ls1=f.read().strip('\n').split('\n')
#     # "姓名, 语文, 数学, 英语, 特长,\n张三, 95, 96, 97, 98,\n李四, 90, 91, 97, 98,\n王五, 85, 86, 87, 90,"
#     # ["姓名, 语文, 数学, 英语, 特长,"   ,  "张三, 95, 96, 97, 98,"  ,  "李四, 90, 91, 97, 98,"  ,  "王五, 85, 86, 87, 90,"]
#     # ["姓名, 语文, 数学, 英语, 特长", "张三, 95, 96, 97, 98", "李四, 90, 91, 97, 98", "王五, 85, 86, 87, 90"]
#     for row in ls1:
#         ls.append(row.strip(',').split(','))
#     return ls
#
# def sum_score(re):
#     return [[i[0],eval('+'.join(i[1:]))] for i in re[1:]]
#
# if __name__ == '__main__':
#     c = [
#         ['姓名', '语文', '数学', '英语', '特长'],
#         ['张三', '95', '96', '97', '98'],
#         ['李四', '90', '91', '97', '98'],
#         ['王五', '85', '86', '87', '90']
#     ]
#     filename='two.csv'
#     fwrite(c,filename)           #把C这个二维数据写入文件'two.csv'中
#     re=fread(filename)          #把文件内容读取出来。用re接收。
#     #[['张三', '277'],['李四', '288'],['王五', '287']]
#     reslut=sum_score(re)          #请计算出re列表中的学生的总分
#     print(reslut)

ls=filter(lambda x:x[0]+x[1]+x[2]==25 and x[0]+2*x[1]+5*x[2] == 50,[[i,j,k] for i in range(1,26) for j in range(1,26) for k in range(1,26)] )
print(list(ls))
