'''
异常处理
try:
    <语句1>           #当碰到错误语句，try代码块的剩余代码将会被忽略。
except:
    <语句2>           #except代码块的语句被执行。
例1：
try:
    a = 4/0
    print(a)
except:
    print('除数为0的错误')

例2：
try:
    a = eval(input('a=?'))
    b = eval(input('b=?'))
    s = a/b
    print('结果 = ',s)
except NameError:
    print('输入的不是数字')
except ZeroDivisionError:
    print('输入的分母为0')
except:
    print('其它错误')

异常处理
try:
    <语句块1>
except:
    <语句块2>
else:
    <语句块3>
finally:
    <语句块4>

例：执行方式1：134，方式2：124
try:
    a = eval(input('a=?'))
    b = eval(input('b=?'))
    s = a/b
    print('结果 = ',s)
except:
    print('错误')
else:
    print('正确')
finally:
    print('程序结束！')
'''

