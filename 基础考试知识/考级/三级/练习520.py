# def fun(b):     #取余法
#     #bin(b)      #用了别人的方法，官方给的函数
#     count=0
#     while b:
#         if b%2==1:
#             count+=1
#         b = int(b/2)            #b//=2
#     return count
#写一个函数判断这个数转成二进制后有几个1

#00000000000000000000000000000001
#000000000000000000000000000000001      右移1位

#00000000000000000000000000000001
#00000000000000000000000000000010    左移1位    2
#00000000000000000000000000000100    左移2位    4
# def fun(b):  #位移法
#     count=0
#     while b:
#         if b%2==1:
#             count +=1
#         b>>=1
#     return count

# def fun(b):  #位与，位或，位异或
#     count=0
#     while b:
#         if b&1==1:
#             count +=1
#         b>>=1
#     return count

# def fun():
#     a=10
#     b=20
#     #值交换方法
#     # tem=a
#     # a=b
#     # b=tem
#     #加减乘除，% //  位与，位或，位异
#     # a=a+b       #a=30  b=20
#     # b=a-b       #b=30-20=10   a=30
#     # a=a-b       #a=30-10=20   b=10
#     a=a^b
#     b=a^b
#     a=a^b
#     print(a,b)

# def wfun(c):
#     with open("city.csv",'w',encoding='utf-8') as f:
#         f.write(','.join(c))
#     print("写入完毕。")
#     return "city.csv"
#
# def rfun(filename):
#     with open(filename,'r',encoding='utf-8') as f:
#         citys=f.read().split(',')
#         return citys

#if __name__ == '__main__':
    # c = [['张三','95','96','97','98'],['李四','90','91','97','98'],['王五','85','86','87','90']]
    # re=wfun(c)      #写一个函数把c列表中的城市存入文件city.csv中。
    # ls=rfun(re)     #写一个函数读取re文件内容，返回的是一个列表
    # print("这个是返回的LS",ls)
import random as r
def randfun(n):
    ls=[]
    for i in range(n):
        s=chr(r.randint(97,122))
        while s in ls:
            s = chr(r.randint(97, 122))
        ls.append(s)
    print("这个是原列表：",ls)
    return ls
if __name__ == '__main__':
    ls=randfun(13)       #产生13个随机不重复小写字母
    ls.sort()
    print("这个是新列表：",ls)