'''
NumPy数组属性：
NumPy的数组中比较重要ndarray对象属性有：
    1.ndarray.ndim用于返回数组的维数，等于秩。
实例
import numpy as np
a = np.arange(24)
print(a.ndim)           #a现只有一个维度

#现在调整其大小reshape
b = a.reshape(2,4,3)            #现在拥有三个维度
print(b.ndim)
输出：
1
3

    2.ndarray.shape表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性（秩）。
    比如，一个二维数组，其维度表示“行数”和”列数”。 ndarray.shape 也可以用于调整数组大小。
实例
import numpy as np
a = np.array ([[1,2,3],[4,5,6]])        #数据用[]圈起，其中的每一行代表一个元素，用[],即[[1,2,3],[4,5,6]]表二维
print(a.shape)
输出结果为：
(2,3)

实例
import numpy as np
a = np.array ([[1,2,3],[4,5,6]])
a.shape = (3,2)             #v = a.reshape(3,2) 等同,区别在于reshape是返回值，而shape是改变原数据形状
print(a)
输出结果为：
[[1 2]
 [3 4]
 [5 6]]

#同上
import numpy as np
a = np.array ([[1,2,3],[4,5,6]])
b = a.reshape(3,2)
print(b)
输出结果为：
[[1 2]
 [3 4]
 [5 6]]



    3，ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。
    例如，一个元素类型为float64的数组 itemsize 属性值为8(float64占用64个 bits ，每个字节长度为8，
    所以64/8，占用8个字节）。又如，一个元素类型为complex32的数组 item 属性为4(32/8)。
实例
import numpy as np
x = np.array ([1,2,3,4,5], dtype =np.int8)          #数组的 dtype 为int8（一个字节）
print (x.itemsize)
y = np.array ([1,2,3,4,5], dtype = np.float64)      #数组的 dtype 现在为float64（八个字节）
print (y.itemsize)
print(x,y)
输出：
1
8
[1 2 3 4 5] [1. 2. 3. 4. 5.]

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

import numpy as np#实例
x = np.zeros(5) # 默认为浮点数
print(x)
y = np.zeros((5,), dtype = int) # 设置类型为整数
print(y)
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  # 自定义类型
print(z)

'''
import numpy as np#实例
# x = np.zeros(5) # 默认为浮点数
# print(x)
# y = np.zeros((5,), dtype = int) # 设置类型为整数
# print(y)
z = np.zeros((2,2), dtype = [('x', 'i4'), ('y', 'i4')])  # 自定义类型
print(z['x'][0][0])                 #可通过索引取到每个你想要的值。
print(z['y'])
print(z)
