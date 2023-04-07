"""
创建一个布尔类型的一维数据
import numpy as np
dt=np.dtype('bool')
print(dt)
print(type(dt))
a=np.array([1,2,3],dtype=dt)
print(a)

创建一个二维布尔类型的数据
import numpy as np
dt=np.dtype("bool")
a=np.array([[1,2,3],[0,0,2]],dtype=dt,ndmin=2)
print(a)

import numpy as np
dt=np.dtype('int8')             #i1对应int8(-128,127)   i2对应int16...
a=np.array([i*100 for i in range(5)],dtype=dt)
#[0,100,200,300,400]因为0，100没超过范围，200超过了所以拿出来256变成-56，同理300变成44，400拿二个256变成-122
print(a)
print([i*100 for i in range(5)])

创建一个无符号int类型的数据
import numpy as np
dt=np.dtype('uint8')             #i1对应int8(-128,127)   i2对应int16(-32768,32767)...
a=np.array([i*100 for i in range(5)],dtype=dt)
#[0,100,200,300,400]因为0，100没超过范围，200超过了所以拿出来256变成-56，同理300变成44，400拿二个256变成-122
print(a)
print([i*100 for i in range(5)])

创建一个浮点型类型
import numpy as np
import random as r
dt=np.dtype('float')
nums=[(-1)**i*r.random() for i in range(5)]
a=np.array(nums,dtype=dt)
print(a)
print(nums)

import numpy as np
import random as r
dt=np.dtype('float64')      #单精度
nums=[(-1)**i*r.random() for i in range(5)]
a=np.array(nums,dtype=dt)
print(a)
print(nums)

创建复数类型
import numpy as np
import random as r
dt=np.dtype('complex64')
nums=[r.random() for i in range(5)]
a=np.array(nums,dtype=dt)
print(nums)
print(a)

创建结构化类型
import numpy as np
import random as r
dt=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
nums=[('name%s'%i,r.randint(8,13),r.randint(0,100)) for i in range(9)]     #不支持中文
print(nums)
datas=np.array(nums,dtype=dt)
fo = open('aa.csv','w')
for i in datas:
    v=str(i).strip('()')
    fo.write(v+'\n')
fo.close()

#用array统计学生成绩。
import numpy as np
import random as r
dt=np.dtype([('name','S20'),('chinese','int8'),('math','int8'),('english','int8'),('all_score','int16')])
nums=[['name%s'%i,r.randint(0,100),r.randint(0,100),r.randint(0,100)] for i in range(1,50)]
for i in range(len(nums)):
    nums[i].append(sum(nums[i][1:]))
    nums[i]=tuple(nums[i])
print(nums)
datas=np.array(nums,dtype=dt)
print(datas)
"""

