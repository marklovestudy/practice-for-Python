'''
变量名                                       =                   值
规则：1字母，数字，下划线                                  数字类型：int,float,可以算术，关系，逻辑运算。
    2开头只能用，字母和下划线                               字符串：str,可以加法，乘法，关系，逻辑运算
    3不能包含空格                                          注：int,float,str三个值的相互转换
    4不能用关键字(help('keywords'))和内置函数                    后面会学习其他的变量
    5要具有描述性
    6区分大小写

int(变量)   #把这个变量变成整数
#要求变量是可转类型：如浮点数和整数字符串
str(变量)   #把这个变量变成字符串
float(变量)  #把这个变量变成一个浮点数
#要求变量是可转类型：如数字字符串

请判断下面数据类型
14  int     14.66   float
1.0 float   4.01    float
5   int     6.66    float
请判断下面数据类型
14           int
67           int
'1143'       str
'123'        str
4.0          float
4.66         float
7.0          float
'ass'        str
'as45'       str
'fdfh'       str

#变量名=值
#请创建字符串变量：luxy    创建一个字符串变量 lily
name1='luxy'
name2='lily'
#请创建二个浮点数变量  1.55   1.66
f1=1.55
f2=1.66
#请创建二个整数变量    22     33
n1=22
n2=33
#要求：变量名有描述性.l;

请创建变量   姓名(str)   身高(float)    年龄(int)         这里共有六个变量
同学1       ly          1.67           13              三个
name1='ly'
tall1=1.67
age1=13
同学2       yyds        1.99           15             三个
name2='yyds'
tall2=1.99
age2=15

int  转str   float
n1=22
str1=str(n1)
f1=float(n1)
str  转int   float  都是数字，所以字符串必需是数字类型的字符串
str1='66'
n1=int(str1)
f1=float(str1)

float  f1=8.55  转int  str
n1=int(f1)
str=str(f1)

请转换下面变量类型
把1转换成str存在str1中
把3转换成float存在f1中
把'123'转换成int存在n1中
把'4'转换成float存在f2中
'''



# import random as r
# a=[chr(i) for i in range(ord('a'),ord('z'))]
# r.seed(0)
# for i in range(10):
#     for j in range(3):
#         str1=''
#         for k in range(2):
#             str1+=a[r.randint(0,len(a)-1)]
#         str2 = ''
#         for k in range(2):
#             str2 += a[r.randint(0, len(a) - 1)]
#         print("'{}'+'{}'=".format(str1,str2),end='     ')
#     print()

import random as r
a=[chr(i) for i in range(ord('a'),ord('z'))]
r.seed(0)
for i in range(10):
    for j in range(3):
        str1=''
        for k in range(4):
            str1+=a[r.randint(0,len(a)-1)]
        str2 = ''
        for k in range(2):
            str2 += chr(r.randint(ord('0'),ord('9')))
        print(str1,str2,end='     ')
    print()
