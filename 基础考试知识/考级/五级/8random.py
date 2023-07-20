'''
随机模块 random 中提供了大量与随机数和随机函数有关的对象。常用的有如下几个：
(1) randrange (start,stop,step)，返回 range (start.stop,step)范围内的随机数。
>>> random.randrange(5)
4
>>> random.randrange(1,5,2)
1
(2) randint ( start , stop )，返回闭区间［ start , stop ]）范围内的随机整数。
>>> random.randint(1,6)
5
(3) choice ( seq )，从序列 seq 中随机选择一个元素并返回。
>>> random.choice('mark')
'k'
(4) shuffle ( seq )，将列表 seq 原地打乱。
>>> x = list ( range (5))
>>> random.shuffle(x)
>>> x
[1, 0, 2, 4, 3]
(5) random ()，返回左闭右开区间［0.0,10）内的一个浮点数。
>>> random.random()
0.7844970992445616
(6) uniform ( a , b )，用于生成一个指定范围内的随机浮点数。两个参数分别是上限和下限。
>>> random.uniform(1,5)
3.6940812130637872

实例：
import random
l=['t1','t2','t3','t4','t5','t6']
m = []
a = 0
while a < 6:
    s = random.randint(6,11)
    if s not in m:
        m.append(s)
        print(l[a]+'抽签号为：'+str(s))
        a += 1
'''
import random
l=['t1','t2','t3','t4','t5','t6']
m = []
a = 0
while a < 6:
    s = random.randint(6,11)
    if s not in m:
        m.append(s)
        print(l[a]+'抽签号为：'+str(s))
        a += 1