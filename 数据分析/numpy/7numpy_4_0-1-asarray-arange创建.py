'''
NumPy 创建数组：

ndarray 数组也可以通过以下几种方式来创建。
    1，numpy.empty 方法用来创建一个指定形状（ shape )、数据类型（ dtype )且未初始化的数组：
    numpy.empty ( shape , dtype = float , order = 'C')
参数说明：
    shape 数组形状
    dtype 数据类型，可选
    order 有" C 和" F "两个选项分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。
import numpy as np ＃实例
＃注意  --  数组元素为随机值，因为它们未初始化。
x = np.empty ([3,2], dtype = int )
print ( x )
[[-304086994       2046]
 [-304053152       2046]
 [    917504   16777216]]


numpy.zeros创建指定大小的数组，数组元素以 0 来填充：
numpy.zeros(shape, dtype = float, order = 'C')
参数说明：
    shape	数组形状
    dtype	数据类型，可选
    order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
import numpy as np#实例
x = np.zeros(5) # 默认为浮点数
print(x)
y = np.zeros((5,), dtype = int) # 设置类型为整数
print(y)
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  # 自定义类型
print(z)

numpy.ones创建指定形状的数组，数组元素以 1 来填充：
numpy.ones(shape, dtype = None, order = 'C')
参数说明：
    shape	数组形状
    dtype	数据类型，可选
    order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
import numpy as np#实例
x = np.ones(5) # 默认为浮点数
print(x)
x = np.ones([2,2], dtype = int)# 自定义类型
print(x)

NumPy 从已有的数组创建数组：
numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个。
numpy.asarray(a, dtype = None, order = None)
参数说明：
a	任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
dtype	数据类型，可选
order	可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个。
numpy.asarray(a, dtype = None, order = None)
实例
将元组转换为 ndarray:
import numpy as np
x =  (1,2,3)
a = np.asarray(x)
print (a)
输出结果为：
[1  2  3]

numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个。
numpy.asarray(a, dtype = None, order = None)
实例
将元组列表转换为 ndarray:
import numpy as np
x =  [(1,2,3),(4,5)]
a = np.asarray(x)
print (a)
输出结果为：
[(1, 2, 3) (4, 5)]

numpy.asarray 类似 numpy.array，但 numpy.asarray 参数只有三个。
numpy.asarray(a, dtype = None, order = None)
实例
设置了 dtype 参数：
import numpy as np
x = [1,2,3]
a = np.asarray(x, dtype = float)
print (a)
输出结果为：
[ 1.  2.  3.]

NumPy 从数值范围创建数组：
numpy.arange创建数值范围并返回 ndarray 对象，函数格式如下：
numpy.arange(start, stop, step, dtype)
根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

参数说明：
start	起始值，默认为0
stop	终止值（不包含）
step	步长，默认为1
dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。

实例1:生成 0 到 5 的数组:
import numpy as np
x = np.arange(5)
print (x)
输出结果如下：
[0  1  2  3  4]
实例2:设置返回类型位 float:
import numpy as np
x = np.arange(5, dtype =  float)  # 设置了 dtype
print (x)
输出结果如下：[0.  1.  2.  3.  4.]
实例3:设置了起始值、终止值及步长：
import numpy as np
x = np.arange(10,20,2)
print (x)
输出结果如下：[10  12  14  16  18]

'''
#numpy.empty/numpy.zeros/numpy.ones
import numpy as np
x = [(1,2,3)]
v = np.arange(100)
c=v.reshape(10,10)
v.shape=(5,20)
print(v)
print(c)