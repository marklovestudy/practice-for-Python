#甲乙丙丁，干了一坏事，是谁做了坏事呢。
#只有一个人说了真话。
#甲：是乙干的。1         xt==2         true 1    False 0
#乙：是丁干的。2         xt==4
#丙：不是我干的。3       xt!=3
#丁：不是我。4          xt!=4
# for xt in range(1,5):
#     if (xt==2)+(xt==4)+(xt!=3)+(xt!=4)==1:
#         print(xt)

#一天校长到机器人教室检查，看到电脑游戏是开着的，校长问，谁在玩游戏：
#黄天乐说：是关浩华在玩   1        pl==2
#关浩华说：不是我。      2        pl!=2
#谢政兄弟说：不是我们。    3       pl!=3
#上面只有一句是真的。问谁在玩游戏。
# for pl in range(1,4):
#     if (pl==2) + (pl!=2) + (pl!=3) == 1:
#         print(pl)


'''
序列的通用方法   len(序列)：求序列的长度
'''
# str1=input("请输入一个字符串")
# sz=len(str1)
# print("%s的长度为：%d"%(str1,sz))
# ls1=['mark','ak',[1,2,3,4,5,6]]
# #问题1：请求出ls1的长度（元素个素）。打印出来。
# sz=len(ls1)
# print("ls1的长度是：",sz)
# #问题2：求出ls1的每个元素的长度。打印出来。
# for i in ls1:
#     sz=len(i)
#     print("%s的长度是%d"%(i,sz))

# #推导式   ls=[i for i in range(25)]
# import random as r     #r.randint(最小整数，最大整数)
# #1请用推导式创建一个列表  l1=[1,2,3,4,5]
# l1=[i for i in range(1,6)]
# #2请用推导式创建一个列表  l2=[元素 个数]  元素为0-100的随机数，个数为10个
# l2=[r.randint(0,100) for i in range(10)]
# #3请用推导式创建一个列表  l3=[元素 个数]  元素为0-100的随机数，个数为10-20个随机数
# l3=[r.randint(0,100) for i in range(r.randint(10,20))]
# #4请用len()求出l3的长度。
# sz=len(l3)
# print(sz)
# #5请求出l3所有元素的和。   s=0     s+=元素1   元素2   元素3
# s=0
# for i in l3:
#     s+=i
# print(s)
# #sum()专门用来求和的
# #6请求出l3元素的平均数。
# av=s/sz
# print(av)

# >>> ls1=[1,2,3,4,5]
# >>> sum(ls1)
# 15
# >>> sum((1,2,3))
# 6

#7,请求和1-5
print(sum(range(1,6)))
#8,请求和6-10
print(sum(range(6,11)))
#9，请求和所有0-100包含100偶数和
print(sum(range(0,101,2)))
#10，请求和所有0-100包含奇数和
print(sum(range(1,100,2)))
