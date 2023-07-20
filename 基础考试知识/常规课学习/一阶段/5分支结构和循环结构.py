'''
1顺序结构：由上向下运行
print('hello')
print('money')
print(123)

print('hello')
name = input('your name:?')
if name == 'mark':
    print('ok')
print(22)
2分支结构：
    二分支：if else:
print('hello')
name = input('your name:?')
if name == 'mark':
    print('ok')
else:
    print('no')
print(123)
    三分支和多分支：if elif else/if elif elif elif
print('hello')
name = input('your name:?')
if name == 'mark':
    print('ok')
elif name == '学生':
    print('很好')
else:
    print('no')
print(123)

    分支结构的嵌套
#1先询问你是男的还是女的。多少岁了
#利用分支结构和分支嵌套输出下面的信息。
#2如果你是男的：1，如果没满18岁，你不能工作。
#             2，你满18岁，你就可以工作了，拿100%工资。
#             3,如果你60，你就退休了。拿3000的退休工资。
#3如果你是女的：1，如果没满16岁，你不能工作。
#             2，你满16岁，你就可以工作了，拿100%工资。
#             3,如果你55岁，你就退休了。拿3000的退休工资。
f_m = input('Are you male or famale?')
age = eval(input('How old are you?'))
if f_m == 'male':                          #if 6+4 < x + 5 and a > b or a < c :
    if age < 18:
        print('没满18岁，你不能工作。')
    elif age >= 18 and age < 60:
        print('满18岁，你就可以工作了，拿100%工资。')
    else:
        print('你60，你就退休了。拿3000的退休工资。')
elif f_m == 'famale':
    if age < 16:
        print('没满16岁，你不能工作。')
    elif age >= 16 and age < 55:
        print('满16岁，你就可以工作了，拿100%工资。')
    else:
        print('你55，你可以退休了。拿3000的退休工资。')
else:
    print('我们这里不收%s'%f_m)

循环结构：
1 有限循环 for i in 序列：遍历序列
    遍历range()
    for i in range(9):
        print(i)
    遍历字符串：
    for i in 'mark':
        print(i)
    遍历列表：元组，字典，等等可迭代的对象
    for i in [1,4,7,55]:
        print(i)

for i in range(1,10):       #包头不包尾
    for j in range(1,i+1):
        print('%s * %s = %s'%(j,i,i*j),end='   ')
    print()

2无限循环
while True:#True的时候运行，可以接数字，可以接字符串，只要为真就运行
    print(123)

while False:#False为假的时候不运行如：0,'',[],(),{},None,False
    print(123)

while True:
    name = input('your name？')
    if name == 'q':
        break           #退出循环体(英文表示：打断、打破的意思)
        #continue        #退出本轮循环(英文表示：继续的意思)
    elif name == 'a':
        print('ok')
    else:
        print('no')

3循环直到
n = 1
while n < 10:
    print('第%s次'%n)
    name = input('your name')
    if name == 'q':
        break
    elif n == 3:
        print('ok')
    else:
        print('no')
    n += 1

补充：continue就是跳出本轮循环，开始下一次循环。
for i in range(30):
    if i%2 == 0:
        continue
    else:
        print(i)

利用分支结构和循环结构做一道编程题：
1首先生成一个数可以自已先输入。
2请猜这个数是多少，如果猜大了，就说’猜大了‘，否则说’猜小了‘
3重复循环当你输入的数字与正确答应一样时，停止循环。
'''
# 利用分支结构和循环结构做一道编程题：
# 1首先生成一个数可以自已先输入。
# 2请猜这个数是多少，如果猜大了，就说’猜大了‘，否则说’猜小了‘
# 3重复循环当你输入的数字与正确答应一样时，停止循环。
#三分支和多分支：if elif else/if elif elif elif else/if elif elif elif
#1先询问你是男的还是女的。多少岁了
#利用分支结构和分支嵌套输出下面的信息。
#2如果你是男的：1，如果没满18岁，你不能工作。
#             2，你满18岁，你就可以工作了，拿100%工资。
#             3,如果你60，你就退休了。拿3000的退休工资。
#3如果你是女的：1，如果没满16岁，你不能工作。
#             2，你满16岁，你就可以工作了，拿100%工资。
#             3,如果你55岁，你就退休了。拿3000的退休工资。
n = 1
s = 0
while n < 101:
    s += n
    n += 1
print('从1+到100的结果为：',s)
#请用while循环做一个从1+到100的算法

#请用while循环做一个从1+乘到10的算法

#例1：用50元钱兑换为1，2，5元共25张，每种不少于1张，有多少种方案

#查找1000以内能同时被2和3整除的数

#随机生成一个数字，如果猜大了就说大了，
# 猜小了就说小了，请在10步以内猜出正确答案
