'''
八进制：oct()     0o
逢8进1，0，1，2，3，4，5，6，7


转换

十进制转化为八进制：
数学转换：
除8取余，逆序输出。（除8取余数，直到商为0，将所得余数倒排序。）
python函数转换：
>>> oct(11)
'0o13'

八进制转化为十进制：
数学转换：
按权展开，逐项相加。
'0o13'
1*8**1 +3*8**0 = 11
python函数转换：
>>> 0o13
11
>>> int('13',8)
11
'''