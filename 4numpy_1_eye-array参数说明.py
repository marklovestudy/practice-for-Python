'''
概念：
    NumPy(Numerical Python)是Python语言的一个扩展库，支持大量的维度数组与矩阵运算，针对数组运算提供大量的数学函数库。
    NumPy是一个运行速度非常快的数学库，主要用于数组计算。
    NumPy通常与SciPy(Scientific Python)和 Matplotlib（绘图库）一起使用，是一个强大的科学计算环境，学习数据科学或者机器学习。
    SciPy是一个开源的Python算法库和数学工具包。包含的模块有最优化、线性代数、积分、插值、特殊函数、
    快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。
    Matplotlib是Python编程语言及NumPy的可视化操作界面。它为利片通用的图形用户界面工具包
    （如Tkinter、wxPython、Qt）向应用程序嵌入式绘图提供了应用程序接口（ API )。

函数：
    1.eye(N, M=None, k=0, dtype=float, order='C', *, like=None):
        --N:输出中的行数。
        --M:输出中的列数。如果为None，则输出和N一样的列数
        --k:k=0对角线索引：0（默认值）表示主对角线，正值表示上对角线索引，负值表示到下对角线索引。
        --dtype:dtype=float表示数据类型，可选
        --order：｛'C'，'F'｝，可选输出是否应以行主（C样式）或列主要（Fortran风格）顺序。
        --like： array_like引用对象以允许创建不是 NumPy 数组的数组。
        如果作为like 传入的array-like 支持__array_function__ 协议，则结果将由它定义。
        在这种情况下，它确保创建一个与通过此参数传入的对象兼容的数组对象。

    2.numpy.array(object,dtype = None, copy = True, order = None, subok = False , ndmin =0)
        --object:对象：array-like数组、公开数组接口的任何对象、__array_方法返回数组或任何（嵌套）序列。
        --dtype：数据类型，可选阵列所需的数据类型。如果未给出，则类型将被确定为在序列
        --copy:copy：bool，可选如果为true（默认值），则复制对象。否则，副本将仅当__array_返回一个副本，
        如果obj是嵌套序列，或者如果需要副本以满足任何其他要求（“dtype”、“order”等）。
        --order:顺序：｛'K'，'A'，'C'，'F'｝，可选指定阵列的内存布局。
        如果对象不是数组除非“F”为指定，在这种情况下，它将按Fortran顺序（列主）。
        如果对象是一个数组，则如下所示。
        订单无副本=真
        保留“K”不变的F&C订单，否则最相似的订单如果输入为F而不是C，则“A”保持F顺序不变，
        否则为C顺序“C”C顺序C顺序‘F’F订单F订单
        当“copy=False”
        且出于其他原因进行复制时，结果为与“copy=True”相同，
        但“A”有一些例外，请参见注释部分。默认顺序为“K”。
        --subok：布尔，可选如果为True，则将传递子类，否则返回的数组将被强制为基类数组（默认）。
        --ndmin:int，可选,指定生成的最小尺寸数数组应具有。一个将被预先挂在形状上需要满足这一要求。
        --类似：array-like引用对象以允许创建非NumPy数组。
        如果像“like”这样传入的数组支持__array_function__``协议，将定义结果通过它。
        在这种情况下，它确保创建数组对象与通过此参数传入的兼容。

安装：
pip 安装：pip3 install -- user numpy scipy matplotlib
- user 选项设置只安装在当前的用户下，而不是写入到系统目录。使用清华的镜像：
pip3 install numpy scipy matplotlib - i https://pypi.tuna.tsinghua.edu.cn/simple
安装验证：
测试是否安装成功：
>>> from numpy import *
>>> eye(4)      #生成对角矩阵,返回对角线上为1，其他位置为0的二维数组
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.]])

Ndarray 对象：
    NumPy最重要的一个特点是N维数组对象ndarray ，它是一系列同类型数据的集合，以0下标为开始进行集合中元素的索引。
    ndarray对像是用于存放同类型元素的多维数组，它的每个元素在内存中都有相同存储大小的区域。
创建一个 ndarray :
    numpy.array(object,dtype = None, copy = True, order = None, subok = False , ndmin =0)
    ndaray对象由计算机内存的连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置。
    内存块以行顺序（样式）或列顺序（ FORTRAN或MatLab风格，即前述的F样式）来保存元素。


实例1：
import numpy as np
a = np.array([1,2,3])
print(a)
输出：
[1 2 3]

实例2：
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
输出：
[[1 2 3]
 [4 5 6]]       #不是列表中间没有逗号，是Ndarray

实例3：
import numpy as np
a = np.array([1,2,3,4,5],ndmin = 2)     #ndmin = 2表示二个[]括号，可以理解成几维。几就是几个括号。默认值是1
print(a)
输出：
[[1 2 3 4 5]]           #其中[1 2 3 4 5]是一个元素

实例4：
import numpy as np
a = np.array([1,2,3,4,5],dtype=complex)     #复数的形势
print(a)
输出：
[1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]

参数说明：
名称                  描述
object          数组或嵌套的数列
dtype           数组元素的数据类型，可选int,float,complex
copy            对象是否需要复制，可选
order           创建数组的样式， C 为行方向， F 为列方向， A 为任意方向（默认）
subok           默认返回一个与基类类型一致的数组
ndmin           指定生成数组的最小维度

NumPy 数据类型：
    numpy 支持的数据类型比 Python内置的类型要多，其中部分类型对应为Python内置的类型。常用 NumPy 基本类型：
bool_       布尔型数据类型（ True 或者 False )
int_        默认的整数类型（类似于 C 语言中的 long ,int32或int64)
intc        与 C 的 int 类型一样，一般是 int32或 int64
intp        用于索引的整数类型（类似于 C 的 ssize_t ，一般情况下仍然是int32或int64)
int8        字节（-128 to 127)
int16       整数（-32768 to 32767)
int32       整数（-2147483648 to 2147483647)
int64       鳌数（-9223372036854775808 to 922337203054775807)
uint8       无符号整数（0 to 255)
uint16      无符号整数（0 to 65535)
uint32      无符号整数（0 to 4294967295)
uint64      无符号整数（0 to 18446744073709551615)

以上数据都是周期性数据
'''
import numpy as np
dt = np.dtype([('age',np.int8)])         #使用标量类型,把数据与'age'匹配,
a = np.array([[1234,1116],[23,6789]],dtype=dt)      #数据为单个的元组类型
# print(a['age'])
# print(a)
# print(np.eye(3))
print(np.array(np.eye(4),dtype=dt))
# print(np.array(np.eye(4),dtype=dt)['age'])