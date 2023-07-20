"""
and or not
and
1,都正确的情况
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

not取反   not True = False,not False = True
只会返回True 和False

5 > 3 and 4 <= 6 or 5 > 6 and 'a' > 'b'

not 6 > 3 or 6 < 8 or 5

先算and 再算or  not 只在当前位置起作用。

定义域表示：3<a and a<8 。。。。3<a<8
a = a + 1
a += 1

a = a - 1
a -= 1

a = a * 2
a *= 2

a = a / 2
a /= 2

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
v_l = eval(input('左眼'))
v_r = eval(input('右眼'))
if v_l > 300 and v_r <= 300:
    print('右转')
elif v_l <= 300 and v_r > 300:
    print('左转')
elif v_l > 300 and v_r > 300:
    print('后退，再左转或右转')
else:
    print('前进')

#请设计一个程序说明每个月份的天数。
#一，input()几月份？
#二，输出这个月有多少天。
# n = input('几月份？')
# if n == '2':
#     print('这个月28天')
# elif n in '469' or n == '11':
#     print('这个月30天')
# else:
#     print('这个月31天')

for i in range(1,13):
    n = str(i)              #输入
    if n == '2':
        print('%s月28天'%n)
    elif n in '469' or n == '11':
        print('%s月30天'%n)
    else:
        print('%s月31天'%n)

各位家长您们好。今天学习的逻辑运算。让孩子们回家练习一下：
编程题：#请运用算术运算，关系运算，逻辑运算编写下面程序
#有一天你去买菜
#肉多少斤？用input输入
#鱼多少斤？用input输入
#小菜多少斤？用input输入
#如果肉，鱼，小菜全都大于1斤，或者总共大于5斤：
#就输出‘够吃了’，否则输出：‘还要再买点’
"""
