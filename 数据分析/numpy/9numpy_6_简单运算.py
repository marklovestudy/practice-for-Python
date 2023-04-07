'''
NumPy 算术函数：
NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
数组必须具有相同的形状或符合数组广播规则。

import numpy as np
a = np.arange(9, dtype = np.float_).reshape(3,3)
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
b = np.array([10,10,10])
print (b)
print ('\n')
print ('两个数组相加：')
print (np.add(a,b))
print ('\n')
print ('两个数组相减：')
print (np.subtract(a,b))
print ('\n')
print ('两个数组相乘：')
print (np.multiply(a,b))
print ('\n')
print ('两个数组相除：')
print (np.divide(a,b))


'''
import numpy as np
a = np.arange(9, dtype = np.float_).reshape(3,3)
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
b = np.array([2,2,2])
print (b)

v = np.add(a,b)
print('a+b的结果是：\n',v)

v = np.subtract(a,b)
print('a-b的结果是：\n',v)

v = np.multiply(a,b)
print('a*b的结果是：\n',v)

v = np.divide(a,b)
print('a/b的结果是：\n',v)