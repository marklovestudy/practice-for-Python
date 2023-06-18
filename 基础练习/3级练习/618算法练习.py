#有50道门，这50道编号为1-50.这50道门开始是关闭的
#什么相反操作：如果门是关闭的就打，如果是打开的就闭
#1号操作员，会把所有1的倍数的门作相反的操作。
#2号操作员，会把所有2的倍数的门作相反的操作。
#3号操作员，会把所有3的倍数的门作相反的操作。
#4号操作员，会把所有4的倍数的门作相反的操作。
#。。。。。。。。
#50号操作员，会把所有50的倍数的门作相反的操作。
#问哪些门是打开的。
#创建50个-1列表      -1代表关闭。
# import time
# list1=[-1 for i in range(51)]   #推导式：l1=[元素 个数]
# print(list1)
# for i in range(1,51):         #i=1,代表1号操作员
#     for j in range(1,51):       #所有的门，0索引的除外
#         if j%i==0:              #j是i的倍数，作相反操作
#             list1[j]=-list1[j]
#             print('门信息：')
#             print(list1)
#             time.sleep(0.1)
# sum=0
# for i in range(51):
#     if list1[i]==1:
#         print(i,'号门是开着的。')
#         sum+=1
# print('打开门的总数为：',sum)

#统计50以内的奇数和
# sum=0
# for i in range(50):
#     if i%2==1:
#         sum+=i
# print(sum)

# #统计100以内所有2和3的倍数的数之和
# sum=0
# for i in range(100):
#     if i%2==0 or i%3==0:
#         sum+=i
# print(sum)
#
# #统计10以内所有数的平方之和
# sum=0
# for i in range(10):
#     sum+=i*i
# print(sum)

# #统计10以内:1-1/(2*2)+1/(3*3)-1/(4*4)....-1/(10*10)   ?
# #1+1/(2*2)+1/(3*3)+1/(4*4)....+1/(10*10)
# sum=0
# for i in range(1,11):
#     sum=sum+(-1)**(i-1)*1/(i*i)
# print(sum)

sum=0
for i in range(1,4):
    # sum=sum*10+i   #123
    sum=sum+i*10**(i-1)
print(sum)   #在？处填一个空，使输出为321

