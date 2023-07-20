'''
关系运算符： ==、<、>、<=、>=、!=
逻辑运算符：and or not

假设孩子的身高完全由爸爸和妈妈的遗传因素决定，预测一下长大后孩子的身高是多少？
孩子获得了爸爸妈妈各一半的遗传基因，所以可以用以下公式计算孩子未来的身高。（单位：厘米）
孩子未来的身高=（爸爸的身高+妈妈的身高+13乘以性别系数）/2
如果是“男孩”，性别系数值为“1”；如果是“女孩”，则性别系数值为“-1”。

输入格式：
第一行输入一个数字，代表爸爸的身高
第二行输入一个数字，代表妈妈的身高
第三行输入一个数字（1或-1），代表性别系数
（输入使用input()，并有相应提示信息）
输出格式：
输出孩子未来的身高。
（输出使用print()，并有相应提示信息）
友情提示：
由于考试平台暂不支持eval()命令，同学们可以选用其他命令；当然如果您使用了eval，只要程序是正确的，我们阅卷时依然按照正确处理。

# a = input('你爸爸的身高是：')
# b = input('你妈妈的身高是：')
# c = input('你的性别是：')
# h = (float(a)+float(b)+13*float(c))/2
# print('你未来的身高是：',h)
# print('你未来的身高是：%s',%h)
# print('你爸爸的身体%s,你妈妈的身高是%s,你未来的身高是：%s'%(a,b,h))

'''

import turtle
t = turtle.Turtle() #类   对象1
t.right(90)
t.forward(100)
t.left(90)
t.circle(-50)

p = turtle.Turtle()     #对象2
p.left(90)
p.forward(100)
p.setx(p.xcor()-50)
for i in range(4):
    p.forward(100)
    p.right(90)

a = turtle.Pen()    #类  对象3
a.forward(100)
a.sety(a.ycor()-50)
a.sety(a.ycor()+100)

turtle.backward(100)    #对象4
for i in range(3):
    turtle.backward(100)
    turtle.right(120)



