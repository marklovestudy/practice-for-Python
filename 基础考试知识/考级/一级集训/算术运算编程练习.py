"""
计算长方形的面积要求： (1)利用input()语句输入长方形的长和宽；
(2)利用运算符*，求得长方形的面积；
(3)利用print()语句输出长方形的面积。
输入格式：
第一次输入一个数字，代表长方形的长；
第二次输入一个数字，代表长方形的宽。
(输入有相应的提示信息,如：'请输入长方形的长：')
输出格式：
输出长方形的面积。(输出有相应的提示信息,如：'长方形的面积为：')
"""
# a = input('请问宽是多少：')
# b = input('请问长是多少：')
# s = eval(a)*eval(b)   s = float(a) * float(b)
# print('长方形的面积是：',s)
''' 
假设孩子的身高完全由爸爸和妈妈的遗传因素决定，预测一下长大后孩子的身高是多少？
孩子获得了爸爸妈妈各一半的遗传基因，所以可以用以下公式计算孩子未来的身高。（单位：厘米）
孩子未来的身高=（爸爸的身高+妈妈的身高+13乘以性别系数）/2
如果是“男孩”，性别系数值为“1”；如果是“女孩”，则性别系数值为“-1”。
输入格式：
第一行输入一个数字，代表爸爸的身高
第二行输入一个数字，代表妈妈的身高
第三行输入一个数字（1或-1），代表性别系数
（输入使用input()，并有相应提示信息）
输出格式：要求：用到eval()/float(),print(),input(),占位符%s
输出孩子未来的身高。
（输出使用print()，并有相应提示信息）
友情提示：
由于考试平台暂不支持eval()命令，同学们可以选用其他命令；当然如果您使用了eval，只要程序是正确的，我们阅卷时依然按照正确处理。
'''
# a = eval(input('你爸爸的身高是：'))
# b = eval(input('你妈妈的身高是：'))
# c = eval(input('你的性别是：'))
# h = (a+b+13*c)/2
# print('你未来的身高是：',h)
# print('你未来的身高是：%s'%h)
# print('你爸爸的身体%s,你妈妈的身高是%s,你未来的身高是：%s'%(a,b,h))

"""
计算三角形的面积要求： (1)利用input()语句输入三角形的底和高；
(2)利用运算符*，求得三角形的面积；
(3)利用print()语句输出三角形的面积。
输入格式：
第一次输入一个数字，代表三角形的底；
第二次输入一个数字，代表三角形的高。
(输入有相应的提示信息,如：'请输入三角形的底：')
输出格式：
输出三角形的面积。(输出有相应的提示信息,如：'三角形的面积为：')
"""
# a = input('底是多少')
# h = input('高是多少')
# s = 1/2*eval(a)*eval(h)
# print('三角形的面积是：',s)
'''
计算梯形的面积要求： 
(1)利用input()语句输入上底、下底和高；
(2)利用运算符*，求得面积；
(3)利用print()语句输出面积。
输入格式：
第一次输入一个数字，代表上底；
第二次输入一个数字，代表下底；
第三次输入一个数字，代表高。
(输入有相应的提示信息,如：'请输入上底：')
输出格式：
输出面积。(输出有相应的提示信息,如：'梯形的面积为：')  
'''
# a = input('上底是多少')
# b = input('下底是多少')
# h = input('高是多少')
# s = (eval(a)+eval(b))*eval(h)/2
# print('梯形的面积是：',s)


'''
y = kx + b
直线输入要求： 
(1)利用input()语句输入K和b值；
(2)利用input()询问x的值；
(3)利用y = kx + b求出y的值，并打印出y'输出有相应的提示信息'
(4)利用y = kx + b得到一条直线。并在turtle画出直线
'''

# K = input('斜率K的值是多少：')
# b = input('截距b的值是多少：')
# x = input('x坐标的取值是多少：')
# y = eval(K)*eval(x)+eval(b)
# print('直线y=Kx+b，当x坐标为%s时，y的坐标是%s'%(x,y))

# import turtle as t
# K = input('斜率K的值是多少：')
# b = input('截距b的值是多少：')
# x = -300
# t.penup()
# for i in range(600):
#     y = eval(K)*x+eval(b)
#     t.goto(x,y)
#     t.pendown()
#     x += 1
# t.mainloop()


# import turtle as t
# a = input('a')
# b = input('b')
# x = -300
# t.penup()
# for i in range(600):
#     y2 = (1-x**2/eval(a)**2)*eval(b)**2
#     y = pow(y2,1/2)
#     t.goto(x,y)
#     t.pendown()
#     t.goto(x,-y)
#     x += 1
# t.mainloop()

