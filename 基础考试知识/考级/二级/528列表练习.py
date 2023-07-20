# names=[]        #创建一个列表
# names.append('黄天乐')         #添加元素
# names.append('关浩华')
# names.append('谢政江')
# names.append('谢政洪')
# print(names)
#列表的访问
#print('这个是索引号为2：',names[2])
# for name in names:    #遍历列表-元素从左到右
#     print("你好啊：%s，你吃了吗？"%name)
#     print("我吃了啊。。可香啦！！")
#
#     #names[0],names[1],names[2],names[3],用索引号来遍历
# for i in range(4):
#     print("你好啊：%s，你吃了吗？"%names[i])
#     print("我吃了啊。。可香啦！！")

# weeks=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
# #当输入：1，输出星期一。
# #当输入：7，输出星期日。
# while True:
#     n=eval(input("请输出1-7"))
#     if n >7 or n<1:
#         print("输入错误。")
#     else:
#         print(weeks[n-1])        #当输入：1，输出星期一。当输入：7，输出星期日。

score=[]
#询问，语文考了多少，数学考了多少，英语考了多少。
#把分数分别添加到列表score中。打印出列表。
english=eval(input("english=?"))
score.append(english)
math_s=eval(input("math=?"))
score.append(math_s)
chinese=eval(input("chinese=?"))
score.append(chinese)
#请计算出总分，和平均分。用遍历的方式去计算
s=0
for i in score:
    s+=i            #s+=i    s=s+i
av=s/3
print("总分：%s, 平均分：%s"%(s,av))