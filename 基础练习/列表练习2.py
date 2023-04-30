scores=[55,66,77,22,33,87,43,45,89,99]
#请计算全班的总分
#请计算平均分

#增     删除     改     访问
list1=[]
#增
list1.append(1)
#删除   ，remove()值删除
list1.pop(0)    #pop()索引删除
list1.remove(4) #remove()值删除
#改 访问  单个改，区间改，步长改
#单个
list1[0]    #访问
list1[0]=22 #改
#多个
list1[0:2]  #区间访问
list1[0:2]=[1,2,3]  #区间改
#步长
list1[0::2]    #步长访问
list1[0::2]=[11,22,33,44]       #步长修改
# #第一种方法：for
# s=0     #和
# for i in scores:
#     s+=i
# for i in range(10):
#     s+=scores[i]
# #第二种方法用函数
# s=sum(scores)       #和
# l=len(scores)       #有几项，长度
# v=s/l               #平均分
#第三种，推导式的方法：
# import random as r
# scores=[r.randint(0,100) for i in range(50)]
# print(scores)


names=[['mark',66,77,56],['xx',76,57,96],['yy',55,87,66]]
s=[]
#请统计班上每个学生的总分,并把分数用append添加到s列表中。

#第一种方法
for i in names:
    # print(i)
    print(i[1:])
    v=sum(i[1:])
    s.append(v)
print(s)
#第二种方法
# s=[sum(i[1:]) for i in names]
# print(s)