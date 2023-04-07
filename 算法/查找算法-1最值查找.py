'''
以找最小值为例：ls=[54,13,43,7,23,2,90]   7项
步骤：1，首先将min设定为第一项的值，即min=54。
     2,然后将min和第二项比较，因为13<min,所以将min=13。
     3,和第三项比较，43>min,所以min=13。
     4,和第四项比较，7<min,所以min=7。
     5,和第五项比较，23>min,所以min=7。
     6,和第六项比较，2<min,所以min=2。
     7,和第七项比较，90>min,所以min=2。
     8，通过以上比较，最后结果为min=2。
'''
ls=[54,13,43,7,23,2,90]
min=ls[0]
for i in ls:
    if i < min:
        min=i
print('最小值为:%s'%min)

import random as r
ls=[r.randint(0,100) for i in range(25)]
print(ls)
def m_find(l,m):
    if m == '最大值':
        m=l[0]
        for i in ls:
            if i>m:
                m=i
    elif m== '最小值':
        m=l[0]
        for i in ls:
            if i < m:
                m=i
    return m
print(m_find(ls,'最大值'))
print(m_find(ls,'最小值'))