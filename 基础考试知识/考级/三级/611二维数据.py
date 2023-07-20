c = [
    ['张三','95','96','97','98'],
    ['李四','90','91','97','98'],
    ['王五','85','86','87','90'],
]

#遍历列表
# for i in c:         #for i in 序列：
#     print(i)
# for i in range(len(c)):     #len(c)求列表的长度
#     print(i,c[i])
# f=open('611.csv','w',encoding='utf-8')
# f.write('aa,bb,cc')
# f.close()
f=open('611.csv','w',encoding='utf-8')
for i in c:   #c是一个二维列表
    print(i)  #i是一个列表，他的每个元素是一个字符串
    #变成字符串
    str1=','.join(i)
    f.write(str1+'\n')   #写入的必需是一个字符串。所以要把i变成字符串。
f.close()