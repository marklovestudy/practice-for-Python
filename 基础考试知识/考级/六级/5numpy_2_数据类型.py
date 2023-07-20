'''
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

float_      float64类型的简写
float16     半精度浮点数，包括：1个符号位，5个指数位，10个尾数位
float32     单精度浮点数，包括：1个符号位，8个指数位，23个尾数位
float64     双精度浮点数，包括：1个符号位，11个指数位，52个尾数位
complex_    complex128类型的简写，即128位复数
complex64   复数，表示双32位浮点数（实数部分和虛数部分）
complex128  复数，表示双64位浮点数（实数部分和虛数部分）

numpy 的数值类型实际上是 dtype 对象的实例，并对应唯一的字符，包括 np.bool_, np.int32, np.float32，等等。

数据类型对象（ dtype ):
    数据类型对象（ numpy . dtype 类的实例）用来描述与数组对应的内存区域是如何使用的。它描述了数据的以下几个方面：
    1．数据的类型（整数，浮点数或者 Python 对象）
    2．数据的大小（例如，整数使用多少个字节存储）
    3．数据的字节顺序（小端法或大端法）
    4．在结构化类型的情况下，字段的名称、每个字段的数据类型和每个字段所取的内存块的部分
    5．如果数据类型是子数组，那么它的形状和数据类型是什么。
    字节顺序是通过对数据类型预先设定＜或＞来决定的。＜意味着小端法（最小值存储在最小的地址，即低位组放在最前面）。
    ＞意味着大端法（最重要的字节存储在最小的地址，即高位组放在最前面）。


    dtype 对象语法构造如下：
    numpy.dtype(object,align,copy)
    参数说明：
    object要转换为的数据类型对象
    align -如果为true，填充字段使其类似C的结构体。
    copy ﹣复制 dtype 对象，如果为 false ，则是对内置数据类型对象的

实例1：
import numpy as np
dt = np.dtype(np.int32)         #使用标量类型
print(dt)
输出：
int32

实例2：
import numpy as np
dt = np.dtype('i4')         #int8,int16,int32,int64四种数据类型可以使用字符串'i1','i2','i4','i8'代替，8的倍数。
print(dt)
输出：
int32

实例3：
import numpy as np
dt = np.dtype('<i4')         #字节顺序标注
print(dt)
输出：
int32

实例4，展示结构化数据类型的使用，类型字段和对应的实际类型将被创建。
import numpy as np
dt = np.dtype([('age',np.int8)])         #首先创建结构化数据类型
print(dt)
输出：
[('age', 'i1')]

实例5：
import numpy as np
dt = np.dtype([('age',np.int8)])         #将数据类型应用于ndarray对象
a = np.array([(10,),(20,),(30,)],dtype=dt)
print(a)
输出：
[(10,) (20,) (30,)]

实例6：
import numpy as np
dt = np.dtype([('age',np.int8)])         #类型字段名可以用于存取实际的age列
a = np.array([(10,),(20,),(30,)],dtype=dt)
print(a['age'])
输出：
[10 20 30]

实例7下面的示例定义一个结构化数据类型student，包含字符串段name，整数字段age,及浮点字段marks,并将这个dtype应用到ndarray对象。
import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
输出：
[('name', 'S20'), ('age', 'i1'), ('marks', '<f4')]

import numpy as np
student = np.dtype([('name','S20'),('age','i1'),('marks','f4')])#每组数据元素（name,age,marks）
a = np.array([('abc',21,50),('xyz',18,75)],dtype=student)
print(a)
输出：
[(b'abc', 21, 50.) (b'xyz', 18, 75.)]

每个内建类型都有一个唯一定义它的字符代码，如下：
字符          对应类型
b           布尔型
i           （有符号）整型
u           无符号整型 integer
f           浮点型
c           复数浮点型
m           timedelta （时间间隔）
M           datetime （日期时间）
O           ( Python ）对象
S,a         ( byte -）字符串
U           Unicode
V           原始数据（ void )

NumPy数组属性：
NumPy的数组中比较重要ndarray对象属性有：
ndarray.ndim用于返回数组的维数，等于秩。
实例
import numpy as np
a = np.arange(24)
print(a.ndim)           #a现只有一个维度

#现在调整其大小
b = a.reshape(2,4,3)            #现在拥有三个维度
print(b.ndim)
输出：
1
3
'''
import numpy as np
dt = np.dtype([('age','i8'),('name','S20'),('tall','f4')])         #使用标量类型
print(dt)
data = np.array([[(23,'mark',156),(16,'weiwei',166),(34,'dafei',171)],[(23,'ma',156),(16,'weei',166),(34,'dei',171)]],dtype=dt)      #上传数据是多维元组
print(data)

a = np.arange(24)       #0-23的序列
print(a)           #a现只有一个维度

#现在调整其大小
b = a.reshape(2,4,3)            #现在拥有三个维度,2行4列3维
print(b)                        #重新调整后为三维

