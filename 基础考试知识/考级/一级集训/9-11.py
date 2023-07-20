"""
1www.python.org     谷歌下载：系统要求，多少位（右键计算属性）。
安装细节：

2如何起动：
    1、cmd(win+r)   一，输入‘python’,二，python+' '+文件
    2、IDLE交互式的：从开始菜单里进入，要会简单的交互操作，文件操作

3快捷键：ctrl+z撤消，ctrl+c复制，ctrl+v粘贴，ctrl+A全选

4文件要怎么看：acsii   0000 0001  a     0000 1000    b  一个字节
            gbk     0000 0000 0000 0001             二个字节
            utf-8   国际通用的编码     65536

"""


# 判断题：命名
# 1在Python中变量名只能包含字母、数字和下划线。且不能以数字开头。
# 2程序:a=b中,a是变量,b是值。
# 3变量名可以随便命名。
# 4,_3a=66
# 5,a__33 = 45
# 6,a 33 = 56
# 7,import = 34
# 8,变量na和Na没有区别

#age = 13        #数字  int
#height = 1.72   #数字  float

#数字变量可以进行算术运算，关系运算，逻辑运算
#算术运算：/取浮点型，浮点型的混合运算结果都是浮点型
# 关系运算的结果是True,False
#逻辑运算返回值为真时，取后者，a = 10,b = 4    a and b 返回为b
         #为假时，返回为假。

"""

关键字怎么找help('keywords')
写一组：数字变量进行算术运算+-..，关系运算<>..，逻辑运算and,or,not。
a =  
b = 
a+b
a-b
a*b
a/b
a**b
a%b
a//b
"""
# name = 'mark'       #字符串类型的变量必需有引号，''   ""  ''' ''',""" """
# ad = "I'm ok"       #str简写方式
# nam = '城'
# #1字符串可以进行加法和乘法，可以关系运算，可以逻辑运算
# ord()
# a = input("a = ")
# b = input("b = ")
# v = a and b
# r = a
# if r == True:
#     r = b
# else:
#     r = ad
# v = a or b
# r1 = a
# if r1 == True:
#     r1 = a
# else:
#     r1 = b

#2,可以找到每个字符。
#name = "zouzihengisveryhandsome"
#       0123456789..............
#       ................-4-3-2-1
"""
name = "zouzihengisveryhandsome"
请找到8号位、3-7位、全部字符、
4到最后的字符、倒数4号位、倒数5位到倒数9位。
"""

#补充：变量的混合运算
#数字和字符串：把数字转成字符串，str()数字
#数字和数字字符串：可以把字符串转成数字，int(),float().
# str(6)   int('6')    float('4')
# 1+'5'

# 1请将678转换成字符串，请将678转换成字符串并赋值给a。
# 2请将'5.78'转换成浮点型变量。
# 3请将'65'转换成整型变量，并赋值给v
# 4请查看'65','65.6',66,68.7数据类型。type(v)
'''
1,优先级：1括号，2**乘方，3//取整,%取余, *,/取浮点型,  4，，+,-
>>> "+" > "*"
True
>>> 2**3*4 + 3*8 - (6 + 4)
46
>>> 2**3*4 + 3*8 - 10
46
>>> 8*4 +3*8 - 10
46
>>> 32+24-10
46
>>> 46
46
>>> 8/4
2.0
>>> 2 == 2.0
True
>>> 8/4
2.0
>>> 6//4b
1
>>> (8/4)*100
200.0
>>> 2.4*10
24.0
>>> 24.0//2
12.0
>>> 46
>>> 8*4 +3*8 - 10
46
>>> 32+24-10
46
>>> 46
46
>>> 8/4
2.0
>>> 2 == 2.0
True
>>> 8/4
2.0
>>> 6//4
1
>>> (8/4)*100
200.0>>> 2.4*10
24.0
>>> 24.0//2
'''
# 2eval()
'''
>>> v = eval(a)
>>> v
3
>>> type(v)
<class 'int'>
>>> b = 'zz'
>>> b
'zz'
>>> v = eval(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    v = eval(b)
  File "<string>", line 1, in <module>
NameError: name 'zz' is not defined
>>> b
'zz'
>>> v = eval('b')
>>> v
'zz'
>>> v = eval(a)
>>> v = eval(3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    v = eval(3)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> v = eval("""3""")
>>> v
3
>>> type(v)
<class 'int'>
>>> v = eval("""a""")
>>> v
'3'
>>> v = eval(""""3"""")

SyntaxError: EOL while scanning string literal
>>> v = eval("""3""")
>>> v
3
>>> v = eval(""""c"""")

SyntaxError: EOL while scanning string literal
>>> v = eval("""c""")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    v = eval("""c""")
  File "<string>", line 1, in <module>
NameError: name 'c' is not defined
>>> b
'zz'
>>> v = eval("""b""")
>>> v
'zz'
>>> v = eval("""'df'""")
>>> v
'df'
>>> v = eval('''"""fd"""''')
>>> v
'fd'
注：eval提取的内容的前提：提取完后对象是一个变量。（除掉外面的同级引号）
'''

# str()
# str(3)------'3'

# print()   打印括号里的变量。
"""
>>> print('I m ok ')
I m ok 
>>> a = 1213243214
>>> a
1213243214
>>> print(a)
1213243214
>>> print("your name" + " is " + "ackk")
your name is ackk
>>> print(a,"mark",1234)
1213243214 mark 1234
>>> 
"""

# input()   等待用户输入，然后将变量返回，属于字符串变量
# v = input()  等待用户输入，然后将变量返回,并赋值给V

"""
编程题：
1请制作一个菜单，菜单有三种商品，并标明商品的价格，请打印出菜单
2请输入三个同学的名字，三个同学的身高，并打印出来。

for i in range(3):
    name = input("classmate's name :")
    height = int(input("how high :"))
    print("%s的身高为：%d"%(name,height))
    #%f浮点型，%d整型，%s字符串

小数的位数 
print("%.2f"%2.44333)
2.44
>>> print("%.3f"%2.44333)
2.443
>>> print("%.5f"%2.44333444)
2.44333
name = input("classmate's name :")
height = int(input("how high :"))
f_d = 3.43432432432432
print("%s 的身高是：%s"%(name,height))   #占位符%s字符串，%d整型，%f浮点型
print("%s 的身高是:%d,这个小数是%.6f"%(name,height,f_d))
"""

print(6 + 6);
print('ok');
print(123)
print('6' + '6')
print('6' * 2)
"""
关系运算符： ==、<、>、<=、>=、!=
运算符 功 能 优先级 示 例 结果及说明
 ＝= 相等 4==0 False
 ！= 不相等 4!=0
 ”abc”!= ”abd” True (字符串比较完全一样时才相等)
 < 小于 5<10 True
 > 大于 ”abd”> ”abc” True (字符串比较，逐个字符比较)
 <＝ 小于等于  20<＝20True(小于或等于)
 >＝ 大于等于 ”abc”>＝”ad” False (字符”b”小于字符”d”)

 优先级：先算术运算，再关系运算。
"""

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

定义域表示：3<a and a<8 。。。。。3<a<8
"""
a = a + 1
a += 1

a = a - 1
a -= 1

a = a * 2
a *= 2

a = a / 2
a /= 2
