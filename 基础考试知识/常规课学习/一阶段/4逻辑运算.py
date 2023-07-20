"""
编程题：1小华的月工资是a = eval(input('工资多少'))，
n=eval(input('工作多久'))个月，3小红手上有20000元，
请编一个程序来判断，小华和小红手上的钱谁的多。

逻辑运算
and or not
and
1,都正确的情况    a  =  判断1 and 判断2           print(a)
True and True    True#返回的是第二个True
if r == True:
#     r = b
# else:
#     r = ad
# v = a or b
# r1 = a
# if r1 == True:
#     r1 = a
# else:
#     r1 = b

2 False and True  或者是   True and False,返回False.
有为空的，返回为空，否则返回False

3 False and False
首先判断左边的第一个是否正确，如果错误，返回第一个（有为空的，返回为空，否则返回False），否则返回第二个

or
1 True or True    返回第一个True

2 False or True, True or False  返回True

3 False or False 返回第2个False

not取反   not True == False,not False == True
只会返回True 和False

5 > 3 and 4 <= 6 or 5 > 6 and 'a' > 'b'

not 6 > 3 or 6 < 8 or 5
>>> True and True
True
>>> 6 + 4 > 5 and not 6 > 7
True
>>> 4*4 < 6 and 5 > 3
False
>>> '' and 6 > 2
''
>>> 6-2 and 5 > 3
True
>>> 4 and 3
3
>>> 6 + 4 > 9 and 6 > 7 or 8 > 7
True
>>> not 6 + 4 > 9 and 6 > 7 or 8 > 7
True
>>> 7+8 > 6 and 7 < 5 or 6 > 3 and 5 < 8
True
>>> 7+8 > 6 and 7 < 5
False
>>> False or
SyntaxError: invalid syntax
>>> False or 6 > 3 and 5 < 8
True
>>> 6 > 3 and 5 < 8
True
>>> False or True
True
>>> 7+8 > 6 and 7 < 5 or 6 > 3 and 5 < 8 and '' or 4
4
>>> 7+8 > 6 and 7 < 5 or 6 > 3 and 5 < 8 and ''
''

先算and 再算or  not 只在当前位置起作用。

定义域表示：3<a and a<8 。。。。。3<a<8

a = a + 1
a += 1

a = a - 1
a -= 1

a = a * 2
a *= 2

a = a / 2
a /= 2

"""
# a = eval(input('老板你好，小华一个月多少钱呢？'))
# n = eval(input('小华工作了多少个月：'))
# money = a * n
# if money > 20000:
#     print('小华的钱比小红的多')
# elif money == 20000:
#     print('小华和小红的钱一样多')
# else:
#     print('小华比小红的钱少')

#请运用算术运算，关系运算，逻辑运算编写下面程序
#语文成绩是多少？用input输入
#你的数学成绩是多少？用input输入
#你的英语成绩是多少，用input输入
#如果语文，数学，英语全都大于80分，
# 或者总分大于270，你就可以玩了
#否则你要继续学习
yw = eval(input('你的语文成绩是多少：'))
eg = eval(input('你的英语成绩是多少：'))
math1 = eval(input('你的数学成绩是多少：'))
s = yw + eg + math1
if yw > 80 and eg > 80 and math1 > 80 or s > 270:
    print('你可以玩了')
else:
    print('你还要继续学习')

'''
#请运用算术运算，关系运算，逻辑运算编写下面程序
#有一天你去买菜
#肉多少斤？用input输入
#鱼多少斤？用input输入
#小菜多少斤？用input输入
#如果肉，鱼，小菜全都大于1斤，或者总共大于5斤：
#就输出‘够吃了’，否则输出：‘还要再买点’
'''