"""
计算总分要求： 
(1)利用input()语句输入个一同学的姓名，以及这个同学语文，数学，英语成绩。
(2)利用运算符，求得这个同学的总分和平均分；
(3)利用print()语句输出这个位同学的总分和平均分。
输入格式：
第一步输入姓名；
第二步输入该同学的语文，数学，英语成绩；
第三步计算该同学的总分。
(输入有相应的提示信息,如：'请输入姓名：')
输出格式：
(输出有相应的提示信息,如：'**同学的总分为**')
"""
# name1 = input('学生的名字：')
# chinese1 = input('语文成绩：')
# math1 = input('数学成绩：')
# e_glist1 = input('英语成绩：')
# s1 = eval(chinese1)+eval(math1)+eval(e_glist1)
#
# # name2 = input('学生的名字：')
# # chinese2 = input('语文成绩：')
# # math2 = input('数学成绩：')
# # e_glist2 = input('英语成绩：')
# # s2 = eval(chinese2)+eval(math2)+eval(e_glist2)
# #
# # name3 = input('学生的名字：')
# # chinese3 = input('语文成绩：')
# # math3 = input('数学成绩：')
# # e_glist3 = input('英语成绩：')
# # s3 = eval(chinese3)+eval(math3)+eval(e_glist3)
#
# print(name1,'的总成绩是',s1)
# print(name1+'的总成绩是'+s1)
# print('%s的总成绩是%s'%(name1,s1,))
# # print('%s的成绩是%s'%(name2,s2,))
# # print('%s的成绩是%s'%(name3,s3,))
# print(f'{name1}的总成绩是{s1}')
# print('{0}的总成绩是{1}'.format(name1,s1))
# print('{name}的总成绩是{s}'.format(name=name1,s=s1))
# print('{name}的总成绩是{s}'.format_map({'name':name1,'s':s1}))
#
# # 计算y = ax + b要求：
# # (1)利用input()a、x、b的值，
# # (2)利用运算符，求得y；
# # (3)利用print()语句输出y的值，如：'y的值是：‘
# a = float(input('a=?'))
# x = float(input('x=?'))
# b = float(input('b=?'))
# y = a * x + b
# print('y的值是%s'%y)
#
# # 请用速度公式。写一个简单的算法：
# # 第一步：input()变量速度是多少
# # 第二步：input()变量时间是多少
# # 第三步：根据速度公式s = v*t求出距离s
# # 第四步：打印出速度是多少，时间是多少，距离是多少。请用点位符的形式输出
# # 注:print('%s...%s...%s'%(v,t,s))
# v = float(input('速度是多少'))
# t = float(input('时间是多少'))
# s = v * t
# print('速度是%s,时间是%s，经过的距离是%s。'%(v,t,s))

# 请用速度公式。写一个简单的算法：
# 第一步：input()一分钟的圈数，轮子一圈是2米，你能做的就是统计轮子一分钟转了多少圈。
# 第二步：利用轮子算出距离。
# 第三步：根据速度公式v = s/t求出速度
# 第四步：判断120公里/每小时，说明超速，否则不超，请设计一个程序告诉
#       司机是否超速
#       120公里/每小时=120 000米/60分钟 = 2000 米/1分钟 = 1000圈/1分钟
# 第五步：打印出多少圈是越速的。多少圈以内是合格的。
#解答：120公里/每小时=120 000米/60分钟 = 2000 米/1分钟 = 1000圈/1分钟
# n = eval(input('一分钟的圈数？'))
# if n > 1000:
#     print('%s圈一分钟超速了'%n)
# else:
#     print('%s圈一分钟没有超速'%n)
'''无人驾驶'''
#一台车，有左右二个红外线眼睛，如果左边的值大于300，说明左边有障碍物
#如果右边的值大于300，说明右边有障碍物
# 左边大于300时右转，右边大于300时左转，
#左右二边同时大于300，后退
#如果没有障碍物就前进
#请写一道编程，让这台车有这样的智能系统
#1  v_l左边的眼睛的值用input()输入一个数
#2  v_r右边的眼睛的值用input()输入一个数
#3  判断车应该怎么动。
# v_l = eval(input('左眼'))
# v_r = eval(input('右眼'))
# if v_l > 300 and v_r <= 300:
#     print('右转')
# elif v_l <= 300 and v_r > 300:
#     print('左转')
# elif v_l > 300 and v_r > 300:
#     print('后退，再左转或右转')
# else:
#     print('前进')

a = input('请问宽是多少：')
b = input('请问长是多少：')
# s = int(a)*int(b)
s = float(a) * float(b)
print('长方形的面积是：',s)


