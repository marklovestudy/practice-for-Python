'''
1,优先级：1括号，2**乘方/根运算，3//取整,%取余, *,/取浮点型,  4，，+,-

+-*/   //   %     **  ()
/结果为浮点数，浮点数的混合运算结果为浮点数
// %
>>> 5除以3=1。。。2  #   // :1    %:2
SyntaxError: invalid syntax
>>> 5//3
1
>>> 5%3
2
>>> -5除以3=-2。。。1
**
>>> 8/2
4.0
>>> 6/2
3.0
>>> 6/4
1.5
>>> 1.5+34+321
356.5
>>> 1.0*10
10.0
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
>>> 6//4
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
#2eval()
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

#str()
#str(3)------'3'

#print()   打印括号里的变量。
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


#input()   等待用户输入，然后将变量返回，属于字符串变量
#v = input()  等待用户输入，然后将变量返回,并赋值给V

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
#请写出下列运算顺序
2**3*4 + 3*8 - (6 + 4)      46
2*3/2 + 3 - 2 - (6 + 4)     -6.0